.. _cn_api_paddle_experimental_average_accumulates_:

average_accumulates_
-------------------------------

.. cpp:function:: std::tuple<Tensor & , Tensor & , Tensor & , Tensor & , Tensor & , Tensor &> average_accumulates_ ( const Tensor & param , Tensor & in_sum_1 , Tensor & in_sum_2 , Tensor & in_sum_3 , Tensor & in_num_accumulates , Tensor & in_old_num_accumulates , Tensor & in_num_updates , float average_window = 0 , int64_t max_average_window = INT64_MAX , int64_t min_average_window = 10000 L ) ;

<--! name="desc" -->

<--! /name -->

定义目录
:::::::::::::::::::::
paddle\phi\api\include\api.h

参数
:::::::::::::::::::::
	- **param** (const Tensor&) - 
	- **in_sum_1** (Tensor&) - 
	- **in_sum_2** (Tensor&) - 
	- **in_sum_3** (Tensor&) - 
	- **in_num_accumulates** (Tensor&) - 
	- **in_old_num_accumulates** (Tensor&) - 
	- **in_num_updates** (Tensor&) - 
	- **average_window** (float) - 
	- **max_average_window** (int64_t) - 
	- **min_average_window** (int64_t) - 


返回
:::::::::::::::::::::
std::tuple<Tensor , Tensor , Tensor , Tensor , Tensor , Tensor >

<name="reference_link">

</name>

