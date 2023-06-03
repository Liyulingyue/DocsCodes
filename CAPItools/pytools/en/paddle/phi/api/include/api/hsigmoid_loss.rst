.. _en_api_paddle_experimental_hsigmoid_loss:

hsigmoid_loss
-------------------------------

..cpp: function::std::tuple<Tensor , Tensor , Tensor> hsigmoid_loss ( const Tensor & x , const Tensor & label , const Tensor & w , const paddle::optional<Tensor> & bias , const paddle::optional<Tensor> & path , const paddle::optional<Tensor> & code , int num_classes , bool is_sparse ) ;


Path
:::::::::::::::::::::
paddle\phi\api\include\api.h

Parameters
:::::::::::::::::::::
	- **x** (const Tensor&)
	- **label** (const Tensor&)
	- **w** (const Tensor&)
	- **bias** (const paddle::optional<Tensor>&)
	- **path** (const paddle::optional<Tensor>&)
	- **code** (const paddle::optional<Tensor>&)
	- **num_classes** (int)
	- **is_sparse** (bool)

Returns
:::::::::::::::::::::
std::tuple<Tensor , Tensor , Tensor>
