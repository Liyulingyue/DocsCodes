.. _cn_api_paddle_experimental_sparse_conv3d:

conv3d
-------------------------------

..cpp: function::Tensor conv3d ( const Tensor & x , const Tensor & kernel , const std::vector<int> & paddings , const std::vector<int> & dilations , const std::vector<int> & strides , int groups , bool subm , const std::string & key = "" ) ;

定义目录
:::::::::::::::::::::
paddle\phi\api\include\sparse_api.h

参数
:::::::::::::::::::::
	- **x** (const Tensor&)
	- **kernel** (const Tensor&)
	- **paddings** (const std::vector<int>&)
	- **dilations** (const std::vector<int>&)
	- **strides** (const std::vector<int>&)
	- **groups** (int)
	- **subm** (bool)
	- **key** (const std::string&)

返回
:::::::::::::::::::::
Tensor
