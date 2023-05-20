.. _en_api_paddle_experimental_adamax_:

adamax_
-------------------------------

..cpp: function::std::tuple<Tensor & , Tensor & , Tensor & , paddle::optional<Tensor> &> adamax_ ( Tensor & param , const Tensor & grad , const Tensor & learning_rate , Tensor & moment , Tensor & inf_norm , const Tensor & beta1_pow , paddle::optional<Tensor> & master_param , float beta1 = 0.9 f , float beta2 = 0.999 f , float epsilon = 1.0e-8 f , bool multi_precision = false ) ;


Path
:::::::::::::::::::::
paddle\phi\api\include\api.h

Parameters
:::::::::::::::::::::
	- **param** (Tensor&)
	- **grad** (const Tensor&)
	- **learning_rate** (const Tensor&)
	- **moment** (Tensor&)
	- **inf_norm** (Tensor&)
	- **beta1_pow** (const Tensor&)
	- **master_param** (paddle::optional<Tensor>&)
	- **beta1** (float)
	- **beta2** (float)
	- **epsilon** (float)
	- **multi_precision** (bool)

Returns
:::::::::::::::::::::
std::tuple<Tensor , Tensor , Tensor , paddle::optional<Tensor> >
