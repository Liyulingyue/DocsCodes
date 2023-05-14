.. _cn_api_paddle_experimental_send_u_recv:

send_u_recv
-------------------------------

..cpp: function::Tensor send_u_recv ( const Tensor & x , const Tensor & src_index , const Tensor & dst_index , const std::string & reduce_op = "SUM" , const IntArray & out_size = { 0 } ) ;

定义目录
:::::::::::::::::::::
paddle\phi\api\include\api.h

参数
:::::::::::::::::::::
	- **x** (const Tensor&) - 
	- **src_index** (const Tensor&) - 
	- **dst_index** (const Tensor&) - 
	- **reduce_op** (const std::string&) - 
	- **out_size** (const IntArray&) - 

返回
:::::::::::::::::::::
Tensor
