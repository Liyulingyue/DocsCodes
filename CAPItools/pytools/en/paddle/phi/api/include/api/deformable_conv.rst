.. _en_api_paddle_experimental_deformable_conv:

deformable_conv
-------------------------------

..cpp: function::Tensor deformable_conv ( const Tensor & x , const Tensor & offset , const Tensor & filter , const paddle::optional<Tensor> & mask , const std::vector<int> & strides , const std::vector<int> & paddings , const std::vector<int> & dilations , int deformable_groups , int groups , int im2col_step ) ;


Path
:::::::::::::::::::::
paddle\phi\api\include\api.h

Parameters
:::::::::::::::::::::
	- **x** (const Tensor&)
	- **offset** (const Tensor&)
	- **filter** (const Tensor&)
	- **mask** (const paddle::optional<Tensor>&)
	- **strides** (const std::vector<int>&)
	- **paddings** (const std::vector<int>&)
	- **dilations** (const std::vector<int>&)
	- **deformable_groups** (int)
	- **groups** (int)
	- **im2col_step** (int)

Returns
:::::::::::::::::::::
Tensor
