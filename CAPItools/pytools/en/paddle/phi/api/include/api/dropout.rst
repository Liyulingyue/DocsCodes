.. _en_api_paddle_experimental_dropout:

dropout
-------------------------------

..cpp: function::std::tuple<Tensor , Tensor> dropout ( const Tensor & x , const paddle::optional<Tensor> & seed_tensor , const Scalar & p , bool is_test , const std::string & mode , int seed , bool fix_seed ) ;


定义目录
:::::::::::::::::::::
paddle\phi\api\include\api.h

参数
:::::::::::::::::::::
	- **x** (const Tensor&)
	- **seed_tensor** (const paddle::optional<Tensor>&)
	- **p** (const Scalar&)
	- **is_test** (bool)
	- **mode** (const std::string&)
	- **seed** (int)
	- **fix_seed** (bool)

返回
:::::::::::::::::::::
std::tuple<Tensor , Tensor>
