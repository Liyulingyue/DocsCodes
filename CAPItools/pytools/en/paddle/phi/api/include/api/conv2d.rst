.. _en_api_paddle_experimental_conv2d:

conv2d
-------------------------------

..cpp: function::Tensor conv2d ( const Tensor & input , const Tensor & filter , const std::vector<int> & strides , const std::vector<int> & paddings , const std::string & padding_algorithm , const std::vector<int> & dilations , int groups , const std::string & data_format ) ;


Path
:::::::::::::::::::::
paddle\phi\api\include\api.h

Parameters
:::::::::::::::::::::
	- **input** (const Tensor&)
	- **filter** (const Tensor&)
	- **strides** (const std::vector<int>&)
	- **paddings** (const std::vector<int>&)
	- **padding_algorithm** (const std::string&)
	- **dilations** (const std::vector<int>&)
	- **groups** (int)
	- **data_format** (const std::string&)

Returns
:::::::::::::::::::::
Tensor
