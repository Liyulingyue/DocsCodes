.. _en_api_paddle_experimental_yolo_loss:

yolo_loss
-------------------------------

..cpp: function::std::tuple<Tensor , Tensor , Tensor> yolo_loss ( const Tensor & x , const Tensor & gt_box , const Tensor & gt_label , const paddle::optional<Tensor> & gt_score , const std::vector<int> & anchors , const std::vector<int> & anchor_mask , int class_num , float ignore_thresh , int downsample_ratio , bool use_label_smooth = true , float scale_x_y = 1.0 ) ;


Path
:::::::::::::::::::::
paddle\phi\api\include\api.h

Parameters
:::::::::::::::::::::
	- **x** (const Tensor&)
	- **gt_box** (const Tensor&)
	- **gt_label** (const Tensor&)
	- **gt_score** (const paddle::optional<Tensor>&)
	- **anchors** (const std::vector<int>&)
	- **anchor_mask** (const std::vector<int>&)
	- **class_num** (int)
	- **ignore_thresh** (float)
	- **downsample_ratio** (int)
	- **use_label_smooth** (bool)
	- **scale_x_y** (float)

Returns
:::::::::::::::::::::
std::tuple<Tensor , Tensor , Tensor>
