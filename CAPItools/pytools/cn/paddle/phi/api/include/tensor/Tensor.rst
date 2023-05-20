.. _cn_api_Tensor:

Tensor[源代码](https://github.com/PaddlePaddle/Paddle/blob/develop/paddle\phi\api\include\tensor.h)
-------------------------------

.. cpp:class:: Tensor ( std::shared_ptr<phi::TensorBase> tensor_impl , const std::string & name ) ;


定义目录
:::::::::::::::::::::
paddle\phi\api\include\tensor.h

方法
:::::::::::::::::::::

Tensor ( ) = default ;
'''''''''''
Construct a new Tensor object



Tensor ( const Tensor & ) = default ;
'''''''''''
Construct a new Tensor object by copy


**参数**
'''''''''''
	- **&** (const Tensor)

Tensor ( Tensor & & ) = default ;
'''''''''''
Construct a new Tensor object by move


**参数**
'''''''''''
	- **&** (Tensor&)

explicit Tensor ( std::shared_ptr<phi::TensorBase> tensor_impl ) ;
'''''''''''
Construct a new Tensor object by a TensorBase pointer 

**参数**
'''''''''''
	- **tensor_impl** (std::shared_ptr<phi::TensorBase >) - tensor_impl


explicit Tensor ( const Place & place ) ;
'''''''''''
Construct a new Tensor object on the target place. This is a deprecated method and may be removed in the future!!! 

**参数**
'''''''''''
	- **place** (const Place&) - place


Tensor ( const Place & place , const std::vector<int64_t> & shape ) ;
'''''''''''
Construct a new Tensor object on the target place with specified shape. This is a deprecated method and may be removed in the future!!! 

**参数**
'''''''''''
	- **place** (const Place&)
	- **shape** (const std::vector<int64_t>&) - shape


Tensor ( std::shared_ptr<phi::TensorBase> tensor_impl , const std::string & name ) ;
'''''''''''
Construct a new Tensor object by a TensorBase pointer and name 

**参数**
'''''''''''
	- **tensor_impl** (std::shared_ptr<phi::TensorBase >) - tensor_impl

	- **name** (const std::string&)

explicit Tensor ( const std::string & name ) :
'''''''''''
Construct a new Tensor object with name 

**参数**
'''''''''''
	- **name** (const std::string&)

int64_t numel ( ) const ;
'''''''''''
Return the number of elements of Tensor. 


**返回**
'''''''''''
int64_t

int64_t size ( ) const ;
'''''''''''
Get the size of current tensor. The compatible method of `Tensor::numel()`. This is a deprecated method and may be removed in the future! 


**返回**
'''''''''''
int64_t

const phi::DDim & dims ( ) const ;
'''''''''''
Return the dimensions of Tensor. 


**返回**
'''''''''''
phi::DDim

std::vector<int64_t> shape ( ) const ;
'''''''''''
Return the shape (dimensions) of Tensor. The compatible method of `Tensor::dims()`. This is a deprecated method and may be removed in the future! 


**返回**
'''''''''''
std::vector<int64_t>

void reshape ( const std::vector<int64_t> & shape ) ;
'''''''''''
Reset the shape of the tensor. 

**参数**
'''''''''''
	- **shape** (const std::vector<int64_t>&) - shape


DataType dtype ( ) const ;
'''''''''''
Return the data type of Tensor. 


**返回**
'''''''''''
DataType

DataType type ( ) const ;
'''''''''''
Return the data type of Tensor. The compatible method of `Tensor::dtype()`. This is a deprecated method and may be removed in the future! 


**返回**
'''''''''''
DataType

phi::DataLayout layout ( ) const ;
'''''''''''
Return the layout of Tensor. 


**返回**
'''''''''''
DataLayout

bool is_dense_tensor ( ) const ;
'''''''''''
Determine whether tensor is DenseTensor 


**返回**
'''''''''''
false

bool is_selected_rows ( ) const ;
'''''''''''
Determine whether tensor is SelectedRows 


**返回**
'''''''''''
false

bool is_sparse_coo_tensor ( ) const ;
'''''''''''
Determine whether tensor is SparseCooTensor 


**返回**
'''''''''''
false

bool is_sparse_csr_tensor ( ) const ;
'''''''''''
Determine whether tensor is SparseCsrTensor 


**返回**
'''''''''''
false

bool is_string_tensor ( ) const ;
'''''''''''
Determine whether tensor is StringTensor 


**返回**
'''''''''''
false

const Place & place ( ) const ;
'''''''''''
Return the place (device) of Tensor. 


**返回**
'''''''''''
Place

bool is_cpu ( ) const ;
'''''''''''
Determine whether the tensor device is CPU 


**返回**
'''''''''''
false

bool is_gpu ( ) const ;
'''''''''''
Determine whether the tensor device is GPU 


**返回**
'''''''''''
false

bool is_gpu_pinned ( ) const ;
'''''''''''
Determine whether the tensor device is GPU_PINNED 


**返回**
'''''''''''
false

bool is_xpu ( ) const ;
'''''''''''
Determine whether the tensor device is XPU 


**返回**
'''''''''''
false

bool is_custom_device ( ) const ;
'''''''''''
Determine whether the tensor device is CustomDevice 


**返回**
'''''''''''
false

T * mutable_data ( ) ;
'''''''''''
Get the memory pointer in CPU or GPU with specific data type. It's usually used to get the output data pointer, same as the T* data(). 


**返回**
'''''''''''
T*

T * mutable_data ( const Place & place ) ;
'''''''''''
Get the memory pointer in CPU or GPU with specific data type. It's usually used to get the output data pointer. This is a deprecated method and may be removed in the future! 

**参数**
'''''''''''
	- **place** (const Place&)

**返回**
'''''''''''
T*

const T * data ( ) const ;
'''''''''''
Get the const memory pointer directly. It's usually used to get the output data pointer. 


**返回**
'''''''''''
T*

T * data ( ) ;
'''''''''''
Get the memory pointer directly. It's usually used to get the mutable output data pointer. 


**返回**
'''''''''''
T*

const void * data ( ) const ;
'''''''''''
Get the const memory pointer directly. It's usually used to get the output data pointer. 


**返回**
'''''''''''
T*

void * data ( ) ;
'''''''''''
Get the memory pointer directly. It's usually used to get the mutable output data pointer. 


**返回**
'''''''''''
T*

Tensor slice ( int64_t begin_idx , int64_t end_idx ) const ;
'''''''''''
Return a sub-tensor of the given tensor. It is usually used to extract a sub-tensor (which supports modifying the data of the original tensor) to perform further operations. 

**参数**
'''''''''''
	- **begin_idx** (int64_t) - The index of the start row (inclusive) to slice.The index number begins from 0. 
	- **end_idx** (int64_t) - The index of the end row (exclusive) to slice. The index number begins from begin_idx + 1. 

**返回**
'''''''''''
Tensor

const std::shared_ptr<phi::TensorBase> & impl ( ) const ;
'''''''''''
Return the implementation of current Tensor. 


**返回**
'''''''''''
std::shared_ptr<phi::TensorBase>

void set_impl ( const std::shared_ptr<phi::TensorBase> & impl ) ;
'''''''''''
Set the implementation of current Tensor. 

**参数**
'''''''''''
	- **impl** (const std::shared_ptr<phi::TensorBase>&) - impl


void set_impl ( std::shared_ptr<phi::TensorBase> & & impl ) ;
'''''''''''
Set the implementation of current Tensor. 

**参数**
'''''''''''
	- **impl** (std::shared_ptr<phi::TensorBase>) - impl


gpuStream_t stream ( ) const ;
'''''''''''
Get the stream where the tensor is currently located This is a deprecated method and may be removed in the future! 


**返回**
'''''''''''
gpuStream_t

const std::string & name ( ) const {
'''''''''''
Return the name of Tensor. 


**返回**
'''''''''''
const std::string&

void set_name ( const std::string & name ) {
'''''''''''
Set name of Tensor. 

**参数**
'''''''''''
	- **name** (const std::string&)

Tensor copy_to ( const Place & target_place ) const ;
'''''''''''
Copy the current Tensor data to the specified device and return the new Tensor. It's usually used to set the input tensor data. 

**参数**
'''''''''''
	- **target_place** (const Place&)

**返回**
'''''''''''
Tensor

Tensor copy_to ( const Place & place , bool blocking ) const ;
'''''''''''
Transfer the current Tensor to the specified device and return. 

**参数**
'''''''''''
	- **place** (const Place&)
	- **blocking** (bool)

**返回**
'''''''''''
Tensor

void copy_ ( const Tensor & src , const Place & target_place , bool blocking ) ;
'''''''''''
Transfer the source Tensor to current Tensor. 

**参数**
'''''''''''
	- **src** (const Tensor&)
	- **target_place** (const Place&)
	- **blocking** (bool)

Tensor cast ( DataType target_type ) const ;
'''''''''''
Cast datatype from one to another 

**参数**
'''''''''''
	- **target_type** (DataType)

**返回**
'''''''''''
Tensor

bool defined ( ) const ;
'''''''''''
Determine whether it is a meaningful Tensor 


**返回**
'''''''''''
false

bool initialized ( ) const ;
'''''''''''
Determine whether Tensor is initialized. 


**返回**
'''''''''''
false

bool is_initialized ( ) const ;
'''''''''''
Determine whether Tensor is initialized. This is a deprecated method and may be removed in the future! 


**返回**
'''''''''''
false

void reset ( ) ;
'''''''''''
Reset the Tensor implementation



Tensor & operator = ( const Tensor & x ) & ;
'''''''''''
Assignment operator 

**参数**
'''''''''''
	- **x** (const Tensor&)

**返回**
'''''''''''
Tensor&

Tensor & operator = ( Tensor & & x ) & ;
'''''''''''
Move assignment operator 

**参数**
'''''''''''
	- **x** (Tensor)

**返回**
'''''''''''
Tensor&

Tensor operator + ( const Tensor & other ) const ;
'''''''''''
Tensor operants 

**参数**
'''''''''''
	- **other** (const Tensor&)

**返回**
'''''''''''
Tensor

Tensor operator - ( const Tensor & other ) const ;
'''''''''''


**参数**
'''''''''''
	- **other** (const Tensor&)

**返回**
'''''''''''
Tensor
Tensor operator * ( const Tensor & other ) const ;
'''''''''''


**参数**
'''''''''''
	- **other** (const Tensor&)

**返回**
'''''''''''
Tensor
Tensor operator / ( const Tensor & other ) const ;
'''''''''''


**参数**
'''''''''''
	- **other** (const Tensor&)

**返回**
'''''''''''
Tensor
Tensor operator + ( const Scalar & other ) const ;
'''''''''''


**参数**
'''''''''''
	- **other** (Scalar&)

**返回**
'''''''''''
Tensor
Tensor operator - ( const Scalar & other ) const ;
'''''''''''


**参数**
'''''''''''
	- **other** (Scalar&)

**返回**
'''''''''''
Tensor
Tensor operator * ( const Scalar & other ) const ;
'''''''''''


**参数**
'''''''''''
	- **other** (Scalar&)

**返回**
'''''''''''
Tensor
Tensor operator / ( const Scalar & other ) const ;
'''''''''''


**参数**
'''''''''''
	- **other** (Scalar&)

**返回**
'''''''''''
Tensor
Tensor operator<( const Tensor & other ) const ;
'''''''''''


**参数**
'''''''''''
	- **other** (const Tensor&)

**返回**
'''''''''''
Tensor
Tensor operator<= ( const Tensor & other ) const ;
'''''''''''


**参数**
'''''''''''
	- **other** (const Tensor&)

**返回**
'''''''''''
Tensor
Tensor operator = = ( const Tensor & other ) const ;
'''''''''''


**参数**
'''''''''''
	- **other** (const Tensor&)

**返回**
'''''''''''
Tensor
Tensor operator ! = ( const Tensor & other ) const ;
'''''''''''


**参数**
'''''''''''
	- **other** (const Tensor&)

**返回**
'''''''''''
Tensor
Tensor operator> ( const Tensor & other ) const ;
'''''''''''


**参数**
'''''''''''
	- **other** (const Tensor&)

**返回**
'''''''''''
Tensor
Tensor operator> = ( const Tensor & other ) const ;
'''''''''''


**参数**
'''''''''''
	- **other** (const Tensor&)

**返回**
'''''''''''
Tensor
Tensor operator - ( ) const ;
'''''''''''



**返回**
'''''''''''
Tensor
Tensor operator ~ ( ) const ;
'''''''''''



**返回**
'''''''''''
Tensor
Tensor operator & ( const Tensor & other ) const ;
'''''''''''


**参数**
'''''''''''
	- **other** (const Tensor&)

**返回**
'''''''''''
Tensor
Tensor operator | ( const Tensor & other ) const ;
'''''''''''


**参数**
'''''''''''
	- **other** (const Tensor&)

**返回**
'''''''''''
Tensor
Tensor operator ^ ( const Tensor & other ) const ;
'''''''''''


**参数**
'''''''''''
	- **other** (const Tensor&)

**返回**
'''''''''''
Tensor
AbstractAutogradMeta * get_autograd_meta ( ) const ;
'''''''''''
Get the autograd meta object pointer 


**返回**
'''''''''''
AbstractAutogradMeta*

const std::shared_ptr<AbstractAutogradMeta> & mutable_autograd_meta ( ) const ;
'''''''''''
Get the shared pointer of autograd meta object 


**返回**
'''''''''''
std::shared_ptr<AbstractAutogradMeta>&

void set_autograd_meta ( std::shared_ptr<AbstractAutogradMeta> autograd_meta ) ;
'''''''''''
Set the autograd meta object 

**参数**
'''''''''''
	- **autograd_meta** (std::shared_ptr<AbstractAutogradMeta >) - autograd_meta


void bump_inplace_version ( ) ;
'''''''''''
Increase inplace version



uint32_t current_inplace_version ( ) ;
'''''''''''
Get current inplace version 


**返回**
'''''''''''
uint32_t

void reset_inplace_version ( bool set_to_zero = false ) ;
'''''''''''
Reset inplace version


**参数**
'''''''''''
	- **set_to_zero** (bool)

Tensor to_sparse_coo ( const int64_t sparse_dim ) const ;
'''''''''''
Convert DenseTensor or SparseCsrTensor to SparseCooTensor 

**参数**
'''''''''''
	- **sparse_dim** (const int64_t)

**返回**
'''''''''''
Tensor

Tensor to_sparse_csr ( ) const ;
'''''''''''
Convert DenseTensor or SparseCooTensor to SparseCsrTensor 


**返回**
'''''''''''
Tensor

Tensor to_dense ( ) const ;
'''''''''''
Convert SparseCooTensor or SparseCsrTensor to DenseTensor 


**返回**
'''''''''''
Tensor

Tensor add ( const Tensor & y ) const ;
'''''''''''


**参数**
'''''''''''
	- **y** (const Tensor&)

**返回**
'''''''''''
Tensor
Tensor divide ( const Tensor & y ) const ;
'''''''''''


**参数**
'''''''''''
	- **y** (const Tensor&)

**返回**
'''''''''''
Tensor
Tensor multiply ( const Tensor & y ) const ;
'''''''''''


**参数**
'''''''''''
	- **y** (const Tensor&)

**返回**
'''''''''''
Tensor
Tensor subtract ( const Tensor & y ) const ;
'''''''''''


**参数**
'''''''''''
	- **y** (const Tensor&)

**返回**
'''''''''''
Tensor
Tensor add ( const Scalar & y ) const ;
'''''''''''


**参数**
'''''''''''
	- **y** (Scalar&)

**返回**
'''''''''''
Tensor
Tensor divide ( const Scalar & y ) const ;
'''''''''''


**参数**
'''''''''''
	- **y** (Scalar&)

**返回**
'''''''''''
Tensor
Tensor multiply ( const Scalar & y ) const ;
'''''''''''


**参数**
'''''''''''
	- **y** (Scalar&)

**返回**
'''''''''''
Tensor
Tensor subtract ( const Scalar & y ) const ;
'''''''''''


**参数**
'''''''''''
	- **y** (Scalar&)

**返回**
'''''''''''
Tensor
Tensor less_equal ( const Tensor & y ) const ;
'''''''''''


**参数**
'''''''''''
	- **y** (const Tensor&)

**返回**
'''''''''''
Tensor
Tensor less_than ( const Tensor & y ) const ;
'''''''''''


**参数**
'''''''''''
	- **y** (const Tensor&)

**返回**
'''''''''''
Tensor
Tensor equal ( const Tensor & y ) const ;
'''''''''''


**参数**
'''''''''''
	- **y** (const Tensor&)

**返回**
'''''''''''
Tensor
Tensor not_equal ( const Tensor & y ) const ;
'''''''''''


**参数**
'''''''''''
	- **y** (const Tensor&)

**返回**
'''''''''''
Tensor
Tensor greater_equal ( const Tensor & y ) const ;
'''''''''''


**参数**
'''''''''''
	- **y** (const Tensor&)

**返回**
'''''''''''
Tensor
Tensor greater_than ( const Tensor & y ) const ;
'''''''''''


**参数**
'''''''''''
	- **y** (const Tensor&)

**返回**
'''''''''''
Tensor
Tensor bitwise_and ( const Tensor & y ) const ;
'''''''''''


**参数**
'''''''''''
	- **y** (const Tensor&)

**返回**
'''''''''''
Tensor
Tensor bitwise_or ( const Tensor & y ) const ;
'''''''''''


**参数**
'''''''''''
	- **y** (const Tensor&)

**返回**
'''''''''''
Tensor
Tensor bitwise_xor ( const Tensor & y ) const ;
'''''''''''


**参数**
'''''''''''
	- **y** (const Tensor&)

**返回**
'''''''''''
Tensor
Tensor bitwise_not ( ) const ;
'''''''''''



**返回**
'''''''''''
Tensor
Tensor pow ( const Tensor & y ) const ;
'''''''''''


**参数**
'''''''''''
	- **y** (const Tensor&)

**返回**
'''''''''''
Tensor
Tensor pow ( const Scalar & y ) const ;
'''''''''''


**参数**
'''''''''''
	- **y** (Scalar&)

**返回**
'''''''''''
Tensor
Tensor exp ( ) const ;
'''''''''''



**返回**
'''''''''''
Tensor
Tensor floor ( ) const ;
'''''''''''



**返回**
'''''''''''
Tensor
Tensor gather_nd ( const Tensor & index ) const ;
'''''''''''


**参数**
'''''''''''
	- **index** (const Tensor&)

**返回**
'''''''''''
Tensor
Tensor log ( ) const ;
'''''''''''



**返回**
'''''''''''
Tensor
Tensor roll ( const IntArray & shifts = { } , const std::vector<int64_t> & axis = { } ) const ;
'''''''''''


**参数**
'''''''''''
	- **shifts** (IntArray&)
	- **axis** (const std::vector<int64_t>&)

**返回**
'''''''''''
Tensor
Tensor scatter ( const Tensor & index , const Tensor & updates , bool overwrite = true ) const ;
'''''''''''


**参数**
'''''''''''
	- **index** (const Tensor&)
	- **updates** (const Tensor&)
	- **overwrite** (bool)

**返回**
'''''''''''
Tensor
Tensor scatter_nd_add ( const Tensor & index , const Tensor & updates ) const ;
'''''''''''


**参数**
'''''''''''
	- **index** (const Tensor&)
	- **updates** (const Tensor&)

**返回**
'''''''''''
Tensor
Tensor abs ( ) const ;
'''''''''''



**返回**
'''''''''''
Tensor
Tensor assign ( ) const ;
'''''''''''



**返回**
'''''''''''
Tensor
Tensor elementwise_pow ( const Tensor & y ) const ;
'''''''''''


**参数**
'''''''''''
	- **y** (const Tensor&)

**返回**
'''''''''''
Tensor
Tensor expand ( const IntArray & shape ) const ;
'''''''''''


**参数**
'''''''''''
	- **shape** (IntArray&)

**返回**
'''''''''''
Tensor
Tensor matmul ( const Tensor & y , bool transpose_x = false , bool transpose_y = false ) const ;
'''''''''''


**参数**
'''''''''''
	- **y** (const Tensor&)
	- **transpose_x** (bool)
	- **transpose_y** (bool)

**返回**
'''''''''''
Tensor
Tensor max ( const IntArray & axis = { } , bool keepdim = false ) const ;
'''''''''''


**参数**
'''''''''''
	- **axis** (IntArray&)
	- **keepdim** (bool)

**返回**
'''''''''''
Tensor
Tensor maximum ( const Tensor & y ) const ;
'''''''''''


**参数**
'''''''''''
	- **y** (const Tensor&)

**返回**
'''''''''''
Tensor
Tensor minimum ( const Tensor & y ) const ;
'''''''''''


**参数**
'''''''''''
	- **y** (const Tensor&)

**返回**
'''''''''''
Tensor
Tensor scale ( const Scalar & scale = 1.0 , float bias = 0.0 , bool bias_after_scale = true ) const ;
'''''''''''


**参数**
'''''''''''
	- **scale** (Scalar&)
	- **bias** (float)
	- **bias_after_scale** (bool)

**返回**
'''''''''''
Tensor
Tensor sum ( const IntArray & axis = { } , DataType dtype = DataType::UNDEFINED , bool keepdim = false ) const ;
'''''''''''


**参数**
'''''''''''
	- **axis** (IntArray&)
	- **dtype** (DataType)
	- **keepdim** (bool)

**返回**
'''''''''''
Tensor
Tensor tile ( const IntArray & repeat_times = { } ) const ;
'''''''''''


**参数**
'''''''''''
	- **repeat_times** (IntArray&)

**返回**
'''''''''''
Tensor
