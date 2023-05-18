.. _cn_api_paddle_experimental_strided_slice:

strided_slice
-------------------------------

..cpp: function::Tensor strided_slice ( const Tensor & x , const std::vector<int> & axes , const IntArray & starts , const IntArray & ends , const IntArray & strides ) ;

本 API 与 Python API 对齐，详细用法可参考链接：[paddle.strided_slice](https://www.paddlepaddle.org.cn/documentation/docs/zh/api/paddle/strided_slice_cn.html)

定义目录
:::::::::::::::::::::
paddle\phi\api\include\api.h

参数
:::::::::::::::::::::
	- **x** (const Tensor&)
	- **axes** (const std::vector<int>&)
	- **starts** (const IntArray&)
	- **ends** (const IntArray&)
	- **strides** (const IntArray&)

返回
:::::::::::::::::::::
Tensor
