.. _cn_api_paddle_GetCurrentCUDAStream:

GetCurrentCUDAStream
-------------------------------

..cpp: function::phi::CUDAStream * GetCurrentCUDAStream ( const phi::Place & place ) ;
 Get the current CUDA stream for the passed CUDA device.


定义目录
:::::::::::::::::::::
paddle\phi\api\include\context_pool.h

参数
:::::::::::::::::::::
	- **place** (const phi::Place&)

返回
:::::::::::::::::::::
phi::CUDAStream
