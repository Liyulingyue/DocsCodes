.. _en_api_paddle_experimental_roi_pool:

roi_pool
-------------------------------

..cpp: function::Tensor roi_pool ( const Tensor & x , const Tensor & boxes , const paddle::optional<Tensor> & boxes_num , int pooled_height , int pooled_width , float spatial_scale ) ;


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
	- **spatial_scale** (float)

Returns
:::::::::::::::::::::
Tensor
