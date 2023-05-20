.. _en_api_paddle_experimental_unique_consecutive:

unique_consecutive
-------------------------------

..cpp: function::std::tuple<Tensor , Tensor , Tensor> unique_consecutive ( const Tensor & x , bool return_inverse = false , bool return_counts = false , const std::vector<int> & axis = { } , int dtype = 5 ) ;


定义目录
:::::::::::::::::::::
paddle\phi\api\include\api.h

参数
:::::::::::::::::::::
	- **x** (const Tensor&)
	- **return_inverse** (bool)
	- **return_counts** (bool)
	- **axis** (const std::vector<int>&)
	- **dtype** (int)

返回
:::::::::::::::::::::
std::tuple<Tensor , Tensor , Tensor>
