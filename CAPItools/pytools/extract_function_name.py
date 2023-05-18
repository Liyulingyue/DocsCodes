import CppHeaderParser
import json
import os

from utils_helper import func_helper, class_helper, generate_overview
from utils import get_PADDLE_API_class, get_PADDLE_API_func

# TODO 通过已安装的 paddle 来查找 include
# import paddle
# import inspect
#
# # 获取已安装paddle的路径
# print(os.path.dirname(inspect.getsourcefile(paddle)))


# TODO 需要单独处理一下这种
"""
#if defined(PADDLE_WITH_CUDA) || defined(PADDLE_WITH_HIP)
/**
 * Get the current CUDA stream for the passed CUDA device.
 */
PADDLE_API phi::CUDAStream* GetCurrentCUDAStream(const phi::Place& place);
#endif
"""


# 获取namespace
# 多线程使用并不安全, 请不要使用多线程
def analysis_file(path):
    header = CppHeaderParser.CppHeader(path, encoding='utf8')
    data = json.loads(header.toJSON())
    return data


# 生成文件
def generate_docs(all_funcs, all_class, cpp2py_api_list, LANGUAGE = "cn"):
    for item in all_funcs:
        path = item["filename"].replace("../", "").replace(".h", "")
        dir_path = os.path.join(".", LANGUAGE, path)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        # 这个反斜杠需要单独处理, 在 linux 下
        func_name = item["name"].replace("/", "")
        rst_dir = os.path.join(".", LANGUAGE, path, func_name + ".rst")
        # avoid a filename such as operate*.rst, only windows
        try:
            helper = func_helper(item, cpp2py_api_list, LANGUAGE)
            helper.create_file(rst_dir)
        except:
            print('FAULT GENERATE:' + rst_dir)

    for item in all_class:
        path = item["filename"].replace("../", "").replace(".h", "")
        dir_path = os.path.join(".", LANGUAGE, path)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        func_name = item["name"].replace("PADDLE_API", "")
        rst_dir = os.path.join(".", LANGUAGE, path, func_name + ".rst")
        try:
            helper = class_helper(item, LANGUAGE)
            helper.create_file(rst_dir)
        except:
            print('FAULT GENERATE:' + rst_dir)


# cpp 对应 python api
def cpp2py(data: dict):
    cpp2py_api_list = []
    for i in data["using"]:
        cpp2py_api_list.append(i.replace("paddle::", ""))

    return cpp2py_api_list


if __name__ == "__main__":
    LANGUAGE = "cn"
    all_funcs = []
    all_class = []
    cpp2py_api_list = []
    overview_list = []
    root_dir = '../paddle'
    for home, dirs, files in os.walk(root_dir):
        for file_name in files:
            file_path = os.path.join(home, file_name)
            # 处理 cpp 和 py api对应的文件
            if file_name == "tensor_compat.h":
                cpp2py_data = analysis_file(file_path)
                cpp2py_api_list = cpp2py(cpp2py_data).copy()

            # 跳过文件中未包含PADDLE_API
            with open(file_path, encoding='utf8') as f:
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
            overview_list.append({'h_file':file_path,'class':current_class,'function':current_func})

    generate_docs(all_funcs, all_class, cpp2py_api_list, LANGUAGE)

    # TODO: delete the try-except after every thing is prepare
    try:
        generate_overview(overview_list, LANGUAGE)
    except:
        pass

    print("PADDLE_API func count: ", len(all_funcs))
    print("PADDLE_API class count: ", len(all_class))
    print("cpp2py api count: ", len(cpp2py_api_list))
