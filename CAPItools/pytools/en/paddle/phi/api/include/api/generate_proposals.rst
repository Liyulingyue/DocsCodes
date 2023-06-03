.. _en_api_paddle_experimental_generate_proposals:

generate_proposals
-------------------------------

..cpp: function::std::tuple<Tensor , Tensor , Tensor> generate_proposals ( const Tensor & scores , const Tensor & bbox_deltas , const Tensor & im_shape , const Tensor & anchors , const Tensor & variances , int pre_nms_top_n , int post_nms_top_n , float nms_thresh , float min_size , float eta , bool pixel_offset = true ) ;


Path
:::::::::::::::::::::
paddle\phi\api\include\api.h

Parameters
:::::::::::::::::::::
	- **scores** (const Tensor&)
	- **bbox_deltas** (const Tensor&)
	- **im_shape** (const Tensor&)
	- **anchors** (const Tensor&)
	- **variances** (const Tensor&)
	- **pre_nms_top_n** (int)
	- **post_nms_top_n** (int)
	- **nms_thresh** (float)
	- **min_size** (float)
	- **eta** (float)
	- **pixel_offset** (bool)

Returns
:::::::::::::::::::::
std::tuple<Tensor , Tensor , Tensor>
