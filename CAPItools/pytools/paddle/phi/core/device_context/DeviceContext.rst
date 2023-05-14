.. _cn_api_DeviceContext:

DeviceContext[Դ����](https://github.com/PaddlePaddle/Paddle/blob/develop/paddle\phi\core\device_context.h)
-------------------------------

.. cpp:class:: DeviceContext ( const DeviceContext & ) ;

<name="desc">
 DeviceContext provides device-related interfaces. All kernels must access the interfaces provided by the backend through DeviceContext.

</name>

����Ŀ¼
:::::::::::::::::::::
paddle\phi\core\device_context.h

����
:::::::::::::::::::::
DeviceContext ( ) ;
'''''''''
<name="desc">
 @brief Default construct.

</name>


����
:::::::::::::::::::::
��

DeviceContext ( const DeviceContext & ) ;
'''''''''
<name="desc">
 @brief Copy construct.

</name>


����
:::::::::::::::::::::
	- **&** (const DeviceContext) - 

����
:::::::::::::::::::::
��

DeviceContext ( DeviceContext & & ) ;
'''''''''
<name="desc">
 @brief Move construct.

</name>


����
:::::::::::::::::::::
	- **&** (DeviceContext&) - 

����
:::::::::::::::::::::
��

DeviceContext & operator = ( DeviceContext & & ) ;
'''''''''
<name="desc">
 @brief Move assign operator.

</name>


����
:::::::::::::::::::::
	- **&** (DeviceContext&) - 

����
:::::::::::::::::::::
DeviceContext

virtual ~DeviceContext ( ) ;
'''''''''
<name="desc">
 @brief Default destruct.

</name>


����
:::::::::::::::::::::
��

void SetAllocator ( const Allocator * ) ;
'''''''''
<name="desc">
 @brief Set the device-related Allocator object. @param allocator

</name>


����
:::::::::::::::::::::
	- **** (const Allocator*) - 

����
:::::::::::::::::::::
void

void SetHostAllocator ( const Allocator * ) ;
'''''''''
<name="desc">
 @brief Set the host Allocator object. @param allocator

</name>


����
:::::::::::::::::::::
	- **** (const Allocator*) - 

����
:::::::::::::::::::::
void

void SetZeroAllocator ( const Allocator * ) ;
'''''''''
<name="desc">
 @brief Set the zero-size Allocator object. @param allocator

</name>


����
:::::::::::::::::::::
	- **** (const Allocator*) - 

����
:::::::::::::::::::::
void

void SetHostZeroAllocator ( const Allocator * ) ;
'''''''''
<name="desc">
 @brief Set the zero-size host Allocator object. @param allocator

</name>


����
:::::::::::::::::::::
	- **** (const Allocator*) - 

����
:::::::::::::::::::::
void

void SetPinnedAllocator ( const Allocator * ) ;
'''''''''
<name="desc">
 @brief Set the zero-size Allocator object. @param allocator

</name>


����
:::::::::::::::::::::
	- **** (const Allocator*) - 

����
:::::::::::::::::::::
void

const Allocator & GetAllocator ( ) const ;
'''''''''
<name="desc">
 @brief Get the const Allocator object. @return Allocator

</name>


����
:::::::::::::::::::::
Allocator

const Allocator & GetHostAllocator ( ) const ;
'''''''''
<name="desc">
 @brief Get the const device-related Allocator object. @return Allocator

</name>


����
:::::::::::::::::::::
Allocator

const Allocator & GetZeroAllocator ( ) const ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
Allocator

const Allocator & GetHostZeroAllocator ( ) const ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
Allocator

const Allocator & GetPinnedAllocator ( ) const ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
Allocator

void SetCUDAGraphAllocator ( const Allocator * ) ;
'''''''''
<name="desc">
 @brief Set the CUDA graph Allocator object. @param allocator

</name>


����
:::::::::::::::::::::
	- **** (const Allocator*) - 

����
:::::::::::::::::::::
void

const Allocator & GetCUDAGraphAllocator ( ) const ;
'''''''''
<name="desc">
 @brief Get the const CUDA graph Allocator object. @return Allocator

</name>


����
:::::::::::::::::::::
Allocator

bool IsCUDAGraphAllocatorValid ( ) const ;
'''''''''
<name="desc">
 @brief Test whether the CUDA graph allocator is valid This method should be called before calling GetCUDAGraphAllocator(). Other unit can calls GetCUDAGraphAllocator() method, only when this method returns True! @return true if cuda_graph_allocator_ is valid, false otherwise

</name>


����
:::::::::::::::::::::
bool

void * Alloc ( TensorBase * , DataType dtype , size_t requested_size = 0 , bool pinned = false , bool fake_alloc = false ) const ;
'''''''''
<name="desc">
 @brief Allocate device memory for tensor.

</name>


����
:::::::::::::::::::::
	- **** (TensorBase*) - 
	- **dtype** (DataType) - 
	- **requested_size** (size_t) - 
	- **pinned** (bool) - 
	- **fake_alloc** (bool) - 

����
:::::::::::::::::::::
void

T * Alloc ( TensorBase * tensor , size_t requested_size = 0 , bool pinned = false ) const ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
	- **tensor** (TensorBase*) - 
	- **requested_size** (size_t) - 
	- **pinned** (bool) - 

����
:::::::::::::::::::::
T

void * HostAlloc ( TensorBase * tensor , DataType dtype , size_t requested_size = 0 , bool fake_alloc = false ) const ;
'''''''''
<name="desc">
 @brief Allocate host memory for tensor.

</name>


����
:::::::::::::::::::::
	- **tensor** (TensorBase*) - 
	- **dtype** (DataType) - 
	- **requested_size** (size_t) - 
	- **fake_alloc** (bool) - 

����
:::::::::::::::::::::
void

T * HostAlloc ( TensorBase * tensor , size_t requested_size = 0 ) const ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
	- **tensor** (TensorBase*) - 
	- **requested_size** (size_t) - 

����
:::::::::::::::::::::
T

virtual const Place & GetPlace ( ) const = 0 ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
Place

virtual void Wait ( ) const {
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
void

void SetGenerator ( Generator * ) ;
'''''''''
<name="desc">
 @brief Set the generator for special op. @param Generator

</name>


����
:::::::::::::::::::::
	- **** (Generator*) - 

����
:::::::::::::::::::::
void

Generator * GetGenerator ( ) const ;
'''''''''
<name="desc">
 @brief Get the generator object. @return Generator

</name>


����
:::::::::::::::::::::
Generator

void SetHostGenerator ( Generator * ) ;
'''''''''
<name="desc">
 @brief Set the host generator for special op. @param Generator

</name>


����
:::::::::::::::::::::
	- **** (Generator*) - 

����
:::::::::::::::::::::
void

Generator * GetHostGenerator ( ) const ;
'''''''''
<name="desc">
 @brief Get the host generator object. @return Generator

</name>


����
:::::::::::::::::::::
Generator

TypeInfo<DeviceContext> type_info ( ) const {
'''''''''
<name="desc">
 @brief Return the type information of the derived class to supportsafely downcast in non-rtti environment. @return The type information of the derived class.

</name>


����
:::::::::::::::::::::
TypeInfo<DeviceContext>

void SetCommContext ( distributed::CommContext * comm_context ) ;
'''''''''
<name="desc">
 @brief Set the comm context point. @param CommContext

</name>


����
:::::::::::::::::::::
	- **comm_context** (distributed::CommContext*) - 

����
:::::::::::::::::::::
void

distributed::CommContext * GetCommContext ( ) const ;
'''''''''
<name="desc">
 @brief Get the comm context point. @return comm context point

</name>


����
:::::::::::::::::::::
distributed::CommContext



<name="reference_link">

</name>

