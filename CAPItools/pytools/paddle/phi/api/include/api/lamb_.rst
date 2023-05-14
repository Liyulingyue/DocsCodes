.. _cn_api_paddle_experimental_lamb_:

lamb_
-------------------------------

..cpp: function::std::tuple<Tensor & , Tensor & , Tensor & , Tensor & , Tensor & , paddle::optional<Tensor> &> lamb_ ( Tensor & param , const Tensor & grad , const Tensor & learning_rate , Tensor & moment1 , Tensor & moment2 , Tensor & beta1_pow , Tensor & beta2_pow , paddle::optional<Tensor> & master_param , const paddle::optional<Tensor> & skip_update , float weight_decay , float beta1 = 0.9 , float beta2 = 0.999 , float epsilon = 1.0e-6 f , bool multi_precision = false ) ;

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
	- **weight_decay** (float) - 
	- **beta1** (float) - 
	- **beta2** (float) - 
	- **epsilon** (float) - 
	- **multi_precision** (bool) - 

返回
:::::::::::::::::::::
std::tuple<Tensor , Tensor , Tensor , Tensor , Tensor , paddle::optional<Tensor> >
