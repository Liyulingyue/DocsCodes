.. _cn_api_paddle_experimental_merged_adam_:

merged_adam_
-------------------------------

..cpp: function::std::tuple<std::vector<Tensor> & , std::vector<Tensor> & , std::vector<Tensor> & , std::vector<Tensor> & , std::vector<Tensor> & , paddle::optional<std::vector<Tensor> > &> merged_adam_ ( std::vector<Tensor> & param , const std::vector<Tensor> & grad , const std::vector<Tensor> & learning_rate , std::vector<Tensor> & moment1 , std::vector<Tensor> & moment2 , std::vector<Tensor> & beta1_pow , std::vector<Tensor> & beta2_pow , paddle::optional<std::vector<Tensor> > & master_param , const Scalar & beta1 = 0.9 f , const Scalar & beta2 = 0.999 f , const Scalar & epsilon = 1.0e-8 f , bool multi_precision = false , bool use_global_beta_pow = false ) ;

定义目录
:::::::::::::::::::::
paddle\phi\api\include\api.h

参数
:::::::::::::::::::::
	- **param** (std::vector<Tensor>&) - 
	- **grad** (const std::vector<Tensor>&) - 
	- **learning_rate** (const std::vector<Tensor>&) - 
	- **moment1** (std::vector<Tensor>&) - 
	- **moment2** (std::vector<Tensor>&) - 
	- **beta1_pow** (std::vector<Tensor>&) - 
	- **beta2_pow** (std::vector<Tensor>&) - 
	- **master_param** (paddle::optional<std::vector<Tensor> >&) - 
	- **beta1** (const Scalar&) - 
	- **beta2** (const Scalar&) - 
	- **epsilon** (const Scalar&) - 
	- **multi_precision** (bool) - 
	- **use_global_beta_pow** (bool) - 

返回
:::::::::::::::::::::
std::tuple<std::vector<Tensor> , std::vector<Tensor> , std::vector<Tensor> , std::vector<Tensor> , std::vector<Tensor> , paddle::optional<std::vector<Tensor> > >
