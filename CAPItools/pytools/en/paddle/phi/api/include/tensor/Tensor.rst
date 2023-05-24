.. _en_api_Tensor:

Tensor[source](https://github.com/PaddlePaddle/Paddle/blob/develop/paddle\phi\api\include\tensor.h)
-------------------------------

.. cpp:class:: Tensor ( std::shared_ptr<phi::TensorBase> tensor_impl , const std::string & name ) ;


Path
:::::::::::::::::::::
paddle\phi\api\include\tensor.h

Methods
:::::::::::::::::::::

Tensor ( ) = default ;
'''''''''''
Construct a new Tensor object



Tensor ( const Tensor & ) = default ;
'''''''''''
Construct a new Tensor object by copy


**Parameters**
'''''''''''
	- **&** (const Tensor)

Tensor ( Tensor & & ) = default ;
'''''''''''
Construct a new Tensor object by move


**Parameters**
'''''''''''
	- **&** (Tensor&)

explicit Tensor ( std::shared_ptr<phi::TensorBase> tensor_impl ) ;
'''''''''''
Construct a new Tensor object by a TensorBase pointer 

**Parameters**
'''''''''''
	- **tensor_impl** (std::shared_ptr<phi::TensorBase >) - tensor_impl


explicit Tensor ( const Place & place ) ;
'''''''''''
Construct a new Tensor object on the target place. This is a deprecated method and may be removed in the future!!! 

**Parameters**
'''''''''''
	- **place** (const Place&) - place


Tensor ( const Place & place , const std::vector<int64_t> & shape ) ;
'''''''''''
Construct a new Tensor object on the target place with specified shape. This is a deprecated method and may be removed in the future!!! 

**Parameters**
'''''''''''
	- **place** (const Place&)
	- **shape** (const std::vector<int64_t>&) - shape


Tensor ( std::shared_ptr<phi::TensorBase> tensor_impl , const std::string & name ) ;
'''''''''''
Construct a new Tensor object by a TensorBase pointer and name 

**Parameters**
'''''''''''
	- **tensor_impl** (std::shared_ptr<phi::TensorBase >) - tensor_impl

	- **name** (const std::string&)

explicit Tensor ( const std::string & name ) :
'''''''''''
Construct a new Tensor object with name 

..note::
	Internal method, used to adapt original execution mechanism and debug analysis in the development of new dygraph. It may be removed in the future. 

**Parameters**
'''''''''''
	- **name** (const std::string&)

int64_t numel ( ) const ;
'''''''''''
Return the number of elements of Tensor. 


**Returns**
'''''''''''
int64_t

int64_t size ( ) const ;
'''''''''''
Get the size of current tensor. The compatible method of `Tensor::numel()`. This is a deprecated method and may be removed in the future! 


**Returns**
'''''''''''
int64_t

const phi::DDim & dims ( ) const ;
'''''''''''
Return the dimensions of Tensor. 


**Returns**
'''''''''''
phi::DDim

std::vector<int64_t> shape ( ) const ;
'''''''''''
Return the shape (dimensions) of Tensor. The compatible method of `Tensor::dims()`. This is a deprecated method and may be removed in the future! 


**Returns**
'''''''''''
std::vector<int64_t>

void reshape ( const std::vector<int64_t> & shape ) ;
'''''''''''
Reset the shape of the tensor. 

**Parameters**
'''''''''''
	- **shape** (const std::vector<int64_t>&) - shape


DataType dtype ( ) const ;
'''''''''''
Return the data type of Tensor. 


**Returns**
'''''''''''
DataType

DataType type ( ) const ;
'''''''''''
Return the data type of Tensor. The compatible method of `Tensor::dtype()`. This is a deprecated method and may be removed in the future! 


**Returns**
'''''''''''
DataType

phi::DataLayout layout ( ) const ;
'''''''''''
Return the layout of Tensor. 


**Returns**
'''''''''''
DataLayout

bool is_dense_tensor ( ) const ;
'''''''''''
Determine whether tensor is DenseTensor 


**Returns**
'''''''''''
false

bool is_selected_rows ( ) const ;
'''''''''''
Determine whether tensor is SelectedRows 


**Returns**
'''''''''''
false

bool is_sparse_coo_tensor ( ) const ;
'''''''''''
Determine whether tensor is SparseCooTensor 


**Returns**
'''''''''''
false

bool is_sparse_csr_tensor ( ) const ;
'''''''''''
Determine whether tensor is SparseCsrTensor 


**Returns**
'''''''''''
false

bool is_string_tensor ( ) const ;
'''''''''''
Determine whether tensor is StringTensor 


**Returns**
'''''''''''
false

const Place & place ( ) const ;
'''''''''''
Return the place (device) of Tensor. 


**Returns**
'''''''''''
Place

bool is_cpu ( ) const ;
'''''''''''
Determine whether the tensor device is CPU 


**Returns**
'''''''''''
false

bool is_gpu ( ) const ;
'''''''''''
Determine whether the tensor device is GPU 


**Returns**
'''''''''''
false

bool is_gpu_pinned ( ) const ;
'''''''''''
Determine whether the tensor device is GPU_PINNED 


**Returns**
'''''''''''
false

bool is_xpu ( ) const ;
'''''''''''
Determine whether the tensor device is XPU 


**Returns**
'''''''''''
false

bool is_custom_device ( ) const ;
'''''''''''
Determine whether the tensor device is CustomDevice 


**Returns**
'''''''''''
false

T * mutable_data ( ) ;
'''''''''''
Get the memory pointer in CPU or GPU with specific data type. It's usually used to get the output data pointer, same as the T* data(). 


**Returns**
'''''''''''
T*

T * mutable_data ( const Place & place ) ;
'''''''''''
Get the memory pointer in CPU or GPU with specific data type. It's usually used to get the output data pointer. This is a deprecated method and may be removed in the future! 

**Parameters**
'''''''''''
	- **place** (const Place&)

**Returns**
'''''''''''
T*

const T * data ( ) const ;
'''''''''''
Get the const memory pointer directly. It's usually used to get the output data pointer. 


**Returns**
'''''''''''
T*

T * data ( ) ;
'''''''''''
Get the memory pointer directly. It's usually used to get the mutable output data pointer. 


**Returns**
'''''''''''
T*

const void * data ( ) const ;
'''''''''''
Get the const memory pointer directly. It's usually used to get the output data pointer. 


**Returns**
'''''''''''
T*

void * data ( ) ;
'''''''''''
Get the memory pointer directly. It's usually used to get the mutable output data pointer. 


**Returns**
'''''''''''
T*

Tensor slice ( int64_t begin_idx , int64_t end_idx ) const ;
'''''''''''
Return a sub-tensor of the given tensor. It is usually used to extract a sub-tensor (which supports modifying the data of the original tensor) to perform further operations. 

**Parameters**
'''''''''''
	- **begin_idx** (int64_t) - The index of the start row (inclusive) to slice.The index number begins from 0. 
	- **end_idx** (int64_t) - The index of the end row (exclusive) to slice. The index number begins from begin_idx + 1. 

**Returns**
'''''''''''
Tensor

const std::shared_ptr<phi::TensorBase> & impl ( ) const ;
'''''''''''
Return the implementation of current Tensor. 


**Returns**
'''''''''''
std::shared_ptr<phi::TensorBase>

void set_impl ( const std::shared_ptr<phi::TensorBase> & impl ) ;
'''''''''''
Set the implementation of current Tensor. 

**Parameters**
'''''''''''
	- **impl** (const std::shared_ptr<phi::TensorBase>&) - impl


void set_impl ( std::shared_ptr<phi::TensorBase> & & impl ) ;
'''''''''''
Set the implementation of current Tensor. 

**Parameters**
'''''''''''
	- **impl** (std::shared_ptr<phi::TensorBase>) - impl


gpuStream_t stream ( ) const ;
'''''''''''
Get the stream where the tensor is currently located This is a deprecated method and may be removed in the future! 


**Returns**
'''''''''''
gpuStream_t

const std::string & name ( ) const {
'''''''''''
Return the name of Tensor. 

..note::
	Used to adapt original execution mechanism and debug analysis in the development of new dygraph. 


**Returns**
'''''''''''
const std::string&

void set_name ( const std::string & name ) {
'''''''''''
Set name of Tensor. 

..note::
	Used to adapt original execution mechanism and debug analysis in the development of new dygraph. 

**Parameters**
'''''''''''
	- **name** (const std::string&)

Tensor copy_to ( const Place & target_place ) const ;
'''''''''''
Copy the current Tensor data to the specified device and return the new Tensor. It's usually used to set the input tensor data. 

..note::
	The Tensor's `copy_to` method is deprecated since version 2.3, and will be removed in version 2.4, please use `copy_to` method without template argument instead. reason: copying a Tensor to another device does not need to specify the data type template argument 

**Parameters**
'''''''''''
	- **target_place** (const Place&)

**Returns**
'''''''''''
Tensor

Tensor copy_to ( const Place & place , bool blocking ) const ;
'''''''''''
Transfer the current Tensor to the specified device and return. 

**Parameters**
'''''''''''
	- **place** (const Place&)
	- **blocking** (bool)

**Returns**
'''''''''''
Tensor

void copy_ ( const Tensor & src , const Place & target_place , bool blocking ) ;
'''''''''''
Transfer the source Tensor to current Tensor. 

**Parameters**
'''''''''''
	- **src** (const Tensor&)
	- **target_place** (const Place&)
	- **blocking** (bool)

Tensor cast ( DataType target_type ) const ;
'''''''''''
Cast datatype from one to another 

**Parameters**
'''''''''''
	- **target_type** (DataType)

**Returns**
'''''''''''
Tensor

bool defined ( ) const ;
'''''''''''
Determine whether it is a meaningful Tensor 


**Returns**
'''''''''''
false

bool initialized ( ) const ;
'''''''''''
Determine whether Tensor is initialized. 


**Returns**
'''''''''''
false

bool is_initialized ( ) const ;
'''''''''''
Determine whether Tensor is initialized. This is a deprecated method and may be removed in the future! 


**Returns**
'''''''''''
false

void reset ( ) ;
'''''''''''
Reset the Tensor implementation



Tensor & operator = ( const Tensor & x ) & ;
'''''''''''
Assignment operator 

**Parameters**
'''''''''''
	- **x** (const Tensor&)

**Returns**
'''''''''''
Tensor&

Tensor & operator = ( Tensor & & x ) & ;
'''''''''''
Move assignment operator 

**Parameters**
'''''''''''
	- **x** (Tensor)

**Returns**
'''''''''''
Tensor&

Tensor operator + ( const Tensor & other ) const ;
'''''''''''
Tensor operants 

**Parameters**
'''''''''''
	- **other** (const Tensor&)

**Returns**
'''''''''''
Tensor

Tensor operator - ( const Tensor & other ) const ;
'''''''''''


**Parameters**
'''''''''''
	- **other** (const Tensor&)

**Returns**
'''''''''''
Tensor
Tensor operator * ( const Tensor & other ) const ;
'''''''''''


**Parameters**
'''''''''''
	- **other** (const Tensor&)

**Returns**
'''''''''''
Tensor
Tensor operator / ( const Tensor & other ) const ;
'''''''''''


**Parameters**
'''''''''''
	- **other** (const Tensor&)

**Returns**
'''''''''''
Tensor
Tensor operator + ( const Scalar & other ) const ;
'''''''''''


**Parameters**
'''''''''''
	- **other** (const Scalar&)

**Returns**
'''''''''''
Tensor
Tensor operator - ( const Scalar & other ) const ;
'''''''''''


**Parameters**
'''''''''''
	- **other** (const Scalar&)

**Returns**
'''''''''''
Tensor
Tensor operator * ( const Scalar & other ) const ;
'''''''''''


**Parameters**
'''''''''''
	- **other** (const Scalar&)

**Returns**
'''''''''''
Tensor
Tensor operator / ( const Scalar & other ) const ;
'''''''''''


**Parameters**
'''''''''''
	- **other** (const Scalar&)

**Returns**
'''''''''''
Tensor
Tensor operator<( const Tensor & other ) const ;
'''''''''''


**Parameters**
'''''''''''
	- **other** (const Tensor&)

**Returns**
'''''''''''
Tensor
Tensor operator<= ( const Tensor & other ) const ;
'''''''''''


**Parameters**
'''''''''''
	- **other** (const Tensor&)

**Returns**
'''''''''''
Tensor
Tensor operator = = ( const Tensor & other ) const ;
'''''''''''


**Parameters**
'''''''''''
	- **other** (const Tensor&)

**Returns**
'''''''''''
Tensor
Tensor operator ! = ( const Tensor & other ) const ;
'''''''''''


**Parameters**
'''''''''''
	- **other** (const Tensor&)

**Returns**
'''''''''''
Tensor
Tensor operator> ( const Tensor & other ) const ;
'''''''''''


**Parameters**
'''''''''''
	- **other** (const Tensor&)

**Returns**
'''''''''''
Tensor
Tensor operator> = ( const Tensor & other ) const ;
'''''''''''


**Parameters**
'''''''''''
	- **other** (const Tensor&)

**Returns**
'''''''''''
Tensor
Tensor operator - ( ) const ;
'''''''''''



**Returns**
'''''''''''
Tensor
Tensor operator ~ ( ) const ;
'''''''''''



**Returns**
'''''''''''
Tensor
Tensor operator & ( const Tensor & other ) const ;
'''''''''''


**Parameters**
'''''''''''
	- **other** (const Tensor&)

**Returns**
'''''''''''
Tensor
Tensor operator | ( const Tensor & other ) const ;
'''''''''''


**Parameters**
'''''''''''
	- **other** (const Tensor&)

**Returns**
'''''''''''
Tensor
Tensor operator ^ ( const Tensor & other ) const ;
'''''''''''


**Parameters**
'''''''''''
	- **other** (const Tensor&)

**Returns**
'''''''''''
Tensor
AbstractAutogradMeta * get_autograd_meta ( ) const ;
'''''''''''
Get the autograd meta object pointer 


**Returns**
'''''''''''
AbstractAutogradMeta*

const std::shared_ptr<AbstractAutogradMeta> & mutable_autograd_meta ( ) const ;
'''''''''''
Get the shared pointer of autograd meta object 


**Returns**
'''''''''''
std::shared_ptr<AbstractAutogradMeta>&

void set_autograd_meta ( std::shared_ptr<AbstractAutogradMeta> autograd_meta ) ;
'''''''''''
Set the autograd meta object 

**Parameters**
'''''''''''
	- **autograd_meta** (std::shared_ptr<AbstractAutogradMeta >) - autograd_meta


void bump_inplace_version ( ) ;
'''''''''''
Increase inplace version



uint32_t current_inplace_version ( ) ;
'''''''''''
Get current inplace version 


**Returns**
'''''''''''
uint32_t

void reset_inplace_version ( bool set_to_zero = false ) ;
'''''''''''
Reset inplace version


**Parameters**
'''''''''''
	- **set_to_zero** (bool)

Tensor to_sparse_coo ( const int64_t sparse_dim ) const ;
'''''''''''
Convert DenseTensor or SparseCsrTensor to SparseCooTensor 

**Parameters**
'''''''''''
	- **sparse_dim** (const int64_t)

**Returns**
'''''''''''
Tensor

Tensor to_sparse_csr ( ) const ;
'''''''''''
Convert DenseTensor or SparseCooTensor to SparseCsrTensor 


**Returns**
'''''''''''
Tensor

Tensor to_dense ( ) const ;
'''''''''''
Convert SparseCooTensor or SparseCsrTensor to DenseTensor 


**Returns**
'''''''''''
Tensor

Tensor add ( const Tensor & y ) const ;
'''''''''''


**Parameters**
'''''''''''
	- **y** (const Tensor&)

**Returns**
'''''''''''
Tensor
Tensor divide ( const Tensor & y ) const ;
'''''''''''


**Parameters**
'''''''''''
	- **y** (const Tensor&)

**Returns**
'''''''''''
Tensor
Tensor multiply ( const Tensor & y ) const ;
'''''''''''


**Parameters**
'''''''''''
	- **y** (const Tensor&)

**Returns**
'''''''''''
Tensor
Tensor subtract ( const Tensor & y ) const ;
'''''''''''


**Parameters**
'''''''''''
	- **y** (const Tensor&)

**Returns**
'''''''''''
Tensor
Tensor add ( const Scalar & y ) const ;
'''''''''''


**Parameters**
'''''''''''
	- **y** (const Scalar&)

**Returns**
'''''''''''
Tensor
Tensor divide ( const Scalar & y ) const ;
'''''''''''


**Parameters**
'''''''''''
	- **y** (const Scalar&)

**Returns**
'''''''''''
Tensor
Tensor multiply ( const Scalar & y ) const ;
'''''''''''


**Parameters**
'''''''''''
	- **y** (const Scalar&)

**Returns**
'''''''''''
Tensor
Tensor subtract ( const Scalar & y ) const ;
'''''''''''


**Parameters**
'''''''''''
	- **y** (const Scalar&)

**Returns**
'''''''''''
Tensor
Tensor less_equal ( const Tensor & y ) const ;
'''''''''''


**Parameters**
'''''''''''
	- **y** (const Tensor&)

**Returns**
'''''''''''
Tensor
Tensor less_than ( const Tensor & y ) const ;
'''''''''''


**Parameters**
'''''''''''
	- **y** (const Tensor&)

**Returns**
'''''''''''
Tensor
Tensor equal ( const Tensor & y ) const ;
'''''''''''


**Parameters**
'''''''''''
	- **y** (const Tensor&)

**Returns**
'''''''''''
Tensor
Tensor not_equal ( const Tensor & y ) const ;
'''''''''''


**Parameters**
'''''''''''
	- **y** (const Tensor&)

**Returns**
'''''''''''
Tensor
Tensor greater_equal ( const Tensor & y ) const ;
'''''''''''


**Parameters**
'''''''''''
	- **y** (const Tensor&)

**Returns**
'''''''''''
Tensor
Tensor greater_than ( const Tensor & y ) const ;
'''''''''''


**Parameters**
'''''''''''
	- **y** (const Tensor&)

**Returns**
'''''''''''
Tensor
Tensor bitwise_and ( const Tensor & y ) const ;
'''''''''''


**Parameters**
'''''''''''
	- **y** (const Tensor&)

**Returns**
'''''''''''
Tensor
Tensor bitwise_or ( const Tensor & y ) const ;
'''''''''''


**Parameters**
'''''''''''
	- **y** (const Tensor&)

**Returns**
'''''''''''
Tensor
Tensor bitwise_xor ( const Tensor & y ) const ;
'''''''''''


**Parameters**
'''''''''''
	- **y** (const Tensor&)

**Returns**
'''''''''''
Tensor
Tensor bitwise_not ( ) const ;
'''''''''''



**Returns**
'''''''''''
Tensor
Tensor pow ( const Tensor & y ) const ;
'''''''''''


**Parameters**
'''''''''''
	- **y** (const Tensor&)

**Returns**
'''''''''''
Tensor
Tensor pow ( const Scalar & y ) const ;
'''''''''''


**Parameters**
'''''''''''
	- **y** (const Scalar&)

**Returns**
'''''''''''
Tensor
Tensor exp ( ) const ;
'''''''''''



**Returns**
'''''''''''
Tensor
Tensor floor ( ) const ;
'''''''''''



**Returns**
'''''''''''
Tensor
Tensor gather_nd ( const Tensor & index ) const ;
'''''''''''


**Parameters**
'''''''''''
	- **index** (const Tensor&)

**Returns**
'''''''''''
Tensor
Tensor log ( ) const ;
'''''''''''



**Returns**
'''''''''''
Tensor
Tensor roll ( const IntArray & shifts = { } , const std::vector<int64_t> & axis = { } ) const ;
'''''''''''


**Parameters**
'''''''''''
	- **shifts** (const IntArray&)
	- **axis** (const std::vector<int64_t>&)

**Returns**
'''''''''''
Tensor
Tensor scatter ( const Tensor & index , const Tensor & updates , bool overwrite = true ) const ;
'''''''''''


**Parameters**
'''''''''''
	- **index** (const Tensor&)
	- **updates** (const Tensor&)
	- **overwrite** (bool)

**Returns**
'''''''''''
Tensor
Tensor scatter_nd_add ( const Tensor & index , const Tensor & updates ) const ;
'''''''''''


**Parameters**
'''''''''''
	- **index** (const Tensor&)
	- **updates** (const Tensor&)

**Returns**
'''''''''''
Tensor
Tensor abs ( ) const ;
'''''''''''



**Returns**
'''''''''''
Tensor
Tensor assign ( ) const ;
'''''''''''



**Returns**
'''''''''''
Tensor
Tensor elementwise_pow ( const Tensor & y ) const ;
'''''''''''


**Parameters**
'''''''''''
	- **y** (const Tensor&)

**Returns**
'''''''''''
Tensor
Tensor expand ( const IntArray & shape ) const ;
'''''''''''


**Parameters**
'''''''''''
	- **shape** (const IntArray&)

**Returns**
'''''''''''
Tensor
Tensor matmul ( const Tensor & y , bool transpose_x = false , bool transpose_y = false ) const ;
'''''''''''


**Parameters**
'''''''''''
	- **y** (const Tensor&)
	- **transpose_x** (bool)
	- **transpose_y** (bool)

**Returns**
'''''''''''
Tensor
Tensor max ( const IntArray & axis = { } , bool keepdim = false ) const ;
'''''''''''


**Parameters**
'''''''''''
	- **axis** (const IntArray&)
	- **keepdim** (bool)

**Returns**
'''''''''''
Tensor
Tensor maximum ( const Tensor & y ) const ;
'''''''''''


**Parameters**
'''''''''''
	- **y** (const Tensor&)

**Returns**
'''''''''''
Tensor
Tensor minimum ( const Tensor & y ) const ;
'''''''''''


**Parameters**
'''''''''''
	- **y** (const Tensor&)

**Returns**
'''''''''''
Tensor
Tensor scale ( const Scalar & scale = 1.0 , float bias = 0.0 , bool bias_after_scale = true ) const ;
'''''''''''


**Parameters**
'''''''''''
	- **scale** (const Scalar&)
	- **bias** (float)
	- **bias_after_scale** (bool)

**Returns**
'''''''''''
Tensor
Tensor sum ( const IntArray & axis = { } , DataType dtype = DataType::UNDEFINED , bool keepdim = false ) const ;
'''''''''''


**Parameters**
'''''''''''
	- **axis** (const IntArray&)
	- **dtype** (DataType)
	- **keepdim** (bool)

**Returns**
'''''''''''
Tensor
Tensor tile ( const IntArray & repeat_times = { } ) const ;
'''''''''''


**Parameters**
'''''''''''
	- **repeat_times** (const IntArray&)

**Returns**
'''''''''''
Tensor
