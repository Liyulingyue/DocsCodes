.. _en_api_paddle_experimental_send_uv:

send_uv
-------------------------------

..cpp: function::Tensor send_uv ( const Tensor & x , const Tensor & y , const Tensor & src_index , const Tensor & dst_index , const std::string & message_op = "ADD" ) ;


This API is aligned with Python API, more details are shown in [paddle.send_uv](https://www.paddlepaddle.org.cn/documentation/docs/zh/api/paddle/send_uv_en.html)

Path
:::::::::::::::::::::
paddle\phi\api\include\api.h

Parameters
:::::::::::::::::::::
	- **x** (const Tensor&)
	- **y** (const Tensor&)
	- **src_index** (const Tensor&)
	- **dst_index** (const Tensor&)
	- **message_op** (const std::string&)

Returns
:::::::::::::::::::::
Tensor
