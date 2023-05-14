# 生成函数文档
def generate_func_docs_file(data: dict):
    # TODO 这里要看一下 operator== 这种情况能不能正常解析
    func_name = data["name"]
    namespace = data["namespace"].replace("::", "_")
    doxygen = data.get("doxygen", "").replace("/**", "").replace("*/", "").replace("\n*", "").replace("  ", "")
    # TODO 如果使用已安装的 paddle 包需要调整
    file_path = data["filename"].replace("../", "")

    # 解析参数
    parameter = ""
    if len(data["parameters"]) != 0:
        parameter, parameter_api = get_parameters(data["parameters"])

    # 解析返回值, 这里不用考虑空返回值, 因为空也会有 void
    returns_text = "\n返回\n:::::::::::::::::::::\n"
    returns = data["returns"].replace("PADDLE_API ", "")

    # 解析api
    api = data["debug"].replace("PADDLE_API ", "")  # 这个解析出来会有空格
    # api = f"{returns} {func_name}({parameter_api});" # 这个有部分api解析不到type

    # TODO 这里面的描述要根据中英文来修改
    text = f""".. _{LANGUAGE}_api_{namespace}{func_name}:

{func_name}
-------------------------------

.. cpp:function:: {api}

<--! name="desc" -->
{doxygen}
<--! /name -->

定义目录
:::::::::::::::::::::
{file_path}
{parameter}
{returns_text + returns}

<name="reference_link">

</name>

"""
    # TODO 参考链接
    # TODO 代码示例 (暂时不考虑)
    return text


# 生成类文档
def generate_class_doc_file(data: dict):
    branch = "develop"  # TODO 这里可以看看从包里面获取
    class_name = data["name"].replace("PADDLE_API", "")
    # TODO 如果使用已安装的 paddle 包需要调整
    file_path = data["filename"].replace("../", "")
    doxygen = data.get("doxygen", "").replace("/**", "").replace("*/", "").replace("\n*", "").replace("  ", "")
    # 初始化函数
    init_func = class_name
    funcs = ""
    parameter = ""
    if len(data["methods"]["public"]) != 0:
        funcs += "方法\n:::::::::::::::::::::\n"
        for i in data["methods"]["public"]:
            if class_name in i["name"] and len(i["debug"]) > len(init_func):
                init_func = i["debug"]
            # 获取描述
            funcs_doxygen = i.get("doxygen", "").replace("/**", "").replace("*/", "").replace("\n*", "").replace("  ",
                                                                                                                 "")
            # 解析参数
            parameter = ""
            if len(i["parameters"]) != 0:
                parameter, parameter_api = get_parameters(i["parameters"])
            # 获取返回值
            returns = i["returns"].replace("PADDLE_API ", "")
            if returns == "":
                returns = "无"
            funcs += f"""{i["debug"]}
'''''''''
<name="desc">
{funcs_doxygen}
</name>

{parameter}
返回
:::::::::::::::::::::
{returns}

"""

    text = f""".. _cn_api_{class_name}:

{class_name}[源代码](https://github.com/PaddlePaddle/Paddle/blob/{branch}/{file_path})
-------------------------------

.. cpp:class:: {init_func}

<name="desc">
{doxygen}
</name>

定义目录
:::::::::::::::::::::
{file_path}

{funcs}

<name="reference_link">

</name>

"""
    # TODO 参考链接
    # TODO 代码示例 (暂时不考虑)
    return text

