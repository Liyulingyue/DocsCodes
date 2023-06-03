.. _en_api_paddle_experimental_conv3d:

conv3d
-------------------------------

..cpp: function::Tensor conv3d ( const Tensor & input , const Tensor & filter , const std::vector<int> & strides , const std::vector<int> & paddings , const std::string & padding_algorithm , int groups , const std::vector<int> & dilations , const std::string & data_format ) ;


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
	- **groups** (int)
	- **dilations** (const std::vector<int>&)
	- **data_format** (const std::string&)

Returns
:::::::::::::::::::::
Tensor
