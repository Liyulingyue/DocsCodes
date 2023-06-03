.. _en_api_paddle_GetCurrentCUDAStream:

GetCurrentCUDAStream
-------------------------------

..cpp: function::phi::CUDAStream * GetCurrentCUDAStream ( const phi::Place & place ) ;
 Get the current CUDA stream for the passed CUDA device.


Path
:::::::::::::::::::::
paddle\phi\api\include\context_pool.h

Parameters
:::::::::::::::::::::
	- **place** (const phi::Place&)

Returns
:::::::::::::::::::::
phi::CUDAStream
