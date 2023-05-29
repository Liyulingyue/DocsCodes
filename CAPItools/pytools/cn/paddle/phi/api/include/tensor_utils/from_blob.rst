.. _cn_api_paddle_from_blob:

from_blob
-------------------------------

..cpp: function::Tensor from_blob ( void * data , const phi::IntArray & shape , phi::DataType dtype , phi::DataLayout layout = phi::DataLayout::NCHW , const phi::Place & place = phi::Place ( ) , const Deleter & deleter = nullptr ) ;
Construct a Tensor from a buffer pointed to by `data` 

..note::
	`from_blob` doesn’t copy or move data, Modifying the constructed tensor is equivalent to modifying the original data. 

定义目录
:::::::::::::::::::::
paddle\phi\api\include\tensor_utils.h

参数
:::::::::::::::::::::
	- **data** (void*) - The pointer to the memory buffer. 
	- **shape** (const phi::IntArray&) - The dims of the tensor. 
	- **dtype** (phi::DataType) - The data type of the tensor, should correspond to data type of`data`. See PD_FOR_EACH_DATA_TYPE in `phi/common/data_type.h` 
	- **layout** (phi::DataLayout) - The data layout of the tensor. 
	- **place** (const phi::Place&) - The place where the tensor is located.If `place` is default value, it will be inferred from `data`,However, the feature is only supported on CPU or GPU.If `place` is not default value, make sure that `place` is equalto the place of `data` 
	- **deleter** (const function<void ( void )>&) - A function or function object that will be called to free thememory buffer. 

返回
:::::::::::::::::::::
A Tensor object constructed from the buffer

