.. _en_api_paddle_experimental_psroi_pool:

psroi_pool
-------------------------------

..cpp: function::Tensor psroi_pool ( const Tensor & x , const Tensor & boxes , const paddle::optional<Tensor> & boxes_num , int pooled_height , int pooled_width , int output_channels , float spatial_scale ) ;


Path
:::::::::::::::::::::
paddle\phi\api\include\api.h

Parameters
:::::::::::::::::::::
	- **x** (const Tensor&)
	- **boxes** (const Tensor&)
	- **boxes_num** (const paddle::optional<Tensor>&)
	- **pooled_height** (int)
	- **pooled_width** (int)
	- **output_channels** (int)
	- **spatial_scale** (float)

Returns
:::::::::::::::::::::
Tensor
