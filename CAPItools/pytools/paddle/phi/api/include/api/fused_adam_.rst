.. _cn_api_paddle_experimental_fused_adam_:
    
fused_adam_
-------------------------------

.. cpp:function:: std::tuple<std::vector<Tensor> & , std::vector<Tensor> & , std::vector<Tensor> & , std::vector<Tensor> & , std::vector<Tensor> & , paddle::optional<std::vector<Tensor> > &> fused_adam_ ( std::vector<Tensor> & params , const std::vector<Tensor> & grads , const Tensor & learning_rate , std::vector<Tensor> & moments1 , std::vector<Tensor> & moments2 , std::vector<Tensor> & beta1_pows , std::vector<Tensor> & beta2_pows , paddle::optional<std::vector<Tensor> > & master_params , const paddle::optional<Tensor> & skip_update , const Scalar & beta1 , const Scalar & beta2 , const Scalar & epsilon , int chunk_size , float weight_decay , bool use_adamw , bool multi_precision , bool use_global_beta_pow ) ;

<--! name="desc" -->

<--! /name -->

定义目录
:::::::::::::::::::::
paddle\phi\api\include\api.h

参数
:::::::::::::::::::::
	- **params** (std::vector<Tensor>&) - 
	- **grads** (const std::vector<Tensor>&) - 
	- **learning_rate** (const Tensor&) - 
	- **moments1** (std::vector<Tensor>&) - 
	- **moments2** (std::vector<Tensor>&) - 
	- **beta1_pows** (std::vector<Tensor>&) - 
	- **beta2_pows** (std::vector<Tensor>&) - 
	- **master_params** (paddle::optional<std::vector<Tensor> >&) - 
	- **skip_update** (const paddle::optional<Tensor>&) - 
	- **beta1** (const Scalar&) - 
	- **beta2** (const Scalar&) - 
	- **epsilon** (const Scalar&) - 
	- **chunk_size** (int) - 
	- **weight_decay** (float) - 
	- **use_adamw** (bool) - 
	- **multi_precision** (bool) - 
	- **use_global_beta_pow** (bool) - 


返回
:::::::::::::::::::::
std::tuple<std::vector<Tensor> , std::vector<Tensor> , std::vector<Tensor> , std::vector<Tensor> , std::vector<Tensor> , paddle::optional<std::vector<Tensor> > >

<name="reference_link">

</name>

