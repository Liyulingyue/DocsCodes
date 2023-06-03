.. _cn_api_GPUContext:

GPUContext[源代码](https://github.com/PaddlePaddle/Paddle/blob/develop/paddle\phi\backends\gpu\gpu_context.h)
-------------------------------

.. cpp:class:: explicit GPUContext ( const GPUPlace & place , bool init = true , int stream_priority = 0 ) ;


定义目录
:::::::::::::::::::::
paddle\phi\backends\gpu\gpu_context.h

方法
:::::::::::::::::::::

explicit GPUContext ( const GPUPlace & place , bool init = true , int stream_priority = 0 ) ;
'''''''''''


**参数**
'''''''''''
	- **place** (const GPUPlace&)
	- **init** (bool)
	- **stream_priority** (int)

GPUContext ( GPUContext & & ) ;
'''''''''''



GPUContext & operator = ( GPUContext & & ) ;
'''''''''''



**返回**
'''''''''''
GPUContext &

virtual ~GPUContext ( ) ;
'''''''''''



const Place & GetPlace ( ) const override ;
'''''''''''
/*! \briefReturn place in the device context. 


**返回**
'''''''''''
const Place &

gpuStream_t stream ( ) const ;
'''''''''''
/*! \briefReturn gpu stream in the device context. 


**返回**
'''''''''''
gpuStream_t

CUDAStream * cuda_stream ( ) const ;
'''''''''''
/*! \briefReturn CUDAStream in the device context. 


**返回**
'''''''''''
CUDAStream *

dnnHandle_t cudnn_handle ( ) const ;
'''''''''''
/*! \briefReturn cudnnhandle in the device context. 


**返回**
'''''''''''
dnnHandle_t

blasHandle_t cublas_handle ( ) const ;
'''''''''''
/*! \briefReturn cublas handle in the device context. 


**返回**
'''''''''''
blasHandle_t

blasLtHandle_t cublaslt_handle ( ) const ;
'''''''''''
/*! \briefReturn cublasLt handle in the device context. 


**返回**
'''''''''''
blasLtHandle_t

solverHandle_t cusolver_dn_handle ( ) const ;
'''''''''''
/*! \briefReturn cusolver handle in the device context. 


**返回**
'''''''''''
solverHandle_t

sparseHandle_t cusparse_handle ( ) const ;
'''''''''''
/*! \briefReturn cusparse handle in the device context. 


**返回**
'''''''''''
sparseHandle_t

void Wait ( ) const override ;
'''''''''''
/*! \briefWait for all operations completion in the stream. 


void WaitEvent ( gpuEvent_t ev ) const ;
'''''''''''
/*! \briefWait for event in the stream. 

**参数**
'''''''''''
	- **ev** (gpuEvent_t)

bool tensor_core_available ( ) const ;
'''''''''''
/*! \briefCheck whether tensor core is supported 


**返回**
'''''''''''
bool

int GetComputeCapability ( ) const ;
'''''''''''
/*! \briefReturn compute capability in the device context. 


**返回**
'''''''''''
int

int GetMaxPhysicalThreadCount ( ) const ;
'''''''''''
/*! \briefReturn the max physical thread count in the device context 


**返回**
'''''''''''
int

int GetSMCount ( ) const ;
'''''''''''
/*! \briefReturn the SM count in the device context 


**返回**
'''''''''''
int

int GetMaxThreadsPerBlock ( ) const ;
'''''''''''
/*! \briefReturn the Max thread num of block in the device context 


**返回**
'''''''''''
int

std::array<int , 3> GetCUDAMaxGridDimSize ( ) const ;
'''''''''''
/*! \briefReturn the max grid dim size in the device context 


**返回**
'''''''''''
std::array<int, 3 >

Eigen::GpuDevice * eigen_device ( ) const ;
'''''''''''
/*! \briefReturn eigen device in the device context. 


**返回**
'''''''''''
Eigen::GpuDevice *

DnnWorkspaceHandle cudnn_workspace_handle ( ) const ;
'''''''''''
/*! \briefReturn a cudnn workspace handle to call multiple cudnnfunctions without interrupting by other threads.Once the first cudnn function is called by the handle, a lockwould be acquired to prevent other threads from accessing theworkspace. Once the handle is destructed, the lock would be released.



**返回**
'''''''''''
DnnWorkspaceHandle

void CublasCall ( const std::function<void ( blasHandle_t )> & ) const ;
'''''''''''
/*! \briefCall cublas function safely. 


void TensorCoreCublasCallIfAvailable ( const std::function<void ( blasHandle_t )> & ) const ;
'''''''''''
/*! \briefCall cublas function with Tensor Core safely. If
Tensor Core is not available, use DEFAULT_MATH instead. 


void CusparseCall ( const std::function<void ( sparseHandle_t )> & ) const ;
'''''''''''
/*! \briefCall cusparse function safely. 


void RecordEvent ( gpuEvent_t ev , const std::function<void ( )> & callback ) const ;
'''''''''''


**参数**
'''''''''''
	- **ev** (gpuEvent_t)
	- **callback** (const std::function<void ( )>&)

void RecordEvent ( gpuEvent_t ev ) const ;
'''''''''''


**参数**
'''''''''''
	- **ev** (gpuEvent_t)

void AddStreamCallback ( const std::function<void ( )> & callback ) const ;
'''''''''''


**参数**
'''''''''''
	- **callback** (const std::function<void ( )>&)

void WaitStreamCallback ( ) const ;
'''''''''''



bool HasDnnAttr ( const std::string & attr_name ) const ;
'''''''''''


**参数**
'''''''''''
	- **attr_name** (const std::string&)

**返回**
'''''''''''
bool

const Attribute & GetDnnAttr ( const std::string & attr_name ) const ;
'''''''''''


**参数**
'''''''''''
	- **attr_name** (const std::string&)

**返回**
'''''''''''
const Attribute &

void SetDnnAttr ( const std::string & attr_name , Attribute attr ) ;
'''''''''''


**参数**
'''''''''''
	- **attr_name** (const std::string&)
	- **attr** (Attribute)

void ClearDnnAttr ( ) ;
'''''''''''



static const char * name ( ) {
'''''''''''



**返回**
'''''''''''
const char *

ncclComm_t nccl_comm ( ) const ;
'''''''''''
/*! \briefReturn nccl communicators. 


**返回**
'''''''''''
ncclComm_t

void set_nccl_comm ( ncclComm_t comm ) ;
'''''''''''
/*! \briefSet nccl communicators. 

**参数**
'''''''''''
	- **comm** (ncclComm_t)

void Init ( ) ;
'''''''''''



void PartialInitWithoutAllocator ( int stream_priority = 0 ) ;
'''''''''''


**参数**
'''''''''''
	- **stream_priority** (int)

void PartialInitWithAllocator ( ) ;
'''''''''''



void SetCUDAStream ( CUDAStream * , bool clear = true ) ;
'''''''''''


**参数**
'''''''''''
	- **** (CUDAStream*)
	- **clear** (bool)

