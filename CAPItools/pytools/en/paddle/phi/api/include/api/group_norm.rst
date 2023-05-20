.. _en_api_paddle_experimental_group_norm:

group_norm
-------------------------------

..cpp: function::Tensor group_norm ( const Tensor & x , const paddle::optional<Tensor> & scale , const paddle::optional<Tensor> & bias , float epsilon , int groups , const std::string & data_layout ) ;


Path
:::::::::::::::::::::
paddle\phi\api\include\api.h

Parameters
:::::::::::::::::::::
	- **x** (const Tensor&)
	- **scale** (const paddle::optional<Tensor>&)
	- **bias** (const paddle::optional<Tensor>&)
	- **epsilon** (float)
	- **groups** (int)
	- **data_layout** (const std::string&)

Returns
:::::::::::::::::::::
Tensor
