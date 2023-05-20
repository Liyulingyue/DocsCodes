.. _en_api_paddle_experimental_send_u_recv:

send_u_recv
-------------------------------

..cpp: function::Tensor send_u_recv ( const Tensor & x , const Tensor & src_index , const Tensor & dst_index , const std::string & reduce_op = "SUM" , const IntArray & out_size = { 0 } ) ;


This API is aligned with Python API, more details are shown in [paddle.send_u_recv](https://www.paddlepaddle.org.cn/documentation/docs/zh/api/paddle/send_u_recv_en.html)

Path
:::::::::::::::::::::
paddle\phi\api\include\api.h

Parameters
:::::::::::::::::::::
	- **x** (const Tensor&)
	- **src_index** (const Tensor&)
	- **dst_index** (const Tensor&)
	- **reduce_op** (const std::string&)
	- **out_size** (const IntArray&)

Returns
:::::::::::::::::::::
Tensor
