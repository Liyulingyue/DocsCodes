.. _cn_api_paddle_experimental_conv2d_transpose:

conv2d_transpose
-------------------------------

..cpp: function::Tensor conv2d_transpose ( const Tensor & x , const Tensor & filter , const std::vector<int> & strides , const std::vector<int> & paddings , const std::vector<int> & output_padding , const IntArray & output_size , const std::string & padding_algorithm , int groups , const std::vector<int> & dilations , const std::string & data_format ) ;

定义目录
:::::::::::::::::::::
paddle\phi\api\include\api.h

参数
:::::::::::::::::::::
	- **x** (const Tensor&) - 
	- **filter** (const Tensor&) - 
	- **strides** (const std::vector<int>&) - 
	- **paddings** (const std::vector<int>&) - 
	- **output_padding** (const std::vector<int>&) - 
	- **output_size** (const IntArray&) - 
	- **padding_algorithm** (const std::string&) - 
	- **groups** (int) - 
	- **dilations** (const std::vector<int>&) - 
	- **data_format** (const std::string&) - 

返回
:::::::::::::::::::::
Tensor
