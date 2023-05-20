.. _en_api_paddle_experimental_rmsprop_:

rmsprop_
-------------------------------

..cpp: function::std::tuple<Tensor & , Tensor & , Tensor & , paddle::optional<Tensor> & , paddle::optional<Tensor> &> rmsprop_ ( Tensor & param , Tensor & mean_square , const Tensor & grad , Tensor & moment , const Tensor & learning_rate , paddle::optional<Tensor> & mean_grad , paddle::optional<Tensor> & master_param , float epsilon = 1.0e-10 f , float decay = 0.9 f , float momentum = 0.0 f , bool centered = false , bool multi_precision = false ) ;


Path
:::::::::::::::::::::
paddle\phi\api\include\api.h

Parameters
:::::::::::::::::::::
	- **param** (Tensor&)
	- **mean_square** (Tensor&)
	- **grad** (const Tensor&)
	- **moment** (Tensor&)
	- **learning_rate** (const Tensor&)
	- **mean_grad** (paddle::optional<Tensor>&)
	- **master_param** (paddle::optional<Tensor>&)
	- **epsilon** (float)
	- **decay** (float)
	- **momentum** (float)
	- **centered** (bool)
	- **multi_precision** (bool)

Returns
:::::::::::::::::::::
std::tuple<Tensor , Tensor , Tensor , paddle::optional<Tensor> , paddle::optional<Tensor> >
