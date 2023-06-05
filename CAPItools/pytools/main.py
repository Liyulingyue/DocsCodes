# python main.py [source dir] [target dir]
# python main.py ../paddle .


import CppHeaderParser
import json
import os
import traceback
import sys
import re

from utils_helper import func_helper, class_helper, generate_overview
from utils import get_PADDLE_API_class, get_PADDLE_API_func


# 获取namespace
# 多线程使用并不安全, 请不要使用多线程
def analysis_file(path):
    header = CppHeaderParser.CppHeader(path, encoding='utf8')
    data = json.loads(header.toJSON())
    return data


# 生成文件
def generate_docs(all_funcs, all_class, cpp2py_api_list, save_dir, LANGUAGE="cn"):
    for item in all_funcs:
        path = item["filename"].replace("../", "").replace(".h", "")
        dir_path = os.path.join(save_dir, LANGUAGE, path)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        # 这个反斜杠需要单独处理, 在 linux 下
        func_name = item["name"].replace("/", "")

        # Note: 操作符仅不生成rst，实际上在Overview列表依然会呈现以提示存在此操作符
        if func_name.startswith('operator'):
            checkwords = func_name.replace('operator', '', 1)
            if re.search(r"\w", checkwords) == None:
                continue  # 跳过操作符声明
        rst_dir = os.path.join(save_dir, LANGUAGE, path, func_name + ".rst")
        # avoid a filename such as operate*.rst, only windows
        try:
            helper = func_helper(item, cpp2py_api_list)
            helper.create_and_write_file(rst_dir, LANGUAGE)
        except:
            print(traceback.format_exc())
            print('FAULT GENERATE:' + rst_dir)

    for item in all_class:
        path = item["filename"].replace("../", "").replace(".h", "")
        dir_path = os.path.join(save_dir, LANGUAGE, path)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        func_name = item["name"].replace("PADDLE_API", "")
        rst_dir = os.path.join(save_dir, LANGUAGE, path, func_name + ".rst")
        try:
            helper = class_helper(item)
            helper.create_and_write_file(rst_dir, LANGUAGE)
        except:
            print(traceback.format_exc())
            print('FAULT GENERATE:' + rst_dir)


# cpp 对应 python api
def cpp2py(data: dict):
    cpp2py_api_list = []
    for i in data["using"]:
        cpp2py_api_list.append(i.replace("paddle::", ""))

    return cpp2py_api_list


if __name__ == "__main__":
    root_dir = ''
    save_dir = '.'  # 默认保存在当前目录
    if len(sys.argv) == 3:
        root_dir = sys.argv[1]
        save_dir = sys.argv[2]

    if root_dir == '':
        try:
            import paddle
            import inspect

            root_dir = os.path.dirname(inspect.getsourcefile(paddle))
        except:
            # for simple run
            root_dir = '../paddle'
            save_dir = '.'

    all_funcs = []
    all_class = []
    cpp2py_api_list = []
    overview_list = []
    for home, dirs, files in os.walk(root_dir):
        for file_name in files:
            # 跳过不需要处理的文件
            if file_name.split(".")[-1] not in ["cc", "cu", "h"]:
                continue

            file_path = os.path.join(home, file_name)
            # 处理 cpp 和 py api对应的文件
            if file_name == "tensor_compat.h":
                cpp2py_data = analysis_file(file_path)
                cpp2py_api_list = cpp2py(cpp2py_data).copy()

            # 跳过文件中未包含PADDLE_API
            with open(file_path, encoding='utf-8') as f:
                if 'PADDLE_API ' not in f.read():
                    continue

            print("Parsing: ", file_path)
            data = analysis_file(file_path)

            # 信息抽取
            current_func = get_PADDLE_API_func(data)
            current_class = get_PADDLE_API_class(data)

            # 信息记录
            all_funcs.extend(current_func)
            all_class.extend(current_class)
            overview_list.append({'h_file': file_path, 'class': current_class, 'function': current_func})

    generate_docs(all_funcs, all_class, cpp2py_api_list, save_dir, "cn")
    generate_docs(all_funcs, all_class, cpp2py_api_list, save_dir, "en")

    # overview
    generate_overview(overview_list, save_dir, "cn")
    generate_overview(overview_list, save_dir, "en")

    print("PADDLE_API func count: ", len(all_funcs))
    print("PADDLE_API class count: ", len(all_class))
    print("cpp2py api count: ", len(cpp2py_api_list))
