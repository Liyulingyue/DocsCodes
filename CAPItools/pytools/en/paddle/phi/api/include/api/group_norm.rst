.. _en_api_paddle_experimental_group_norm:

group_norm
-------------------------------

..cpp: function::Tensor group_norm ( const Tensor & x , const paddle::optional<Tensor> & scale , const paddle::optional<Tensor> & bias , float epsilon = 1e - 5 , int groups = - 1 , const std::string & data_layout = "NCHW" ) ;


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
