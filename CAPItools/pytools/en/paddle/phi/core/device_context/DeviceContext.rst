.. _en_api_DeviceContext:

DeviceContext[source](https://github.com/PaddlePaddle/Paddle/blob/develop/paddle\phi\core\device_context.h)
-------------------------------

.. cpp:class:: DeviceContext ( const DeviceContext & ) ;
 DeviceContext provides device-related interfaces. All kernels must access the interfaces provided by the backend through DeviceContext.


Path
:::::::::::::::::::::
paddle\phi\core\device_context.h

Methods
:::::::::::::::::::::

DeviceContext ( ) ;
'''''''''''
Default construct.



DeviceContext ( const DeviceContext & ) ;
'''''''''''
Copy construct.


**Parameters**
'''''''''''
	- **&** (const DeviceContext)

DeviceContext ( DeviceContext & & ) ;
'''''''''''
Move construct.


**Parameters**
'''''''''''
	- **&** (DeviceContext&)

DeviceContext & operator = ( DeviceContext & & ) ;
'''''''''''
Move assign operator.


**Parameters**
'''''''''''
	- **&** (DeviceContext&)

**Returns**
'''''''''''
DeviceContext &

virtual ~DeviceContext ( ) ;
'''''''''''
Default destruct.



void SetAllocator ( const Allocator * ) ;
'''''''''''
Set the device-related Allocator object. 

**Parameters**
'''''''''''
	- **** (const Allocator*)

void SetHostAllocator ( const Allocator * ) ;
'''''''''''
Set the host Allocator object. 

**Parameters**
'''''''''''
	- **** (const Allocator*)

void SetZeroAllocator ( const Allocator * ) ;
'''''''''''
Set the zero-size Allocator object. 

**Parameters**
'''''''''''
	- **** (const Allocator*)

void SetHostZeroAllocator ( const Allocator * ) ;
'''''''''''
Set the zero-size host Allocator object. 

**Parameters**
'''''''''''
	- **** (const Allocator*)

void SetPinnedAllocator ( const Allocator * ) ;
'''''''''''
Set the zero-size Allocator object. 

**Parameters**
'''''''''''
	- **** (const Allocator*)

const Allocator & GetAllocator ( ) const ;
'''''''''''
Get the const Allocator object. 


**Returns**
'''''''''''
Allocator


const Allocator & GetHostAllocator ( ) const ;
'''''''''''
Get the const device-related Allocator object. 


**Returns**
'''''''''''
Allocator


const Allocator & GetZeroAllocator ( ) const ;
'''''''''''



**Returns**
'''''''''''
const Allocator &

const Allocator & GetHostZeroAllocator ( ) const ;
'''''''''''



**Returns**
'''''''''''
const Allocator &

const Allocator & GetPinnedAllocator ( ) const ;
'''''''''''



**Returns**
'''''''''''
const Allocator &

void SetCUDAGraphAllocator ( const Allocator * ) ;
'''''''''''
Set the CUDA graph Allocator object. 

**Parameters**
'''''''''''
	- **** (const Allocator*)

const Allocator & GetCUDAGraphAllocator ( ) const ;
'''''''''''
Get the const CUDA graph Allocator object. 


**Returns**
'''''''''''
Allocator


bool IsCUDAGraphAllocatorValid ( ) const ;
'''''''''''
Test whether the CUDA graph allocator is valid This method should be called before calling GetCUDAGraphAllocator(). Other unit can calls GetCUDAGraphAllocator() method, only when this method returns True! 


**Returns**
'''''''''''
true if cuda_graph_allocator_ is valid, false otherwise


void * Alloc ( TensorBase * , DataType dtype , size_t requested_size = 0 , bool pinned = false , bool fake_alloc = false ) const ;
'''''''''''
Allocate device memory for tensor.


**Parameters**
'''''''''''
	- **** (TensorBase*)
	- **dtype** (DataType)
	- **requested_size** (size_t)
	- **pinned** (bool)
	- **fake_alloc** (bool)

template<typename T>
T * Alloc ( TensorBase * tensor , size_t requested_size = 0 , bool pinned = false ) const ;
'''''''''''


**Parameters**
'''''''''''
	- **tensor** (TensorBase*)
	- **requested_size** (size_t)
	- **pinned** (bool)

**Returns**
'''''''''''
T *

void * HostAlloc ( TensorBase * tensor , DataType dtype , size_t requested_size = 0 , bool fake_alloc = false ) const ;
'''''''''''
Allocate host memory for tensor.


**Parameters**
'''''''''''
	- **tensor** (TensorBase*)
	- **dtype** (DataType)
	- **requested_size** (size_t)
	- **fake_alloc** (bool)

template<typename T>
T * HostAlloc ( TensorBase * tensor , size_t requested_size = 0 ) const ;
'''''''''''


**Parameters**
'''''''''''
	- **tensor** (TensorBase*)
	- **requested_size** (size_t)

**Returns**
'''''''''''
T *

virtual const Place & GetPlace ( ) const = 0 ;
'''''''''''



**Returns**
'''''''''''
const Place &

virtual void Wait ( ) const {
'''''''''''



void SetGenerator ( Generator * ) ;
'''''''''''
Set the generator for special op. 

**Parameters**
'''''''''''
	- **** (Generator*)

Generator * GetGenerator ( ) const ;
'''''''''''
Get the generator object. 


**Returns**
'''''''''''
Generator


void SetHostGenerator ( Generator * ) ;
'''''''''''
Set the host generator for special op. 

**Parameters**
'''''''''''
	- **** (Generator*)

Generator * GetHostGenerator ( ) const ;
'''''''''''
Get the host generator object. 


**Returns**
'''''''''''
Generator


TypeInfo<DeviceContext> type_info ( ) const {
'''''''''''
Return the type information of the derived class to supportsafely downcast in non-rtti environment. 


**Returns**
'''''''''''
The type information of the derived class.


void SetCommContext ( distributed::CommContext * comm_context ) ;
'''''''''''
Set the comm context point. 

**Parameters**
'''''''''''
	- **comm_context** (distributed::CommContext*)

distributed::CommContext * GetCommContext ( ) const ;
'''''''''''
Get the comm context point. 


**Returns**
'''''''''''
comm context point


