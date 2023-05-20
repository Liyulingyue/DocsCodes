.. _en_api_paddle_experimental_fused_dropout_add:

fused_dropout_add
-------------------------------

..cpp: function::std::tuple<Tensor , Tensor> fused_dropout_add ( const Tensor & x , const Tensor & y , const paddle::optional<Tensor> & seed_tensor , const Scalar & p , bool is_test , const std::string & mode , int seed = 0 , bool fix_seed = false ) ;


定义目录
:::::::::::::::::::::
paddle\phi\api\include\fused_api.h

参数
:::::::::::::::::::::
	- **x** (const Tensor&)
	- **y** (const Tensor&)
	- **seed_tensor** (const paddle::optional<Tensor>&)
	- **p** (const Scalar&)
	- **is_test** (bool)
	- **mode** (const std::string&)
	- **seed** (int)
	- **fix_seed** (bool)

返回
:::::::::::::::::::::
std::tuple<Tensor , Tensor>
