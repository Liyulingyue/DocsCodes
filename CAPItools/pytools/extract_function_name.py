import re


def analysis_function_type1(text):
    """
        主要解析的结构如下:
        ```
        PADDLE_API Tensor acos(const Tensor& x);
        ```
    Args:
        text: 文件内容

    Returns:
        func_data: 函数返回值和输入参数
        func_name: 函数名
    """
    # 获取所在行
    func_line = re.findall(r"PADDLE_API (.*?)\n", text, re.DOTALL)
    for i in func_line:
        # 处理返回值[0],和输入参数[1]
        func_data = re.split(r'(.*?) [a-zA-Z0-9_]*?\((.*?)\);', i)[1:-1]
        # 处理函数名
        func_name = re.search(r' [a-zA-Z0-9_]*?\([a-zA-Z_]', i).group()[:-2]
    return func_data, func_name


# TODO 这里要考虑到部分函数不包含的情况(放在外层)
"""
namespace A{

namespace B{
} // namespace B

namespace C{
} // namespace C

} // namespace A
"""
def analysis_namespace(text):
    """
        主要解析的结构如下:
        ```
        namespace paddle {
        namespace framework {
        ```
    Args:
        text: 文件内容

    Returns:
        namespace: 最外层namespace
        data: 去除最外层namespace的内容
    """
    # 提取第一个 namespace
    namespace = re.split(r'namespace (.*?) \{', text)
    data = text.split('namespace ' + namespace[1] + " {")[1].split('}  // namespace ' + namespace[1])[0]
    return namespace, data


# if __name__ == "__main__":
#     file_path = '../paddle/phi/api/include/api.h'
#     with open(file_path, 'r') as f:
#         file_content = f.read()
#         analysis_namespace(file_content)
