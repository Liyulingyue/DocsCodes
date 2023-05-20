.. _en_api_paddle_experimental_layer_norm:

layer_norm
-------------------------------

..cpp: function::std::tuple<Tensor , Tensor , Tensor> layer_norm ( const Tensor & x , const paddle::optional<Tensor> & scale , const paddle::optional<Tensor> & bias , float epsilon , int begin_norm_axis ) ;


Path
:::::::::::::::::::::
paddle\phi\api\include\api.h

Parameters
:::::::::::::::::::::
	- **x** (const Tensor&)
	- **scale** (const paddle::optional<Tensor>&)
	- **bias** (const paddle::optional<Tensor>&)
	- **epsilon** (float)
	- **begin_norm_axis** (int)

Returns
:::::::::::::::::::::
std::tuple<Tensor , Tensor , Tensor>
