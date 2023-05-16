.. _cn_api_DeviceContext:

DeviceContext[源代码](https://github.com/PaddlePaddle/Paddle/blob/develop/paddle\phi\core\device_context.h)
-------------------------------

.. cpp:class:: DeviceContext ( const DeviceContext & ) ;
 DeviceContext provides device-related interfaces. All kernels must access the interfaces provided by the backend through DeviceContext.


定义目录
:::::::::::::::::::::
paddle\phi\core\device_context.h

方法
:::::::::::::::::::::

DeviceContext ( ) ;
'''''''''''
 @brief Default construct.



DeviceContext ( const DeviceContext & ) ;
'''''''''''
 @brief Copy construct.


**参数**
'''''''''''
	- **&** (const DeviceContext)

DeviceContext ( DeviceContext & & ) ;
'''''''''''
 @brief Move construct.


**参数**
'''''''''''
	- **&** (DeviceContext&)

DeviceContext & operator = ( DeviceContext & & ) ;
'''''''''''
 @brief Move assign operator.


**参数**
'''''''''''
	- **&** (DeviceContext&)

**返回**
'''''''''''
DeviceContext
virtual ~DeviceContext ( ) ;
'''''''''''
 @brief Default destruct.



void SetAllocator ( const Allocator * ) ;
'''''''''''
 @brief Set the device-related Allocator object. @param allocator


**参数**
'''''''''''
	- **** (const Allocator*)

void SetHostAllocator ( const Allocator * ) ;
'''''''''''
 @brief Set the host Allocator object. @param allocator


**参数**
'''''''''''
	- **** (const Allocator*)

void SetZeroAllocator ( const Allocator * ) ;
'''''''''''
 @brief Set the zero-size Allocator object. @param allocator


**参数**
'''''''''''
	- **** (const Allocator*)

void SetHostZeroAllocator ( const Allocator * ) ;
'''''''''''
 @brief Set the zero-size host Allocator object. @param allocator


**参数**
'''''''''''
	- **** (const Allocator*)

void SetPinnedAllocator ( const Allocator * ) ;
'''''''''''
 @brief Set the zero-size Allocator object. @param allocator


**参数**
'''''''''''
	- **** (const Allocator*)

const Allocator & GetAllocator ( ) const ;
'''''''''''
 @brief Get the const Allocator object. @return Allocator



**返回**
'''''''''''
Allocator
const Allocator & GetHostAllocator ( ) const ;
'''''''''''
 @brief Get the const device-related Allocator object. @return Allocator



**返回**
'''''''''''
Allocator
const Allocator & GetZeroAllocator ( ) const ;
'''''''''''



**返回**
'''''''''''
Allocator
const Allocator & GetHostZeroAllocator ( ) const ;
'''''''''''



**返回**
'''''''''''
Allocator
const Allocator & GetPinnedAllocator ( ) const ;
'''''''''''



**返回**
'''''''''''
Allocator
void SetCUDAGraphAllocator ( const Allocator * ) ;
'''''''''''
 @brief Set the CUDA graph Allocator object. @param allocator


**参数**
'''''''''''
	- **** (const Allocator*)

const Allocator & GetCUDAGraphAllocator ( ) const ;
'''''''''''
 @brief Get the const CUDA graph Allocator object. @return Allocator



**返回**
'''''''''''
Allocator
bool IsCUDAGraphAllocatorValid ( ) const ;
'''''''''''
 @brief Test whether the CUDA graph allocator is valid This method should be called before calling GetCUDAGraphAllocator(). Other unit can calls GetCUDAGraphAllocator() method, only when this method returns True! @return true if cuda_graph_allocator_ is valid, false otherwise



**返回**
'''''''''''
bool
void * Alloc ( TensorBase * , DataType dtype , size_t requested_size = 0 , bool pinned = false , bool fake_alloc = false ) const ;
'''''''''''
 @brief Allocate device memory for tensor.


**参数**
'''''''''''
	- **** (TensorBase*)
	- **dtype** (DataType)
	- **requested_size** (size_t)
	- **pinned** (bool)
	- **fake_alloc** (bool)

T * Alloc ( TensorBase * tensor , size_t requested_size = 0 , bool pinned = false ) const ;
'''''''''''


**参数**
'''''''''''
	- **tensor** (TensorBase*)
	- **requested_size** (size_t)
	- **pinned** (bool)

**返回**
'''''''''''
T
void * HostAlloc ( TensorBase * tensor , DataType dtype , size_t requested_size = 0 , bool fake_alloc = false ) const ;
'''''''''''
 @brief Allocate host memory for tensor.


**参数**
'''''''''''
	- **tensor** (TensorBase*)
	- **dtype** (DataType)
	- **requested_size** (size_t)
	- **fake_alloc** (bool)

T * HostAlloc ( TensorBase * tensor , size_t requested_size = 0 ) const ;
'''''''''''


**参数**
'''''''''''
	- **tensor** (TensorBase*)
	- **requested_size** (size_t)

**返回**
'''''''''''
T
virtual const Place & GetPlace ( ) const = 0 ;
'''''''''''



**返回**
'''''''''''
Place
virtual void Wait ( ) const {
'''''''''''



void SetGenerator ( Generator * ) ;
'''''''''''
 @brief Set the generator for special op. @param Generator


**参数**
'''''''''''
	- **** (Generator*)

Generator * GetGenerator ( ) const ;
'''''''''''
 @brief Get the generator object. @return Generator



**返回**
'''''''''''
Generator
void SetHostGenerator ( Generator * ) ;
'''''''''''
 @brief Set the host generator for special op. @param Generator


**参数**
'''''''''''
	- **** (Generator*)

Generator * GetHostGenerator ( ) const ;
'''''''''''
 @brief Get the host generator object. @return Generator



**返回**
'''''''''''
Generator
TypeInfo<DeviceContext> type_info ( ) const {
'''''''''''
 @brief Return the type information of the derived class to supportsafely downcast in non-rtti environment. @return The type information of the derived class.



**返回**
'''''''''''
TypeInfo<DeviceContext>
void SetCommContext ( distributed::CommContext * comm_context ) ;
'''''''''''
 @brief Set the comm context point. @param CommContext


**参数**
'''''''''''
	- **comm_context** (distributed::CommContext*)

distributed::CommContext * GetCommContext ( ) const ;
'''''''''''
 @brief Get the comm context point. @return comm context point



**返回**
'''''''''''
distributed::CommContext
