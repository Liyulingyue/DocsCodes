.. _en_api_paddle_experimental_unique:

unique
-------------------------------

..cpp: function::std::tuple<Tensor , Tensor , Tensor , Tensor> unique ( const Tensor & x , bool return_index , bool return_inverse , bool return_counts , const std::vector<int> & axis , DataType dtype = DataType::INT64 ) ;


This API is aligned with Python API, more details are shown in [paddle.unique](https://www.paddlepaddle.org.cn/documentation/docs/zh/api/paddle/unique_en.html)

Path
:::::::::::::::::::::
paddle\phi\api\include\api.h

Parameters
:::::::::::::::::::::
	- **x** (const Tensor&)
	- **return_index** (bool)
	- **return_inverse** (bool)
	- **return_counts** (bool)
	- **axis** (const std::vector<int>&)
	- **dtype** (DataType)

Returns
:::::::::::::::::::::
std::tuple<Tensor , Tensor , Tensor , Tensor>
