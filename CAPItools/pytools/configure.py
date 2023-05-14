LANGUAGE = "cn"


# 获取方法中的参数parameters
def get_parameters(parameters):
    parameter_api = ""  # 这里解析是给api使用的 (暂时不用)
    parameter = "\n参数\n:::::::::::::::::::::\n"
    for i in parameters:
        parameter_type_tmp = i['type'].replace(" &", "").replace(" *", "")
        # * 和 & 情况
        # parameter_api += parameter_type_tmp
        if i["reference"] == 1:
            # parameter_api += "&"
            parameter_type_tmp += "&"
        elif i["pointer"] == 1:
            # parameter_api += "*"
            parameter_type_tmp += "*"
        # parameter_api += f" {i['name']}, "
        desc = i.get('desc', '').replace('  ', '')
        parameter += f"\t- **{i['name']}** ({parameter_type_tmp}) - {desc}\n"
    # 去掉末尾的逗号
    # parameter_api = parameter_api[:-2]
    return parameter, parameter_api

class func_helper(object):
    def __init__(self, function_dict):
        super(func_helper, self).__init__()
        self.function_dict = function_dict
        self.decode()

    def decode(self):
        # TODO 这里要看一下 operator== 这种情况能不能正常解析
        self.func_name = self.function_dict["name"]
        # 解析api
        self.api = self.function_dict["debug"].replace("PADDLE_API ", "")
        self.namespace = self.function_dict["namespace"].replace("::", "_")
        self.doxygen = self.function_dict.get("doxygen", "").replace("/**", "").replace("*/", "").replace("\n*", "").replace("  ", "")
        # TODO 如果使用已安装的 paddle 包需要调整
        self.file_path = self.function_dict["filename"].replace("../", "")

        if len(self.function_dict["parameters"]) != 0:
            self.parameter, _ = get_parameters(self.function_dict["parameters"])
        else:
            self.parameter = ""

        self.returns = self.function_dict["returns"].replace("PADDLE_API ", "")

    def create_file(self, save_dir):
        with open(save_dir, 'w') as f:
            head_text = f'.. _{LANGUAGE}_api_{self.namespace}{self.func_name}:\n' \
                        f'\n'
            f.write(head_text)

            name_and_intro_text = f'{self.func_name}\n'\
                                  f'-------------------------------\n' \
                                  f'\n' \
                                  f'..cpp: function::{self.api}\n' \
                                  f'{self.doxygen}' \
                                  f'\n'
            f.write(name_and_intro_text)

            define_path_text = f'定义目录\n' \
                               f':::::::::::::::::::::\n' \
                               f'{self.file_path}' \
                               f'\n'
            f.write(define_path_text)

            # TODO 可以统一把“参数”这样的文本移动到这里进行表达，增加代码维护性
            f.write(self.parameter+'\n')

            return_text = f'返回\n' \
                          f':::::::::::::::::::::\n' \
                          f'{self.returns}' \
                          f'\n'
            if 'void' not in self.returns:
                f.write(return_text)


# 生成函数文档
def generate_func_docs_file(data: dict):
    # TODO 这里要看一下 operator== 这种情况能不能正常解析
    func_name = data["name"]
    # 解析api
    api = data["debug"].replace("PADDLE_API ", "")
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

<name="desc">
{doxygen}
</name>

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

