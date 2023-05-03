import CppHeaderParser
import json
import os

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
    header = CppHeaderParser.CppHeader(path)
    data = json.loads(header.toJSON())
    # print(header.toJSON())
    # print(data)
    # print(type(data))
    return data


if __name__ == "__main__":
    # file_path = '../paddle/phi/api/include/api.h'
    # file_path = '../paddle/phi/api/include/context_pool.h'
    # data = analysis_file(file_path)
    # print(get_PADDLE_API_class(data))

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
            print(get_PADDLE_API_class(data))
