.. _en_api_paddle_experimental_adagrad_:

adagrad_
-------------------------------

..cpp: function::std::tuple<Tensor & , Tensor & , paddle::optional<Tensor> &> adagrad_ ( Tensor & param , const Tensor & grad , Tensor & moment , const Tensor & learning_rate , paddle::optional<Tensor> & master_param , float epsilon = 1.0e-6 f , bool multi_precision = false ) ;


Path
:::::::::::::::::::::
paddle\phi\api\include\api.h

Parameters
:::::::::::::::::::::
	- **param** (Tensor&)
	- **grad** (const Tensor&)
	- **moment** (Tensor&)
	- **learning_rate** (const Tensor&)
	- **master_param** (paddle::optional<Tensor>&)
	- **epsilon** (float)
	- **multi_precision** (bool)

Returns
:::::::::::::::::::::
std::tuple<Tensor , Tensor , paddle::optional<Tensor> >
