.. _cn_api_paddle_experimental_yolo_box:

yolo_box
-------------------------------

..cpp: function::std::tuple<Tensor , Tensor> yolo_box ( const Tensor & x , const Tensor & img_size , const std::vector<int> & anchors = { } , int class_num = 1 , float conf_thresh = 0.01 , int downsample_ratio = 32 , bool clip_bbox = true , float scale_x_y = 1.0 , bool iou_aware = false , float iou_aware_factor = 0.5 ) ;

定义目录
:::::::::::::::::::::
paddle\phi\api\include\api.h

参数
:::::::::::::::::::::
	- **x** (const Tensor&) - 
	- **img_size** (const Tensor&) - 
	- **anchors** (const std::vector<int>&) - 
	- **class_num** (int) - 
	- **conf_thresh** (float) - 
	- **downsample_ratio** (int) - 
	- **clip_bbox** (bool) - 
	- **scale_x_y** (float) - 
	- **iou_aware** (bool) - 
	- **iou_aware_factor** (float) - 

返回
:::::::::::::::::::::
std::tuple<Tensor , Tensor>
