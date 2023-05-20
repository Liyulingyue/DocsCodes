.. _en_api_paddle_experimental_fused_linear_param_grad_add:

fused_linear_param_grad_add
-------------------------------

..cpp: function::std::tuple<Tensor , Tensor> fused_linear_param_grad_add ( const Tensor & x , const Tensor & dout , const paddle::optional<Tensor> & dweight , const paddle::optional<Tensor> & dbias , bool multi_precision = true ) ;


Path
:::::::::::::::::::::
paddle\phi\api\include\fused_api.h

Parameters
:::::::::::::::::::::
	- **x** (const Tensor&)
	- **dout** (const Tensor&)
	- **dweight** (const paddle::optional<Tensor>&)
	- **dbias** (const paddle::optional<Tensor>&)
	- **multi_precision** (bool)

Returns
:::::::::::::::::::::
std::tuple<Tensor , Tensor>
