import CppHeaderParser
import json
import os

from configure import generate_func_docs_file, generate_class_doc_file
from configure import func_helper

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



# 获取存在 PADDLE_API func 数组的名称
def get_PADDLE_API_func(data: dict):
    result = []
    for i in data["functions"]:
        if 'PADDLE_API' in i['debug']:
            result.append(i)
    return result


# 获取存在 PADDLE_API class 数组的名称
def get_PADDLE_API_class(data: dict):
    result = []
    for classname in data["classes"]:
        # TODO 目前没有 PADDLE_API 是 struct 的
        if data["classes"][classname]["declaration_method"] == "struct":
            continue

        # TODO 这里需要处理一下, 因为类名和 PADDLE_API 会粘在一起, 例: PADDLE_APIDeviceContextPool
        if "PADDLE_API" in classname:
            result.append(data["classes"][classname])
    return result


# 获取namespace
# 多线程使用并不安全, 请不要使用多线程
def analysis_file(path):
    header = CppHeaderParser.CppHeader(path, encoding='utf8')
    data = json.loads(header.toJSON())
    return data


# 生成文件
def generate_docs(all_funcs, all_class):
    for item in all_funcs:
        path = item["filename"].replace("../", "").replace(".h", "")
        if not os.path.exists("./" + path):
            os.makedirs("./" + path)
        text = generate_func_docs_file(item)

        # TODO 这个反斜杠需要单独处理看看
        func_name = item["name"].replace("/", "")
        rst_dir = os.path.join(".", path, func_name+".rst")
        # avoid a filename such as operate*.rst
        try:
            helper = func_helper(item)
            helper.create_file(rst_dir)
            # with open(rst_dir, "w") as f:
            #     f.write(text)
        except:
            print('FAULT GENERATE:' + rst_dir)

    for i in all_class:
        path = i["filename"].replace("../", "").replace(".h", "")
        if not os.path.exists("./" + path):
            os.makedirs("./" + path)
        text = generate_class_doc_file(i)

        func_name = i["name"].replace("PADDLE_API", "")
        rst_dir = os.path.join(".", path, func_name+".rst")
        with open(rst_dir, "w") as f:
            f.write(text)


if __name__ == "__main__":
    all_funcs = []
    all_class = []
    root_dir = '../paddle'
    for home, dirs, files in os.walk(root_dir):
        for file_name in files:
            # 跳过文件中未包含PADDLE_API
            file_path = os.path.join(home, file_name)
            with open(file_path, encoding='utf8') as f:
                if 'PADDLE_API ' not in f.read():
                    continue

            print("Parsing: ", file_path)
            data = analysis_file(file_path)
            all_funcs.extend(get_PADDLE_API_func(data))
            all_class.extend(get_PADDLE_API_class(data))

    generate_docs(all_funcs, all_class)
    print("PADDLE_API func count: ", len(all_funcs))
    print("PADDLE_API class count: ", len(all_class))
