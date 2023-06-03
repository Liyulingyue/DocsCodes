.. _en_api_paddle_experimental_dropout:

dropout
-------------------------------

..cpp: function::std::tuple<Tensor , Tensor> dropout ( const Tensor & x , const paddle::optional<Tensor> & seed_tensor , const Scalar & p , bool is_test , const std::string & mode , int seed , bool fix_seed ) ;


Path
:::::::::::::::::::::
paddle\phi\api\include\api.h

Parameters
:::::::::::::::::::::
	- **x** (const Tensor&)
	- **seed_tensor** (const paddle::optional<Tensor>&)
	- **p** (const Scalar&)
	- **is_test** (bool)
	- **mode** (const std::string&)
	- **seed** (int)
	- **fix_seed** (bool)

Returns
:::::::::::::::::::::
std::tuple<Tensor , Tensor>
