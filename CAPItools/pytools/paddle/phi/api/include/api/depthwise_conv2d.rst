.. _cn_api_paddle_experimental_depthwise_conv2d:

depthwise_conv2d
-------------------------------

..cpp: function::Tensor depthwise_conv2d ( const Tensor & x , const Tensor & filter , const std::vector<int> & strides , const std::vector<int> & paddings , const std::string & padding_algorithm , int groups , const std::vector<int> & dilations , const std::string & data_format ) ;

定义目录
:::::::::::::::::::::
paddle\phi\api\include\api.h

参数
:::::::::::::::::::::
	- **x** (const Tensor&) - 
	- **filter** (const Tensor&) - 
	- **strides** (const std::vector<int>&) - 
	- **paddings** (const std::vector<int>&) - 
	- **padding_algorithm** (const std::string&) - 
	- **groups** (int) - 
	- **dilations** (const std::vector<int>&) - 
	- **data_format** (const std::string&) - 



返回
:::::::::::::::::::::
Tensor
