from utils import get_parameters


class func_helper(object):
    def __init__(self, function_dict, cpp2py_api_list, language):
        super(func_helper, self).__init__()
        self.function_dict = function_dict
        self.cpp2py_api_list = cpp2py_api_list
        self.LANGUAGE = language
        self.decode()

    def decode(self):
        # TODO 这里要看一下 operator== 这种情况能不能正常解析
        self.func_name = self.function_dict["name"]
        # 解析api
        self.api = self.function_dict["debug"].replace("PADDLE_API ", "")
        self.namespace = self.function_dict["namespace"].replace("::", "_")
        self.doxygen = self.function_dict.get("doxygen", "").replace("/**", "").replace("*/", "").replace("\n*",
                                                                                                          "").replace(
            "  ", "")
        # TODO 如果使用已安装的 paddle 包需要调整
        self.file_path = self.function_dict["filename"].replace("../", "")

        if len(self.function_dict["parameters"]) != 0:
            self.parameter_dict = get_parameters(self.function_dict["parameters"])
        else:
            self.parameter_dict = {}

        self.returns = self.function_dict["returns"].replace("PADDLE_API ", "")

    def create_file(self, save_dir):
        with open(save_dir, 'w', encoding='utf8') as f:
            head_text = f'.. _{self.LANGUAGE}_api_{self.namespace}{self.func_name}:\n' \
                        f'\n'
            f.write(head_text)

            name_and_intro_text = f'{self.func_name}\n' \
                                  f'-------------------------------\n' \
                                  f'\n' \
                                  f'..cpp: function::{self.api}\n' \
                                  f'{self.doxygen}' \
                                  f'\n'
            f.write(name_and_intro_text)

            if self.func_name in self.cpp2py_api_list:
                cpp2py_text = f'本 API 与 Python API 对齐，详细用法可参考链接：' \
                              f'[paddle.{self.func_name}]' \
                              f'(https://www.paddlepaddle.org.cn/documentation/docs/zh/api/paddle/{self.func_name}_{self.LANGUAGE}.html)' \
                              f'\n\n'
                f.write(cpp2py_text)

            define_path_text = f'定义目录\n' \
                               f':::::::::::::::::::::\n' \
                               f'{self.file_path}\n' \
                               f'\n'
            f.write(define_path_text)

            if len(self.parameter_dict) != 0:
                parameters_text = f'参数\n' \
                                  f':::::::::::::::::::::'
                f.write(parameters_text + '\n')
                for param in self.parameter_dict:
                    param_text = f"\t- **{param['name']}**"
                    if param['type'] != "":
                        param_text += f" ({param['type']})"
                    if param['intro'] != "":
                        param_text += f" - {param['intro']}"
                    param_text += "\n"
                    f.write(param_text)
            f.write('\n')

            return_text = f'返回\n' \
                          f':::::::::::::::::::::\n' \
                          f'{self.returns}' \
                          f'\n'
            if 'void' not in self.returns:
                f.write(return_text)


class class_helper(object):
    def __init__(self, class_dict, language):
        super(class_helper, self).__init__()
        self.class_dict = class_dict
        self.LANGUAGE = language
        self.decode()

    def decode(self):
        self.branch = "develop"  # TODO 这里可以看看从包里面获取
        self.class_name = self.class_dict["name"].replace("PADDLE_API", "")
        # TODO 如果使用已安装的 paddle 包需要调整
        self.file_path = self.class_dict["filename"].replace("../", "")
        self.doxygen = self.class_dict.get("doxygen", "").replace("/**", "").replace("*/", "").replace("\n*",
                                                                                                       "").replace("  ",
                                                                                                                   "")
        # 初始化函数
        # 避免空函数解析
        self.init_func = self.class_name

        self.functions_infor = []
        self.class_function_number = len(self.class_dict["methods"]["public"])
        for i in range(self.class_function_number):
            ith_function = self.class_dict["methods"]["public"][i]
            if self.class_name in ith_function["name"] and len(ith_function["debug"]) > len(self.init_func):
                self.init_func = ith_function["debug"]

            function_name = ith_function['debug']
            # 获取描述
            funcs_doxygen = ith_function.get("doxygen", "").replace("/**", "").replace("*/", "").replace("\n*",
                                                                                                         "").replace(
                "  ", "")
            # 解析参数
            if len(ith_function["parameters"]) != 0:
                parameter_dict = get_parameters(ith_function["parameters"])
            else:
                parameter_dict = {}
            # 获取返回值
            returns = ith_function["returns"].replace("PADDLE_API ", "")

            self.functions_infor.append({'name': function_name,
                                         'doxygen': funcs_doxygen,
                                         'parameter': parameter_dict,
                                         'returns': returns})

    def create_file(self, save_dir):
        with open(save_dir, 'w', encoding='utf8') as f:
            head_text = f'.. _{self.LANGUAGE}_api_{self.class_name}:\n' \
                        f'\n'
            f.write(head_text)

            name_and_intro_text = f'{self.class_name}[源代码](https://github.com/PaddlePaddle/Paddle/blob/{self.branch}/{self.file_path})\n' \
                                  f'-------------------------------\n' \
                                  f'\n' \
                                  f'.. cpp:class:: {self.init_func}\n' \
                                  f'{self.doxygen}\n' \
                                  f'\n'
            f.write(name_and_intro_text)

            define_path_text = f'定义目录\n' \
                               f':::::::::::::::::::::\n' \
                               f'{self.file_path}\n' \
                               f'\n'
            f.write(define_path_text)

            if self.class_function_number != 0:
                class_function_head_text = f'方法\n' \
                                           f':::::::::::::::::::::\n' \
                                           f'\n'
                f.write(class_function_head_text)

                for fun_infor in self.functions_infor:
                    fun_name_and_intro_text = f"{fun_infor['name']}\n" \
                                              f"\'\'\'\'\'\'\'\'\'\'\'\n" \
                                              f"{fun_infor['doxygen']}\n" \
                                              f"\n"
                    f.write(fun_name_and_intro_text)

                    if len(fun_infor['parameter']) != 0:
                        parameters_text = f"**参数**\n" \
                                          f"\'\'\'\'\'\'\'\'\'\'\'\n"
                        f.write(parameters_text)
                        for param in fun_infor['parameter']:
                            param_text = f"\t- **{param['name']}**"
                            if param['type'] != "":
                                param_text += f" ({param['type']})"
                            if param['intro'] != "":
                                param_text += f" - {param['intro']}"
                            param_text += "\n"
                            f.write(param_text)
                    f.write('\n')

                    if fun_infor['returns'] != '' and 'void' not in fun_infor['returns']:
                        fun_return_text = f"**返回**\n" \
                                          f"\'\'\'\'\'\'\'\'\'\'\'\n" \
                                          f"{fun_infor['returns']}" \
                                          f"\n"
                        f.write(fun_return_text)

def generate_overview(overview_list, LANGUAGE):
    pass