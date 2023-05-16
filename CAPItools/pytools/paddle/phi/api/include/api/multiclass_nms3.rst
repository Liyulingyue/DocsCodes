.. _cn_api_paddle_experimental_multiclass_nms3:

multiclass_nms3
-------------------------------

..cpp: function::std::tuple<Tensor , Tensor , Tensor> multiclass_nms3 ( const Tensor & bboxes , const Tensor & scores , const paddle::optional<Tensor> & rois_num , float score_threshold , int nms_top_k , int keep_top_k , float nms_threshold = 0.3 , bool normalized = true , float nms_eta = 1.0 , int background_label = 0 ) ;

定义目录
:::::::::::::::::::::
paddle\phi\api\include\api.h

参数
:::::::::::::::::::::
	- **bboxes** (const Tensor&)
	- **scores** (const Tensor&)
	- **rois_num** (const paddle::optional<Tensor>&)
	- **score_threshold** (float)
	- **nms_top_k** (int)
	- **keep_top_k** (int)
	- **nms_threshold** (float)
	- **normalized** (bool)
	- **nms_eta** (float)
	- **background_label** (int)

返回
:::::::::::::::::::::
std::tuple<Tensor , Tensor , Tensor>
