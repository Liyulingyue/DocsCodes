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
LANGUAGE = "cn"


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
    return data


# 生成函数文档
def generate_func_docs_file(data: dict):
    # TODO 这里要看一下 operator== 这种情况能不能正常解析
    func_name = data["name"]
    namespace = data["namespace"].replace("::", "_")
    # TODO 如果使用已安装的 paddle 包需要调整
    file_path = data["filename"].replace("../", "")

    # 解析参数
    parameter = ""
    parameter_api = ""  # 这里解析是给api使用的
    if len(data["parameters"]) != 0:
        parameter = "\n参数\n:::::::::::::::::::::\n"
        for i in data["parameters"]:
            parameter_type_tmp = i['type'].replace(" &", "").replace(" *", "")
            # * 和 & 情况
            parameter_api += parameter_type_tmp
            if i["reference"] == 1:
                parameter_api += "&"
                parameter_type_tmp += "&"
            elif i["pointer"] == 1:
                parameter_api += "*"
                parameter_type_tmp += "*"
            parameter_api += f" {i['name']}, "
            desc = i.get('desc', '').replace('  ', '')
            parameter += f"\t- **{i['name']}** ({parameter_type_tmp}) - {desc}\n"
        # 去掉末尾的逗号
        parameter_api = parameter_api[:-2]

    # 解析返回值, 这里不用考虑空返回值, 因为空也会有 void
    returns_text = "\n返回\n:::::::::::::::::::::\n"
    returns = data["returns"].replace("PADDLE_API ", "")

    # 解析api
    api = data["debug"].replace("PADDLE_API ", "")  # 这个解析出来会有空格
    # api = f"{returns} {func_name}({parameter_api});" # 这个部分解析不到type

    # TODO 这里面的描述要根据中英文来修改
    text = f""".. _{LANGUAGE}_api_{namespace}{func_name}:
    
{func_name}
-------------------------------

.. cpp:function:: {api}

// TODO 描述: 这里用解析的

定义目录
:::::::::::::::::::::
{file_path}
{parameter}
{returns_text + returns}
"""
    # TODO 代码示例 (暂时不考虑)
    return text


# 生成类文档
def generate_class_doc_file(data: dict):
    # TODO 解析class
    pass


# 生成文件
def generate_docs(all_funcs, all_class):
    for i in all_funcs:
        path = i["filename"].replace("../", "").replace(".h", "")
        if not os.path.exists("./" + path):
            os.makedirs("./" + path)
        text = generate_func_docs_file(i)

        # TODO 这个反斜杠需要单独处理看看
        func_name = i["name"].replace("/", "")
        f = open("./" + path + "/" + func_name + ".rst", "w")
        f.write(text)

    for i in all_class:
        path = i["filename"].replace("../", "").replace(".h", "")
        if not os.path.exists("./" + path):
            os.makedirs("./" + path)


if __name__ == "__main__":
    # file_path = '../paddle/phi/api/include/api.h'
    # file_path = '../paddle/phi/api/include/context_pool.h'
    # data = analysis_file(file_path)
    # print(get_PADDLE_API_class(data))

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
            # print(get_PADDLE_API_func(data))
            # print(get_PADDLE_API_class(data))
            # if len(all_class) != 0:
            #     generate_docs(all_funcs, all_class)
            #     exit()
            all_funcs.extend(get_PADDLE_API_func(data))
            all_class.extend(get_PADDLE_API_class(data))

    generate_docs(all_funcs, all_class)
    print("PADDLE_API func count: ", len(all_funcs))
    print("PADDLE_API class count: ", len(all_class))
