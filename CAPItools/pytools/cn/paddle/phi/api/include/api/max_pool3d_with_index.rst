.. _cn_api_paddle_experimental_max_pool3d_with_index:

max_pool3d_with_index
-------------------------------

..cpp: function::std::tuple<Tensor , Tensor> max_pool3d_with_index ( const Tensor & x , const std::vector<int> & kernel_size , const std::vector<int> & strides = { 1 , 1 , 1 } , const std::vector<int> & paddings = { 0 , 0 , 0 } , bool global_pooling = false , bool adaptive = false ) ;


定义目录
:::::::::::::::::::::
paddle\phi\api\include\api.h

参数
:::::::::::::::::::::
	- **x** (const Tensor&)
	- **kernel_size** (const std::vector<int>&)
	- **strides** (const std::vector<int>&)
	- **paddings** (const std::vector<int>&)
	- **global_pooling** (bool)
	- **adaptive** (bool)

返回
:::::::::::::::::::::
std::tuple<Tensor , Tensor>
