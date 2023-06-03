.. _en_api_paddle_experimental_sgd_:

sgd_
-------------------------------

..cpp: function::std::tuple<Tensor & , paddle::optional<Tensor> &> sgd_ ( Tensor & param , const Tensor & learning_rate , const Tensor & grad , paddle::optional<Tensor> & master_param , bool multi_precision = false ) ;


Path
:::::::::::::::::::::
paddle\phi\api\include\api.h

Parameters
:::::::::::::::::::::
	- **param** (Tensor&)
	- **learning_rate** (const Tensor&)
	- **grad** (const Tensor&)
	- **master_param** (paddle::optional<Tensor>&)
	- **multi_precision** (bool)

Returns
:::::::::::::::::::::
std::tuple<Tensor , paddle::optional<Tensor> >
