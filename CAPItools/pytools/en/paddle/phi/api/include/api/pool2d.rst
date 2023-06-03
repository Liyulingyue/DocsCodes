.. _en_api_paddle_experimental_pool2d:

pool2d
-------------------------------

..cpp: function::Tensor pool2d ( const Tensor & x , const IntArray & kernel_size , const std::vector<int> & strides , const std::vector<int> & paddings , bool ceil_mode , bool exclusive , const std::string & data_format , const std::string & pooling_type , bool global_pooling , bool adaptive , const std::string & padding_algorithm ) ;


Path
:::::::::::::::::::::
paddle\phi\api\include\api.h

Parameters
:::::::::::::::::::::
	- **x** (const Tensor&)
	- **kernel_size** (const IntArray&)
	- **strides** (const std::vector<int>&)
	- **paddings** (const std::vector<int>&)
	- **ceil_mode** (bool)
	- **exclusive** (bool)
	- **data_format** (const std::string&)
	- **pooling_type** (const std::string&)
	- **global_pooling** (bool)
	- **adaptive** (bool)
	- **padding_algorithm** (const std::string&)

Returns
:::::::::::::::::::::
Tensor
