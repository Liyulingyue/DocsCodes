.. _en_api_paddle_experimental_hsigmoid_loss:

hsigmoid_loss
-------------------------------

..cpp: function::std::tuple<Tensor , Tensor , Tensor> hsigmoid_loss ( const Tensor & x , const Tensor & label , const Tensor & w , const paddle::optional<Tensor> & bias , const paddle::optional<Tensor> & path , const paddle::optional<Tensor> & code , int num_classes , bool is_sparse ) ;


定义目录
:::::::::::::::::::::
paddle\phi\api\include\api.h

参数
:::::::::::::::::::::
	- **x** (const Tensor&)
	- **label** (const Tensor&)
	- **w** (const Tensor&)
	- **bias** (const paddle::optional<Tensor>&)
	- **path** (const paddle::optional<Tensor>&)
	- **code** (const paddle::optional<Tensor>&)
	- **num_classes** (int)
	- **is_sparse** (bool)

返回
:::::::::::::::::::::
std::tuple<Tensor , Tensor , Tensor>
