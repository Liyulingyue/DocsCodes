.. _cn_api_paddle_experimental_distribute_fpn_proposals:

distribute_fpn_proposals
-------------------------------

.. cpp:function:: std::tuple<std::vector<Tensor> , std::vector<Tensor> , Tensor> distribute_fpn_proposals ( const Tensor & fpn_rois , const paddle::optional<Tensor> & rois_num , int min_level , int max_level , int refer_level , int refer_scale , bool pixel_offset ) ;

<--! name="desc" -->

<--! /name -->

定义目录
:::::::::::::::::::::
paddle\phi\api\include\api.h

参数
:::::::::::::::::::::
	- **fpn_rois** (const Tensor&) - 
	- **rois_num** (const paddle::optional<Tensor>&) - 
	- **min_level** (int) - 
	- **max_level** (int) - 
	- **refer_level** (int) - 
	- **refer_scale** (int) - 
	- **pixel_offset** (bool) - 


返回
:::::::::::::::::::::
std::tuple<std::vector<Tensor> , std::vector<Tensor> , Tensor>

<name="reference_link">

</name>

