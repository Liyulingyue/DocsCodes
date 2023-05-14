.. _cn_api_paddle_experimental_auc:

auc
-------------------------------

.. cpp:function:: std::tuple<Tensor , Tensor , Tensor> auc ( const Tensor & x , const Tensor & label , const Tensor & stat_pos , const Tensor & stat_neg , const paddle::optional<Tensor> & ins_tag_weight , const std::string & curve = "ROC" , int num_thresholds = ( 2 << 12 ) - 1 , int slide_steps = 1 ) ;

<--! name="desc" -->

<--! /name -->

定义目录
:::::::::::::::::::::
paddle\phi\api\include\api.h

参数
:::::::::::::::::::::
	- **x** (const Tensor&) - 
	- **label** (const Tensor&) - 
	- **stat_pos** (const Tensor&) - 
	- **stat_neg** (const Tensor&) - 
	- **ins_tag_weight** (const paddle::optional<Tensor>&) - 
	- **curve** (const std::string&) - 
	- **num_thresholds** (int) - 
	- **slide_steps** (int) - 


返回
:::::::::::::::::::::
std::tuple<Tensor , Tensor , Tensor>

<name="reference_link">

</name>

