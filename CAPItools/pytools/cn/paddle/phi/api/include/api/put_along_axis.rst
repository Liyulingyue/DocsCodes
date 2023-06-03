.. _cn_api_paddle_experimental_put_along_axis:

put_along_axis
-------------------------------

..cpp: function::Tensor put_along_axis ( const Tensor & arr , const Tensor & indices , const Tensor & values , int axis , const std::string & reduce = "assign" ) ;


本 API 与 Python API 对齐，详细用法可参考链接：[paddle.put_along_axis](https://www.paddlepaddle.org.cn/documentation/docs/zh/api/paddle/put_along_axis_cn.html)

定义目录
:::::::::::::::::::::
paddle\phi\api\include\api.h

参数
:::::::::::::::::::::
	- **arr** (const Tensor&)
	- **indices** (const Tensor&)
	- **values** (const Tensor&)
	- **axis** (int)
	- **reduce** (const std::string&)

返回
:::::::::::::::::::::
Tensor
