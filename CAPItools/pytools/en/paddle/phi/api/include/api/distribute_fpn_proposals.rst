.. _en_api_paddle_experimental_distribute_fpn_proposals:

distribute_fpn_proposals
-------------------------------

..cpp: function::std::tuple<std::vector<Tensor> , std::vector<Tensor> , Tensor> distribute_fpn_proposals ( const Tensor & fpn_rois , const paddle::optional<Tensor> & rois_num , int min_level , int max_level , int refer_level , int refer_scale , bool pixel_offset ) ;


Path
:::::::::::::::::::::
paddle\phi\api\include\api.h

Parameters
:::::::::::::::::::::
	- **fpn_rois** (const Tensor&)
	- **rois_num** (const paddle::optional<Tensor>&)
	- **min_level** (int)
	- **max_level** (int)
	- **refer_level** (int)
	- **refer_scale** (int)
	- **pixel_offset** (bool)

Returns
:::::::::::::::::::::
std::tuple<std::vector<Tensor> , std::vector<Tensor> , Tensor>
