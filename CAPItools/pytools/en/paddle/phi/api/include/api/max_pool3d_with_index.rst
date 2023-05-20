.. _en_api_paddle_experimental_max_pool3d_with_index:

max_pool3d_with_index
-------------------------------

..cpp: function::std::tuple<Tensor , Tensor> max_pool3d_with_index ( const Tensor & x , const std::vector<int> & kernel_size , const std::vector<int> & strides , const std::vector<int> & paddings , bool global_pooling , bool adaptive ) ;


Path
:::::::::::::::::::::
paddle\phi\api\include\api.h

Parameters
:::::::::::::::::::::
	- **x** (const Tensor&)
	- **kernel_size** (const std::vector<int>&)
	- **strides** (const std::vector<int>&)
	- **paddings** (const std::vector<int>&)
	- **global_pooling** (bool)
	- **adaptive** (bool)

Returns
:::::::::::::::::::::
std::tuple<Tensor , Tensor>
