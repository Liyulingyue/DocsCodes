.. _cn_api_GPUContext:

GPUContext[Դ����](https://github.com/PaddlePaddle/Paddle/blob/develop/paddle\phi\backends\gpu\gpu_context.h)
-------------------------------

.. cpp:class:: explicit GPUContext ( const GPUPlace & place , bool init = true , int stream_priority = 0 ) ;

<name="desc">

</name>

����Ŀ¼
:::::::::::::::::::::
paddle\phi\backends\gpu\gpu_context.h

����
:::::::::::::::::::::
explicit GPUContext ( const GPUPlace & place , bool init = true , int stream_priority = 0 ) ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
	- **place** (const GPUPlace&) - 
	- **init** (bool) - 
	- **stream_priority** (int) - 

����
:::::::::::::::::::::
��

GPUContext ( GPUContext & & ) ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
	- **&** (GPUContext&) - 

����
:::::::::::::::::::::
��

GPUContext & operator = ( GPUContext & & ) ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
	- **&** (GPUContext&) - 

����
:::::::::::::::::::::
GPUContext

virtual ~GPUContext ( ) ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
��

const Place & GetPlace ( ) const override ;
'''''''''
<name="desc">
/*! \briefReturn place in the device context. 
</name>


����
:::::::::::::::::::::
Place

gpuStream_t stream ( ) const ;
'''''''''
<name="desc">
/*! \briefReturn gpu stream in the device context. 
</name>


����
:::::::::::::::::::::
gpuStream_t

CUDAStream * cuda_stream ( ) const ;
'''''''''
<name="desc">
/*! \briefReturn CUDAStream in the device context. 
</name>


����
:::::::::::::::::::::
CUDAStream

dnnHandle_t cudnn_handle ( ) const ;
'''''''''
<name="desc">
/*! \briefReturn cudnnhandle in the device context. 
</name>


����
:::::::::::::::::::::
dnnHandle_t

blasHandle_t cublas_handle ( ) const ;
'''''''''
<name="desc">
/*! \briefReturn cublas handle in the device context. 
</name>


����
:::::::::::::::::::::
blasHandle_t

blasLtHandle_t cublaslt_handle ( ) const ;
'''''''''
<name="desc">
/*! \briefReturn cublasLt handle in the device context. 
</name>


����
:::::::::::::::::::::
blasLtHandle_t

solverHandle_t cusolver_dn_handle ( ) const ;
'''''''''
<name="desc">
/*! \briefReturn cusolver handle in the device context. 
</name>


����
:::::::::::::::::::::
solverHandle_t

sparseHandle_t cusparse_handle ( ) const ;
'''''''''
<name="desc">
/*! \briefReturn cusparse handle in the device context. 
</name>


����
:::::::::::::::::::::
sparseHandle_t

void Wait ( ) const override ;
'''''''''
<name="desc">
/*! \briefWait for all operations completion in the stream. 
</name>


����
:::::::::::::::::::::
void

void WaitEvent ( gpuEvent_t ev ) const ;
'''''''''
<name="desc">
/*! \briefWait for event in the stream. 
</name>


����
:::::::::::::::::::::
	- **ev** (gpuEvent_t) - 

����
:::::::::::::::::::::
void

bool tensor_core_available ( ) const ;
'''''''''
<name="desc">
/*! \briefCheck whether tensor core is supported 
</name>


����
:::::::::::::::::::::
bool

int GetComputeCapability ( ) const ;
'''''''''
<name="desc">
/*! \briefReturn compute capability in the device context. 
</name>


����
:::::::::::::::::::::
int

int GetMaxPhysicalThreadCount ( ) const ;
'''''''''
<name="desc">
/*! \briefReturn the max physical thread count in the device context 
</name>


����
:::::::::::::::::::::
int

int GetSMCount ( ) const ;
'''''''''
<name="desc">
/*! \briefReturn the SM count in the device context 
</name>


����
:::::::::::::::::::::
int

int GetMaxThreadsPerBlock ( ) const ;
'''''''''
<name="desc">
/*! \briefReturn the Max thread num of block in the device context 
</name>


����
:::::::::::::::::::::
int

std::array<int , 3> GetCUDAMaxGridDimSize ( ) const ;
'''''''''
<name="desc">
/*! \briefReturn the max grid dim size in the device context 
</name>


����
:::::::::::::::::::::
std::array<int , 3>

Eigen::GpuDevice * eigen_device ( ) const ;
'''''''''
<name="desc">
/*! \briefReturn eigen device in the device context. 
</name>


����
:::::::::::::::::::::
Eigen::GpuDevice

DnnWorkspaceHandle cudnn_workspace_handle ( ) const ;
'''''''''
<name="desc">
/*! \briefReturn a cudnn workspace handle to call multiple cudnnfunctions without interrupting by other threads.Once the first cudnn function is called by the handle, a lockwould be acquired to prevent other threads from accessing theworkspace. Once the handle is destructed, the lock would be released.

</name>


����
:::::::::::::::::::::
DnnWorkspaceHandle

void CublasCall ( const std::function<void ( blasHandle_t )> & ) const ;
'''''''''
<name="desc">
/*! \briefCall cublas function safely. 
</name>


����
:::::::::::::::::::::
	- **&** (const std::function<void ( blasHandle_t )>) - 

����
:::::::::::::::::::::
void

void TensorCoreCublasCallIfAvailable ( const std::function<void ( blasHandle_t )> & ) const ;
'''''''''
<name="desc">
/*! \briefCall cublas function with Tensor Core safely. If
Tensor Core is not available, use DEFAULT_MATH instead. 
</name>


����
:::::::::::::::::::::
	- **&** (const std::function<void ( blasHandle_t )>) - 

����
:::::::::::::::::::::
void

void CusparseCall ( const std::function<void ( sparseHandle_t )> & ) const ;
'''''''''
<name="desc">
/*! \briefCall cusparse function safely. 
</name>


����
:::::::::::::::::::::
	- **&** (const std::function<void ( sparseHandle_t )>) - 

����
:::::::::::::::::::::
void

void RecordEvent ( gpuEvent_t ev , const std::function<void ( )> & callback ) const ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
	- **ev** (gpuEvent_t) - 
	- **callback** (const std::function<void ( )>&) - 

����
:::::::::::::::::::::
void

void RecordEvent ( gpuEvent_t ev ) const ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
	- **ev** (gpuEvent_t) - 

����
:::::::::::::::::::::
void

void AddStreamCallback ( const std::function<void ( )> & callback ) const ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
	- **callback** (const std::function<void ( )>&) - 

����
:::::::::::::::::::::
void

void WaitStreamCallback ( ) const ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
void

bool HasDnnAttr ( const std::string & attr_name ) const ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
	- **attr_name** (const std::string&) - 

����
:::::::::::::::::::::
bool

const Attribute & GetDnnAttr ( const std::string & attr_name ) const ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
	- **attr_name** (const std::string&) - 

����
:::::::::::::::::::::
Attribute

void SetDnnAttr ( const std::string & attr_name , Attribute attr ) ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
	- **attr_name** (const std::string&) - 
	- **attr** (Attribute) - 

����
:::::::::::::::::::::
void

void ClearDnnAttr ( ) ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
void

static const char * name ( ) {
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
char

ncclComm_t nccl_comm ( ) const ;
'''''''''
<name="desc">
/*! \briefReturn nccl communicators. 
</name>


����
:::::::::::::::::::::
ncclComm_t

void set_nccl_comm ( ncclComm_t comm ) ;
'''''''''
<name="desc">
/*! \briefSet nccl communicators. 
</name>


����
:::::::::::::::::::::
	- **comm** (ncclComm_t) - 

����
:::::::::::::::::::::
void

void Init ( ) ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
void

void PartialInitWithoutAllocator ( int stream_priority = 0 ) ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
	- **stream_priority** (int) - 

����
:::::::::::::::::::::
void

void PartialInitWithAllocator ( ) ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
void

void SetCUDAStream ( CUDAStream * , bool clear = true ) ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
	- **** (CUDAStream*) - 
	- **clear** (bool) - 

����
:::::::::::::::::::::
void



<name="reference_link">

</name>

