.. _cn_api_paddle_experimental_sgd_:

sgd_
-------------------------------

..cpp: function::std::tuple<Tensor & , paddle::optional<Tensor> &> sgd_ ( Tensor & param , const Tensor & learning_rate , const Tensor & grad , paddle::optional<Tensor> & master_param , bool multi_precision = false ) ;

����Ŀ¼
:::::::::::::::::::::
paddle\phi\api\include\api.h

����
:::::::::::::::::::::
	- **param** (Tensor&) - 
	- **learning_rate** (const Tensor&) - 
	- **grad** (const Tensor&) - 
	- **master_param** (paddle::optional<Tensor>&) - 
	- **multi_precision** (bool) - 

����
:::::::::::::::::::::
std::tuple<Tensor , paddle::optional<Tensor> >
