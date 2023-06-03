.. _en_api_paddle_experimental_fused_dropout_add:

fused_dropout_add
-------------------------------

..cpp: function::std::tuple<Tensor , Tensor> fused_dropout_add ( const Tensor & x , const Tensor & y , const paddle::optional<Tensor> & seed_tensor , const Scalar & p , bool is_test , const std::string & mode , int seed = 0 , bool fix_seed = false ) ;


Path
:::::::::::::::::::::
paddle\phi\api\include\fused_api.h

Parameters
:::::::::::::::::::::
	- **x** (const Tensor&)
	- **y** (const Tensor&)
	- **seed_tensor** (const paddle::optional<Tensor>&)
	- **p** (const Scalar&)
	- **is_test** (bool)
	- **mode** (const std::string&)
	- **seed** (int)
	- **fix_seed** (bool)

Returns
:::::::::::::::::::::
std::tuple<Tensor , Tensor>
