.. _cn_api_paddle_experimental_sgd_:

sgd_
-------------------------------

..cpp: function::std::tuple<Tensor & , paddle::optional<Tensor> &> sgd_ ( Tensor & param , const Tensor & learning_rate , const Tensor & grad , paddle::optional<Tensor> & master_param , bool multi_precision = false ) ;

定义目录
:::::::::::::::::::::
paddle\phi\api\include\api.h

参数
:::::::::::::::::::::
	- **param** (Tensor&) - 
	- **learning_rate** (const Tensor&) - 
	- **grad** (const Tensor&) - 
	- **master_param** (paddle::optional<Tensor>&) - 
	- **multi_precision** (bool) - 



返回
:::::::::::::::::::::
std::tuple<Tensor , paddle::optional<Tensor> >
