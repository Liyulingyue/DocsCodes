.. _en_api_paddle_experimental_adadelta_:

adadelta_
-------------------------------

..cpp: function::std::tuple<Tensor & , Tensor & , Tensor & , paddle::optional<Tensor> &> adadelta_ ( Tensor & param , const Tensor & grad , Tensor & avg_squared_grad , Tensor & avg_squared_update , const Tensor & learning_rate , paddle::optional<Tensor> & master_param , float rho , float epsilon , bool multi_precision ) ;


Path
:::::::::::::::::::::
paddle\phi\api\include\api.h

Parameters
:::::::::::::::::::::
	- **param** (Tensor&)
	- **grad** (const Tensor&)
	- **avg_squared_grad** (Tensor&)
	- **avg_squared_update** (Tensor&)
	- **learning_rate** (const Tensor&)
	- **master_param** (paddle::optional<Tensor>&)
	- **rho** (float)
	- **epsilon** (float)
	- **multi_precision** (bool)

Returns
:::::::::::::::::::::
std::tuple<Tensor , Tensor , Tensor , paddle::optional<Tensor> >
