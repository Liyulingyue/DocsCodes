.. _en_api_paddle_experimental_unique:

unique
-------------------------------

..cpp: function::std::tuple<Tensor , Tensor , Tensor , Tensor> unique ( const Tensor & x , bool return_index , bool return_inverse , bool return_counts , const std::vector<int> & axis , DataType dtype = DataType::INT64 ) ;


本 API 与 Python API 对齐，详细用法可参考链接：[paddle.unique](https://www.paddlepaddle.org.cn/documentation/docs/zh/api/paddle/unique_en.html)

定义目录
:::::::::::::::::::::
paddle\phi\api\include\api.h

参数
:::::::::::::::::::::
	- **x** (const Tensor&)
	- **return_index** (bool)
	- **return_inverse** (bool)
	- **return_counts** (bool)
	- **axis** (const std::vector<int>&)
	- **dtype** (DataType)

返回
:::::::::::::::::::::
std::tuple<Tensor , Tensor , Tensor , Tensor>
