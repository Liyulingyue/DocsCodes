.. _cn_api_DeviceContext:

DeviceContext[源代码](https://github.com/PaddlePaddle/Paddle/blob/develop/paddle\phi\core\device_context.h)
-------------------------------

.. cpp:class:: DeviceContext ( const DeviceContext & ) ;

<name="desc">
 DeviceContext provides device-related interfaces. All kernels must access the interfaces provided by the backend through DeviceContext.

</name>

定义目录
:::::::::::::::::::::
paddle\phi\core\device_context.h

方法
:::::::::::::::::::::
DeviceContext ( ) ;
'''''''''
<name="desc">
 @brief Default construct.

</name>


返回
:::::::::::::::::::::
无

DeviceContext ( const DeviceContext & ) ;
'''''''''
<name="desc">
 @brief Copy construct.

</name>


参数
:::::::::::::::::::::
	- **&** (const DeviceContext) - 

返回
:::::::::::::::::::::
无

DeviceContext ( DeviceContext & & ) ;
'''''''''
<name="desc">
 @brief Move construct.

</name>


参数
:::::::::::::::::::::
	- **&** (DeviceContext&) - 

返回
:::::::::::::::::::::
无

DeviceContext & operator = ( DeviceContext & & ) ;
'''''''''
<name="desc">
 @brief Move assign operator.

</name>


参数
:::::::::::::::::::::
	- **&** (DeviceContext&) - 

返回
:::::::::::::::::::::
DeviceContext

virtual ~DeviceContext ( ) ;
'''''''''
<name="desc">
 @brief Default destruct.

</name>


返回
:::::::::::::::::::::
无

void SetAllocator ( const Allocator * ) ;
'''''''''
<name="desc">
 @brief Set the device-related Allocator object. @param allocator

</name>


参数
:::::::::::::::::::::
	- **** (const Allocator*) - 

返回
:::::::::::::::::::::
void

void SetHostAllocator ( const Allocator * ) ;
'''''''''
<name="desc">
 @brief Set the host Allocator object. @param allocator

</name>


参数
:::::::::::::::::::::
	- **** (const Allocator*) - 

返回
:::::::::::::::::::::
void

void SetZeroAllocator ( const Allocator * ) ;
'''''''''
<name="desc">
 @brief Set the zero-size Allocator object. @param allocator

</name>


参数
:::::::::::::::::::::
	- **** (const Allocator*) - 

返回
:::::::::::::::::::::
void

void SetHostZeroAllocator ( const Allocator * ) ;
'''''''''
<name="desc">
 @brief Set the zero-size host Allocator object. @param allocator

</name>


参数
:::::::::::::::::::::
	- **** (const Allocator*) - 

返回
:::::::::::::::::::::
void

void SetPinnedAllocator ( const Allocator * ) ;
'''''''''
<name="desc">
 @brief Set the zero-size Allocator object. @param allocator

</name>


参数
:::::::::::::::::::::
	- **** (const Allocator*) - 

返回
:::::::::::::::::::::
void

const Allocator & GetAllocator ( ) const ;
'''''''''
<name="desc">
 @brief Get the const Allocator object. @return Allocator

</name>


返回
:::::::::::::::::::::
Allocator

const Allocator & GetHostAllocator ( ) const ;
'''''''''
<name="desc">
 @brief Get the const device-related Allocator object. @return Allocator

</name>


返回
:::::::::::::::::::::
Allocator

const Allocator & GetZeroAllocator ( ) const ;
'''''''''
<name="desc">

</name>


返回
:::::::::::::::::::::
Allocator

const Allocator & GetHostZeroAllocator ( ) const ;
'''''''''
<name="desc">

</name>


返回
:::::::::::::::::::::
Allocator

const Allocator & GetPinnedAllocator ( ) const ;
'''''''''
<name="desc">

</name>


返回
:::::::::::::::::::::
Allocator

void SetCUDAGraphAllocator ( const Allocator * ) ;
'''''''''
<name="desc">
 @brief Set the CUDA graph Allocator object. @param allocator

</name>


参数
:::::::::::::::::::::
	- **** (const Allocator*) - 

返回
:::::::::::::::::::::
void

const Allocator & GetCUDAGraphAllocator ( ) const ;
'''''''''
<name="desc">
 @brief Get the const CUDA graph Allocator object. @return Allocator

</name>


返回
:::::::::::::::::::::
Allocator

bool IsCUDAGraphAllocatorValid ( ) const ;
'''''''''
<name="desc">
 @brief Test whether the CUDA graph allocator is valid This method should be called before calling GetCUDAGraphAllocator(). Other unit can calls GetCUDAGraphAllocator() method, only when this method returns True! @return true if cuda_graph_allocator_ is valid, false otherwise

</name>


返回
:::::::::::::::::::::
bool

void * Alloc ( TensorBase * , DataType dtype , size_t requested_size = 0 , bool pinned = false , bool fake_alloc = false ) const ;
'''''''''
<name="desc">
 @brief Allocate device memory for tensor.

</name>


参数
:::::::::::::::::::::
	- **** (TensorBase*) - 
	- **dtype** (DataType) - 
	- **requested_size** (size_t) - 
	- **pinned** (bool) - 
	- **fake_alloc** (bool) - 

返回
:::::::::::::::::::::
void

T * Alloc ( TensorBase * tensor , size_t requested_size = 0 , bool pinned = false ) const ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **tensor** (TensorBase*) - 
	- **requested_size** (size_t) - 
	- **pinned** (bool) - 

返回
:::::::::::::::::::::
T

void * HostAlloc ( TensorBase * tensor , DataType dtype , size_t requested_size = 0 , bool fake_alloc = false ) const ;
'''''''''
<name="desc">
 @brief Allocate host memory for tensor.

</name>


参数
:::::::::::::::::::::
	- **tensor** (TensorBase*) - 
	- **dtype** (DataType) - 
	- **requested_size** (size_t) - 
	- **fake_alloc** (bool) - 

返回
:::::::::::::::::::::
void

T * HostAlloc ( TensorBase * tensor , size_t requested_size = 0 ) const ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **tensor** (TensorBase*) - 
	- **requested_size** (size_t) - 

返回
:::::::::::::::::::::
T

virtual const Place & GetPlace ( ) const = 0 ;
'''''''''
<name="desc">

</name>


返回
:::::::::::::::::::::
Place

virtual void Wait ( ) const {
'''''''''
<name="desc">

</name>


返回
:::::::::::::::::::::
void

void SetGenerator ( Generator * ) ;
'''''''''
<name="desc">
 @brief Set the generator for special op. @param Generator

</name>


参数
:::::::::::::::::::::
	- **** (Generator*) - 

返回
:::::::::::::::::::::
void

Generator * GetGenerator ( ) const ;
'''''''''
<name="desc">
 @brief Get the generator object. @return Generator

</name>


返回
:::::::::::::::::::::
Generator

void SetHostGenerator ( Generator * ) ;
'''''''''
<name="desc">
 @brief Set the host generator for special op. @param Generator

</name>


参数
:::::::::::::::::::::
	- **** (Generator*) - 

返回
:::::::::::::::::::::
void

Generator * GetHostGenerator ( ) const ;
'''''''''
<name="desc">
 @brief Get the host generator object. @return Generator

</name>


返回
:::::::::::::::::::::
Generator

TypeInfo<DeviceContext> type_info ( ) const {
'''''''''
<name="desc">
 @brief Return the type information of the derived class to supportsafely downcast in non-rtti environment. @return The type information of the derived class.

</name>


返回
:::::::::::::::::::::
TypeInfo<DeviceContext>

void SetCommContext ( distributed::CommContext * comm_context ) ;
'''''''''
<name="desc">
 @brief Set the comm context point. @param CommContext

</name>


参数
:::::::::::::::::::::
	- **comm_context** (distributed::CommContext*) - 

返回
:::::::::::::::::::::
void

distributed::CommContext * GetCommContext ( ) const ;
'''''''''
<name="desc">
 @brief Get the comm context point. @return comm context point

</name>


返回
:::::::::::::::::::::
distributed::CommContext



<name="reference_link">

</name>

