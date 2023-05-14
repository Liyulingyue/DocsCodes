.. _cn_api_paddle_experimental_merged_momentum_:

merged_momentum_
-------------------------------

..cpp: function::std::tuple<std::vector<Tensor> & , std::vector<Tensor> & , paddle::optional<std::vector<Tensor> > &> merged_momentum_ ( std::vector<Tensor> & param , const std::vector<Tensor> & grad , std::vector<Tensor> & velocity , const std::vector<Tensor> & learning_rate , paddle::optional<std::vector<Tensor> > & master_param , float mu , bool use_nesterov = false , const std::vector<std::string> & regularization_method = { } , const std::vector<float> & regularization_coeff = { } , bool multi_precision = false , float rescale_grad = 1.0 f ) ;

定义目录
:::::::::::::::::::::
paddle\phi\api\include\api.h

参数
:::::::::::::::::::::
	- **param** (std::vector<Tensor>&) - 
	- **grad** (const std::vector<Tensor>&) - 
	- **velocity** (std::vector<Tensor>&) - 
	- **learning_rate** (const std::vector<Tensor>&) - 
	- **master_param** (paddle::optional<std::vector<Tensor> >&) - 
	- **mu** (float) - 
	- **use_nesterov** (bool) - 
	- **regularization_method** (const std::vector<std::string>&) - 
	- **regularization_coeff** (const std::vector<float>&) - 
	- **multi_precision** (bool) - 
	- **rescale_grad** (float) - 

返回
:::::::::::::::::::::
std::tuple<std::vector<Tensor> , std::vector<Tensor> , paddle::optional<std::vector<Tensor> > >
