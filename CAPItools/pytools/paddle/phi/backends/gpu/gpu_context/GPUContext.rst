.. _cn_api_GPUContext:

GPUContext[源代码](https://github.com/PaddlePaddle/Paddle/blob/develop/paddle\phi\backends\gpu\gpu_context.h)
-------------------------------

.. cpp:class:: explicit GPUContext ( const GPUPlace & place , bool init = true , int stream_priority = 0 ) ;

<name="desc">

</name>

定义目录
:::::::::::::::::::::
paddle\phi\backends\gpu\gpu_context.h

方法
:::::::::::::::::::::
explicit GPUContext ( const GPUPlace & place , bool init = true , int stream_priority = 0 ) ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **place** (const GPUPlace&) - 
	- **init** (bool) - 
	- **stream_priority** (int) - 

返回
:::::::::::::::::::::
无

GPUContext ( GPUContext & & ) ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **&** (GPUContext&) - 

返回
:::::::::::::::::::::
无

GPUContext & operator = ( GPUContext & & ) ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **&** (GPUContext&) - 

返回
:::::::::::::::::::::
GPUContext

virtual ~GPUContext ( ) ;
'''''''''
<name="desc">

</name>


返回
:::::::::::::::::::::
无

const Place & GetPlace ( ) const override ;
'''''''''
<name="desc">
/*! \briefReturn place in the device context. 
</name>


返回
:::::::::::::::::::::
Place

gpuStream_t stream ( ) const ;
'''''''''
<name="desc">
/*! \briefReturn gpu stream in the device context. 
</name>


返回
:::::::::::::::::::::
gpuStream_t

CUDAStream * cuda_stream ( ) const ;
'''''''''
<name="desc">
/*! \briefReturn CUDAStream in the device context. 
</name>


返回
:::::::::::::::::::::
CUDAStream

dnnHandle_t cudnn_handle ( ) const ;
'''''''''
<name="desc">
/*! \briefReturn cudnnhandle in the device context. 
</name>


返回
:::::::::::::::::::::
dnnHandle_t

blasHandle_t cublas_handle ( ) const ;
'''''''''
<name="desc">
/*! \briefReturn cublas handle in the device context. 
</name>


返回
:::::::::::::::::::::
blasHandle_t

blasLtHandle_t cublaslt_handle ( ) const ;
'''''''''
<name="desc">
/*! \briefReturn cublasLt handle in the device context. 
</name>


返回
:::::::::::::::::::::
blasLtHandle_t

solverHandle_t cusolver_dn_handle ( ) const ;
'''''''''
<name="desc">
/*! \briefReturn cusolver handle in the device context. 
</name>


返回
:::::::::::::::::::::
solverHandle_t

sparseHandle_t cusparse_handle ( ) const ;
'''''''''
<name="desc">
/*! \briefReturn cusparse handle in the device context. 
</name>


返回
:::::::::::::::::::::
sparseHandle_t

void Wait ( ) const override ;
'''''''''
<name="desc">
/*! \briefWait for all operations completion in the stream. 
</name>


返回
:::::::::::::::::::::
void

void WaitEvent ( gpuEvent_t ev ) const ;
'''''''''
<name="desc">
/*! \briefWait for event in the stream. 
</name>


参数
:::::::::::::::::::::
	- **ev** (gpuEvent_t) - 

返回
:::::::::::::::::::::
void

bool tensor_core_available ( ) const ;
'''''''''
<name="desc">
/*! \briefCheck whether tensor core is supported 
</name>


返回
:::::::::::::::::::::
bool

int GetComputeCapability ( ) const ;
'''''''''
<name="desc">
/*! \briefReturn compute capability in the device context. 
</name>


返回
:::::::::::::::::::::
int

int GetMaxPhysicalThreadCount ( ) const ;
'''''''''
<name="desc">
/*! \briefReturn the max physical thread count in the device context 
</name>


返回
:::::::::::::::::::::
int

int GetSMCount ( ) const ;
'''''''''
<name="desc">
/*! \briefReturn the SM count in the device context 
</name>


返回
:::::::::::::::::::::
int

int GetMaxThreadsPerBlock ( ) const ;
'''''''''
<name="desc">
/*! \briefReturn the Max thread num of block in the device context 
</name>


返回
:::::::::::::::::::::
int

std::array<int , 3> GetCUDAMaxGridDimSize ( ) const ;
'''''''''
<name="desc">
/*! \briefReturn the max grid dim size in the device context 
</name>


返回
:::::::::::::::::::::
std::array<int , 3>

Eigen::GpuDevice * eigen_device ( ) const ;
'''''''''
<name="desc">
/*! \briefReturn eigen device in the device context. 
</name>


返回
:::::::::::::::::::::
Eigen::GpuDevice

DnnWorkspaceHandle cudnn_workspace_handle ( ) const ;
'''''''''
<name="desc">
/*! \briefReturn a cudnn workspace handle to call multiple cudnnfunctions without interrupting by other threads.Once the first cudnn function is called by the handle, a lockwould be acquired to prevent other threads from accessing theworkspace. Once the handle is destructed, the lock would be released.

</name>


返回
:::::::::::::::::::::
DnnWorkspaceHandle

void CublasCall ( const std::function<void ( blasHandle_t )> & ) const ;
'''''''''
<name="desc">
/*! \briefCall cublas function safely. 
</name>


参数
:::::::::::::::::::::
	- **&** (const std::function<void ( blasHandle_t )>) - 

返回
:::::::::::::::::::::
void

void TensorCoreCublasCallIfAvailable ( const std::function<void ( blasHandle_t )> & ) const ;
'''''''''
<name="desc">
/*! \briefCall cublas function with Tensor Core safely. If
Tensor Core is not available, use DEFAULT_MATH instead. 
</name>


参数
:::::::::::::::::::::
	- **&** (const std::function<void ( blasHandle_t )>) - 

返回
:::::::::::::::::::::
void

void CusparseCall ( const std::function<void ( sparseHandle_t )> & ) const ;
'''''''''
<name="desc">
/*! \briefCall cusparse function safely. 
</name>


参数
:::::::::::::::::::::
	- **&** (const std::function<void ( sparseHandle_t )>) - 

返回
:::::::::::::::::::::
void

void RecordEvent ( gpuEvent_t ev , const std::function<void ( )> & callback ) const ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **ev** (gpuEvent_t) - 
	- **callback** (const std::function<void ( )>&) - 

返回
:::::::::::::::::::::
void

void RecordEvent ( gpuEvent_t ev ) const ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **ev** (gpuEvent_t) - 

返回
:::::::::::::::::::::
void

void AddStreamCallback ( const std::function<void ( )> & callback ) const ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **callback** (const std::function<void ( )>&) - 

返回
:::::::::::::::::::::
void

void WaitStreamCallback ( ) const ;
'''''''''
<name="desc">

</name>


返回
:::::::::::::::::::::
void

bool HasDnnAttr ( const std::string & attr_name ) const ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **attr_name** (const std::string&) - 

返回
:::::::::::::::::::::
bool

const Attribute & GetDnnAttr ( const std::string & attr_name ) const ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **attr_name** (const std::string&) - 

返回
:::::::::::::::::::::
Attribute

void SetDnnAttr ( const std::string & attr_name , Attribute attr ) ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **attr_name** (const std::string&) - 
	- **attr** (Attribute) - 

返回
:::::::::::::::::::::
void

void ClearDnnAttr ( ) ;
'''''''''
<name="desc">

</name>


返回
:::::::::::::::::::::
void

static const char * name ( ) {
'''''''''
<name="desc">

</name>


返回
:::::::::::::::::::::
char

ncclComm_t nccl_comm ( ) const ;
'''''''''
<name="desc">
/*! \briefReturn nccl communicators. 
</name>


返回
:::::::::::::::::::::
ncclComm_t

void set_nccl_comm ( ncclComm_t comm ) ;
'''''''''
<name="desc">
/*! \briefSet nccl communicators. 
</name>


参数
:::::::::::::::::::::
	- **comm** (ncclComm_t) - 

返回
:::::::::::::::::::::
void

void Init ( ) ;
'''''''''
<name="desc">

</name>


返回
:::::::::::::::::::::
void

void PartialInitWithoutAllocator ( int stream_priority = 0 ) ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **stream_priority** (int) - 

返回
:::::::::::::::::::::
void

void PartialInitWithAllocator ( ) ;
'''''''''
<name="desc">

</name>


返回
:::::::::::::::::::::
void

void SetCUDAStream ( CUDAStream * , bool clear = true ) ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **** (CUDAStream*) - 
	- **clear** (bool) - 

返回
:::::::::::::::::::::
void



<name="reference_link">

</name>

