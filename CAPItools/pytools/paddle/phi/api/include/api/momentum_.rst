.. _cn_api_paddle_experimental_momentum_:

momentum_
-------------------------------

.. cpp:function:: std::tuple<Tensor & , Tensor & , paddle::optional<Tensor> &> momentum_ ( Tensor & param , const Tensor & grad , Tensor & velocity , const Tensor & learning_rate , paddle::optional<Tensor> & master_param , float mu , bool use_nesterov = false , const std::string & regularization_method = "" , float regularization_coeff = 0.0 f , bool multi_precision = false , float rescale_grad = 1.0 f ) ;

<name="desc">

</name>

定义目录
:::::::::::::::::::::
paddle\phi\api\include\api.h

参数
:::::::::::::::::::::
	- **param** (Tensor&) - 
	- **grad** (const Tensor&) - 
	- **velocity** (Tensor&) - 
	- **learning_rate** (const Tensor&) - 
	- **master_param** (paddle::optional<Tensor>&) - 
	- **mu** (float) - 
	- **use_nesterov** (bool) - 
	- **regularization_method** (const std::string&) - 
	- **regularization_coeff** (float) - 
	- **multi_precision** (bool) - 
	- **rescale_grad** (float) - 


返回
:::::::::::::::::::::
std::tuple<Tensor , Tensor , paddle::optional<Tensor> >

<name="reference_link">

</name>

