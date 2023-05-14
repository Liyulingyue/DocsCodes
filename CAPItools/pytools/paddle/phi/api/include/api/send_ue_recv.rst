.. _cn_api_paddle_experimental_send_ue_recv:

send_ue_recv
-------------------------------

..cpp: function::Tensor send_ue_recv ( const Tensor & x , const Tensor & y , const Tensor & src_index , const Tensor & dst_index , const std::string & message_op = "ADD" , const std::string & reduce_op = "SUM" , const IntArray & out_size = { 0 } ) ;

定义目录
:::::::::::::::::::::
paddle\phi\api\include\api.h

参数
:::::::::::::::::::::
	- **x** (const Tensor&) - 
	- **y** (const Tensor&) - 
	- **src_index** (const Tensor&) - 
	- **dst_index** (const Tensor&) - 
	- **message_op** (const std::string&) - 
	- **reduce_op** (const std::string&) - 
	- **out_size** (const IntArray&) - 

返回
:::::::::::::::::::::
Tensor
