# 获取方法中的参数parameters
def get_parameters(parameters):
    # parameter_api = ""  # 这里解析是给api使用的 (暂时不用)
    parameter_dict = []
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
        parameter_dict.append({'name': i['name'],
                               'type': parameter_type_tmp,
                               'intro': desc})
        # parameter += f"\t- **{i['name']}** ({parameter_type_tmp}) - {desc}\n"
    # 去掉末尾的逗号
    # parameter_api = parameter_api[:-2]
    # return parameter, parameter_api
    return parameter_dict