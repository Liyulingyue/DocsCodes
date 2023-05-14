.. _cn_api_paddle_experimental_adam_:

adam_
-------------------------------

..cpp: function::std::tuple<Tensor & , Tensor & , Tensor & , Tensor & , Tensor & , paddle::optional<Tensor> &> adam_ ( Tensor & param , const Tensor & grad , const Tensor & learning_rate , Tensor & moment1 , Tensor & moment2 , Tensor & beta1_pow , Tensor & beta2_pow , paddle::optional<Tensor> & master_param , const paddle::optional<Tensor> & skip_update , const Scalar & beta1 = 0.9 f , const Scalar & beta2 = 0.999 f , const Scalar & epsilon = 1.0e-8 f , bool lazy_mode = false , int64_t min_row_size_to_use_multithread = 1000 , bool multi_precision = false , bool use_global_beta_pow = false ) ;

定义目录
:::::::::::::::::::::
paddle\phi\api\include\api.h

参数
:::::::::::::::::::::
	- **param** (Tensor&) - 
	- **grad** (const Tensor&) - 
	- **learning_rate** (const Tensor&) - 
	- **moment1** (Tensor&) - 
	- **moment2** (Tensor&) - 
	- **beta1_pow** (Tensor&) - 
	- **beta2_pow** (Tensor&) - 
	- **master_param** (paddle::optional<Tensor>&) - 
	- **skip_update** (const paddle::optional<Tensor>&) - 
	- **beta1** (const Scalar&) - 
	- **beta2** (const Scalar&) - 
	- **epsilon** (const Scalar&) - 
	- **lazy_mode** (bool) - 
	- **min_row_size_to_use_multithread** (int64_t) - 
	- **multi_precision** (bool) - 
	- **use_global_beta_pow** (bool) - 

返回
:::::::::::::::::::::
std::tuple<Tensor , Tensor , Tensor , Tensor , Tensor , paddle::optional<Tensor> >
