.. _cn_api_paddle_experimental_matrix_nms:

matrix_nms
-------------------------------

.. cpp:function:: std::tuple<Tensor , Tensor , Tensor> matrix_nms ( const Tensor & bboxes , const Tensor & scores , float score_threshold , int nms_top_k , int keep_top_k , float post_threshold = 0 . , bool use_gaussian = false , float gaussian_sigma = 2 . , int background_label = 0 , bool normalized = true ) ;

<name="desc">

</name>

定义目录
:::::::::::::::::::::
paddle\phi\api\include\api.h

参数
:::::::::::::::::::::
	- **bboxes** (const Tensor&) - 
	- **scores** (const Tensor&) - 
	- **score_threshold** (float) - 
	- **nms_top_k** (int) - 
	- **keep_top_k** (int) - 
	- **post_threshold** (float) - 
	- **use_gaussian** (bool) - 
	- **gaussian_sigma** (float) - 
	- **background_label** (int) - 
	- **normalized** (bool) - 


返回
:::::::::::::::::::::
std::tuple<Tensor , Tensor , Tensor>

<name="reference_link">

</name>

