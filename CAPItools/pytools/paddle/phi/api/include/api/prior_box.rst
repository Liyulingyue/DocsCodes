.. _cn_api_paddle_experimental_prior_box:
    
prior_box
-------------------------------

.. cpp:function:: std::tuple<Tensor , Tensor> prior_box ( const Tensor & input , const Tensor & image , const std::vector<float> & min_sizes , const std::vector<float> & max_sizes = { } , const std::vector<float> & aspect_ratios = { } , const std::vector<float> & variances = { } , bool flip = true , bool clip = true , float step_w = 0.0 , float step_h = 0.0 , float offset = 0.5 , bool min_max_aspect_ratios_order = false ) ;

<--! name="desc" -->

<--! /name -->

定义目录
:::::::::::::::::::::
paddle\phi\api\include\api.h

参数
:::::::::::::::::::::
	- **input** (const Tensor&) - 
	- **image** (const Tensor&) - 
	- **min_sizes** (const std::vector<float>&) - 
	- **max_sizes** (const std::vector<float>&) - 
	- **aspect_ratios** (const std::vector<float>&) - 
	- **variances** (const std::vector<float>&) - 
	- **flip** (bool) - 
	- **clip** (bool) - 
	- **step_w** (float) - 
	- **step_h** (float) - 
	- **offset** (float) - 
	- **min_max_aspect_ratios_order** (bool) - 


返回
:::::::::::::::::::::
std::tuple<Tensor , Tensor>

<name="reference_link">

</name>

