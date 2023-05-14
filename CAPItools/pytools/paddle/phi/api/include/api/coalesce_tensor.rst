.. _cn_api_paddle_experimental_coalesce_tensor:

coalesce_tensor
-------------------------------

.. cpp:function:: std::tuple<std::vector<Tensor> , Tensor> coalesce_tensor ( const std::vector<Tensor> & input , DataType dtype , bool copy_data = false , bool set_constant = false , bool persist_output = false , float constant = 0.0 , bool use_align = true , int align_size = - 1 , int size_of_dtype = - 1 , const std::vector<int64_t> & concated_shapes = { } , const std::vector<int64_t> & concated_ranks = { } ) ;

<name="desc">

</name>

定义目录
:::::::::::::::::::::
paddle\phi\api\include\api.h

参数
:::::::::::::::::::::
	- **input** (const std::vector<Tensor>&) - 
	- **dtype** (DataType) - 
	- **copy_data** (bool) - 
	- **set_constant** (bool) - 
	- **persist_output** (bool) - 
	- **constant** (float) - 
	- **use_align** (bool) - 
	- **align_size** (int) - 
	- **size_of_dtype** (int) - 
	- **concated_shapes** (const std::vector<int64_t>&) - 
	- **concated_ranks** (const std::vector<int64_t>&) - 


返回
:::::::::::::::::::::
std::tuple<std::vector<Tensor> , Tensor>

<name="reference_link">

</name>

