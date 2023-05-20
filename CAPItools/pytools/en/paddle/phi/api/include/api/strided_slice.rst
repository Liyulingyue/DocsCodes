.. _en_api_paddle_experimental_strided_slice:

strided_slice
-------------------------------

..cpp: function::Tensor strided_slice ( const Tensor & x , const std::vector<int> & axes , const IntArray & starts , const IntArray & ends , const IntArray & strides ) ;


This API is aligned with Python API, more details are shown in [paddle.strided_slice](https://www.paddlepaddle.org.cn/documentation/docs/zh/api/paddle/strided_slice_en.html)

Path
:::::::::::::::::::::
paddle\phi\api\include\api.h

Parameters
:::::::::::::::::::::
	- **x** (const Tensor&)
	- **axes** (const std::vector<int>&)
	- **starts** (const IntArray&)
	- **ends** (const IntArray&)
	- **strides** (const IntArray&)

Returns
:::::::::::::::::::::
Tensor
