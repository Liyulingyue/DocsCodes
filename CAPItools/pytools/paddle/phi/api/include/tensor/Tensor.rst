.. _cn_api_Tensor:

Tensor[源代码](https://github.com/PaddlePaddle/Paddle/blob/develop/paddle\phi\api\include\tensor.h)
-------------------------------

.. cpp:class:: Tensor ( std::shared_ptr<phi::TensorBase> tensor_impl , const std::string & name ) ;

<name="desc">

</name>

定义目录
:::::::::::::::::::::
paddle\phi\api\include\tensor.h

方法
:::::::::::::::::::::
Tensor ( ) = default ;
'''''''''
<name="desc">
 @brief Construct a new Tensor object

</name>


返回
:::::::::::::::::::::
无

Tensor ( const Tensor & ) = default ;
'''''''''
<name="desc">
 @brief Construct a new Tensor object by copy

</name>


参数
:::::::::::::::::::::
	- **&** (const Tensor) - 

返回
:::::::::::::::::::::
无

Tensor ( Tensor & & ) = default ;
'''''''''
<name="desc">
 @brief Construct a new Tensor object by move

</name>


参数
:::::::::::::::::::::
	- **&** (Tensor&) - 

返回
:::::::::::::::::::::
无

explicit Tensor ( std::shared_ptr<phi::TensorBase> tensor_impl ) ;
'''''''''
<name="desc">
 @brief Construct a new Tensor object by a TensorBase pointer @param tensor_impl

</name>


参数
:::::::::::::::::::::
	- **tensor_impl** (std::shared_ptr<phi::TensorBase >) - 

返回
:::::::::::::::::::::
无

explicit Tensor ( const Place & place ) ;
'''''''''
<name="desc">
 @brief Construct a new Tensor object on the target place. This is a deprecated method and may be removed in the future!!! @param place

</name>


参数
:::::::::::::::::::::
	- **place** (const Place&) - 

返回
:::::::::::::::::::::
无

Tensor ( const Place & place , const std::vector<int64_t> & shape ) ;
'''''''''
<name="desc">
 @brief Construct a new Tensor object on the target place with specified shape. This is a deprecated method and may be removed in the future!!! @param place @param shape

</name>


参数
:::::::::::::::::::::
	- **place** (const Place&) - 
	- **shape** (const std::vector<int64_t>&) - 

返回
:::::::::::::::::::::
无

Tensor ( std::shared_ptr<phi::TensorBase> tensor_impl , const std::string & name ) ;
'''''''''
<name="desc">
 @brief Construct a new Tensor object by a TensorBase pointer and name @param tensor_impl

</name>


参数
:::::::::::::::::::::
	- **tensor_impl** (std::shared_ptr<phi::TensorBase >) - 
	- **name** (const std::string&) - 

返回
:::::::::::::::::::::
无

explicit Tensor ( const std::string & name ) :
'''''''''
<name="desc">
 @brief Construct a new Tensor object with name @note Internal method, used to adapt original execution mechanism and debug analysis in the development of new dygraph. It may be removed in the future. 
</name>


参数
:::::::::::::::::::::
	- **name** (const std::string&) - 

返回
:::::::::::::::::::::
无

int64_t numel ( ) const ;
'''''''''
<name="desc">
 @brief Return the number of elements of Tensor. @return int64_t

</name>


返回
:::::::::::::::::::::
int64_t

int64_t size ( ) const ;
'''''''''
<name="desc">
 @brief Get the size of current tensor. The compatible method of `Tensor::numel()`. This is a deprecated method and may be removed in the future! @return int64_t

</name>


返回
:::::::::::::::::::::
int64_t

const phi::DDim & dims ( ) const ;
'''''''''
<name="desc">
 @brief Return the dimensions of Tensor. @return phi::DDim

</name>


返回
:::::::::::::::::::::
phi::DDim

std::vector<int64_t> shape ( ) const ;
'''''''''
<name="desc">
 @brief Return the shape (dimensions) of Tensor. The compatible method of `Tensor::dims()`. This is a deprecated method and may be removed in the future! @return std::vector<int64_t>

</name>


返回
:::::::::::::::::::::
std::vector<int64_t>

void reshape ( const std::vector<int64_t> & shape ) ;
'''''''''
<name="desc">
 @brief Reset the shape of the tensor. @note: This method means Reset the shape of the tensor, and must be called before calling mutable_data() or copy_to(const Place& place), this is not a standard definition of reshape behavior, so we will deprecated this feature in the future. @param shape

</name>


参数
:::::::::::::::::::::
	- **shape** (const std::vector<int64_t>&) - 

返回
:::::::::::::::::::::
void

DataType dtype ( ) const ;
'''''''''
<name="desc">
 @brief Return the data type of Tensor. @return DataType

</name>


返回
:::::::::::::::::::::
DataType

DataType type ( ) const ;
'''''''''
<name="desc">
 @brief Return the data type of Tensor. The compatible method of `Tensor::dtype()`. This is a deprecated method and may be removed in the future! @return DataType

</name>


返回
:::::::::::::::::::::
DataType

phi::DataLayout layout ( ) const ;
'''''''''
<name="desc">
 @brief Return the layout of Tensor. @return DataLayout

</name>


返回
:::::::::::::::::::::
phi::DataLayout

bool is_dense_tensor ( ) const ;
'''''''''
<name="desc">
 @brief Determine whether tensor is DenseTensor @return true @return false

</name>


返回
:::::::::::::::::::::
bool

bool is_selected_rows ( ) const ;
'''''''''
<name="desc">
 @brief Determine whether tensor is SelectedRows @return true @return false

</name>


返回
:::::::::::::::::::::
bool

bool is_sparse_coo_tensor ( ) const ;
'''''''''
<name="desc">
 @brief Determine whether tensor is SparseCooTensor @return true @return false

</name>


返回
:::::::::::::::::::::
bool

bool is_sparse_csr_tensor ( ) const ;
'''''''''
<name="desc">
 @brief Determine whether tensor is SparseCsrTensor @return true @return false

</name>


返回
:::::::::::::::::::::
bool

bool is_string_tensor ( ) const ;
'''''''''
<name="desc">
 @brief Determine whether tensor is StringTensor @return true @return false

</name>


返回
:::::::::::::::::::::
bool

const Place & place ( ) const ;
'''''''''
<name="desc">
 @brief Return the place (device) of Tensor. @return Place

</name>


返回
:::::::::::::::::::::
Place

bool is_cpu ( ) const ;
'''''''''
<name="desc">
 @brief Determine whether the tensor device is CPU @return true @return false

</name>


返回
:::::::::::::::::::::
bool

bool is_gpu ( ) const ;
'''''''''
<name="desc">
 @brief Determine whether the tensor device is GPU @return true @return false

</name>


返回
:::::::::::::::::::::
bool

bool is_gpu_pinned ( ) const ;
'''''''''
<name="desc">
 @brief Determine whether the tensor device is GPU_PINNED @return true @return false

</name>


返回
:::::::::::::::::::::
bool

bool is_xpu ( ) const ;
'''''''''
<name="desc">
 @brief Determine whether the tensor device is XPU @return true @return false

</name>


返回
:::::::::::::::::::::
bool

bool is_custom_device ( ) const ;
'''''''''
<name="desc">
 @brief Determine whether the tensor device is CustomDevice @return true @return false

</name>


返回
:::::::::::::::::::::
bool

T * mutable_data ( ) ;
'''''''''
<name="desc">
 @brief Get the memory pointer in CPU or GPU with specific data type. It's usually used to get the output data pointer, same as the T* data(). @tparam T @return T*

</name>


返回
:::::::::::::::::::::
T

T * mutable_data ( const Place & place ) ;
'''''''''
<name="desc">
 @brief Get the memory pointer in CPU or GPU with specific data type. It's usually used to get the output data pointer. This is a deprecated method and may be removed in the future! @tparam T @param place @return T*

</name>


参数
:::::::::::::::::::::
	- **place** (const Place&) - 

返回
:::::::::::::::::::::
T

const T * data ( ) const ;
'''''''''
<name="desc">
 @brief Get the const memory pointer directly. It's usually used to get the output data pointer. @tparam T @return T*

</name>


返回
:::::::::::::::::::::
T

T * data ( ) ;
'''''''''
<name="desc">
 @brief Get the memory pointer directly. It's usually used to get the mutable output data pointer. @tparam T @return T*

</name>


返回
:::::::::::::::::::::
T

const void * data ( ) const ;
'''''''''
<name="desc">
 @brief Get the const memory pointer directly. It's usually used to get the output data pointer. @tparam T @return T*

</name>


返回
:::::::::::::::::::::
void

void * data ( ) ;
'''''''''
<name="desc">
 @brief Get the memory pointer directly. It's usually used to get the mutable output data pointer. @tparam T @return T*

</name>


返回
:::::::::::::::::::::
void

Tensor slice ( int64_t begin_idx , int64_t end_idx ) const ;
'''''''''
<name="desc">
 @brief Return a sub-tensor of the given tensor. It is usually used to extract a sub-tensor (which supports modifying the data of the original tensor) to perform further operations. @param begin_idx The index of the start row (inclusive) to slice.The index number begins from 0. @param end_idx The index of the end row (exclusive) to slice. The index number begins from begin_idx + 1. @return Tensor

</name>


参数
:::::::::::::::::::::
	- **begin_idx** (int64_t) - The index of the start row (inclusive) to slice.The index number begins from 0.
	- **end_idx** (int64_t) - The index of the end row (exclusive) to slice. The index number begins from begin_idx + 1.

返回
:::::::::::::::::::::
Tensor

const std::shared_ptr<phi::TensorBase> & impl ( ) const ;
'''''''''
<name="desc">
 @brief Return the implementation of current Tensor. @return std::shared_ptr<phi::TensorBase>

</name>


返回
:::::::::::::::::::::
std::shared_ptr<phi::TensorBase>

void set_impl ( const std::shared_ptr<phi::TensorBase> & impl ) ;
'''''''''
<name="desc">
 @brief Set the implementation of current Tensor. @param impl

</name>


参数
:::::::::::::::::::::
	- **impl** (const std::shared_ptr<phi::TensorBase>&) - 

返回
:::::::::::::::::::::
void

void set_impl ( std::shared_ptr<phi::TensorBase> & & impl ) ;
'''''''''
<name="desc">
 @brief Set the implementation of current Tensor. @param impl

</name>


参数
:::::::::::::::::::::
	- **impl** (std::shared_ptr<phi::TensorBase>) - 

返回
:::::::::::::::::::::
void

gpuStream_t stream ( ) const ;
'''''''''
<name="desc">
 @brief Get the stream where the tensor is currently located This is a deprecated method and may be removed in the future! @return gpuStream_t

</name>


返回
:::::::::::::::::::::
gpuStream_t

const std::string & name ( ) const {
'''''''''
<name="desc">
 @brief Return the name of Tensor. @note Used to adapt original execution mechanism and debug analysis in the development of new dygraph. @return const std::string&

</name>


返回
:::::::::::::::::::::
std::string

void set_name ( const std::string & name ) {
'''''''''
<name="desc">
 @brief Set name of Tensor. @note Used to adapt original execution mechanism and debug analysis in the development of new dygraph. @param const std::string& name

</name>


参数
:::::::::::::::::::::
	- **name** (const std::string&) - 

返回
:::::::::::::::::::::
void

Tensor copy_to ( const Place & target_place ) const ;
'''''''''
<name="desc">
 @brief Copy the current Tensor data to the specified device and return the new Tensor. It's usually used to set the input tensor data. @note The Tensor's `copy_to` method is deprecated since version 2.3, and will be removed in version 2.4, please use `copy_to` method without template argument instead. reason: copying a Tensor to another device does not need to specify the data type template argument @tparam T @param target_place, the target place of which the tensor will copy to. @return Tensor

</name>


参数
:::::::::::::::::::::
	- **target_place** (const Place&) - 

返回
:::::::::::::::::::::
Tensor

Tensor copy_to ( const Place & place , bool blocking ) const ;
'''''''''
<name="desc">
 @brief Transfer the current Tensor to the specified device and return. @param place, The target place of which the tensor will copy to. @param blocking, Should we copy this in sync way. @return Tensor

</name>


参数
:::::::::::::::::::::
	- **place** (const Place&) - 
	- **blocking** (bool) - 

返回
:::::::::::::::::::::
Tensor

void copy_ ( const Tensor & src , const Place & target_place , bool blocking ) ;
'''''''''
<name="desc">
 @brief Transfer the source Tensor to current Tensor. @param src, the source Tensor to be copied. @param blocking, Should we copy this in sync way. @return void

</name>


参数
:::::::::::::::::::::
	- **src** (const Tensor&) - 
	- **target_place** (const Place&) - 
	- **blocking** (bool) - 

返回
:::::::::::::::::::::
void

Tensor cast ( DataType target_type ) const ;
'''''''''
<name="desc">
 @brief Cast datatype from one to another @param target_type @return Tensor

</name>


参数
:::::::::::::::::::::
	- **target_type** (DataType) - 

返回
:::::::::::::::::::::
Tensor

bool defined ( ) const ;
'''''''''
<name="desc">
 @brief Determine whether it is a meaningful Tensor @return true @return false

</name>


返回
:::::::::::::::::::::
bool

bool initialized ( ) const ;
'''''''''
<name="desc">
 @brief Determine whether Tensor is initialized. @return true @return false

</name>


返回
:::::::::::::::::::::
bool

bool is_initialized ( ) const ;
'''''''''
<name="desc">
 @brief Determine whether Tensor is initialized. This is a deprecated method and may be removed in the future! @return true @return false

</name>


返回
:::::::::::::::::::::
bool

void reset ( ) ;
'''''''''
<name="desc">
 @brief Reset the Tensor implementation

</name>


返回
:::::::::::::::::::::
void

Tensor & operator = ( const Tensor & x ) & ;
'''''''''
<name="desc">
 @brief Assignment operator @param x @return Tensor&

</name>


参数
:::::::::::::::::::::
	- **x** (const Tensor&) - 

返回
:::::::::::::::::::::
Tensor

Tensor & operator = ( Tensor & & x ) & ;
'''''''''
<name="desc">
 @brief Move assignment operator @param x @return Tensor&

</name>


参数
:::::::::::::::::::::
	- **x** (Tensor) - 

返回
:::::::::::::::::::::
Tensor

Tensor operator + ( const Tensor & other ) const ;
'''''''''
<name="desc">
 @brief Tensor operants @param other @return Tensor

</name>


参数
:::::::::::::::::::::
	- **other** (const Tensor&) - 

返回
:::::::::::::::::::::
Tensor

Tensor operator - ( const Tensor & other ) const ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **other** (const Tensor&) - 

返回
:::::::::::::::::::::
Tensor

Tensor operator * ( const Tensor & other ) const ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **other** (const Tensor&) - 

返回
:::::::::::::::::::::
Tensor

Tensor operator / ( const Tensor & other ) const ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **other** (const Tensor&) - 

返回
:::::::::::::::::::::
Tensor

Tensor operator + ( const Scalar & other ) const ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **other** (Scalar&) - 

返回
:::::::::::::::::::::
Tensor

Tensor operator - ( const Scalar & other ) const ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **other** (Scalar&) - 

返回
:::::::::::::::::::::
Tensor

Tensor operator * ( const Scalar & other ) const ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **other** (Scalar&) - 

返回
:::::::::::::::::::::
Tensor

Tensor operator / ( const Scalar & other ) const ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **other** (Scalar&) - 

返回
:::::::::::::::::::::
Tensor

Tensor operator<( const Tensor & other ) const ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **other** (const Tensor&) - 

返回
:::::::::::::::::::::
Tensor

Tensor operator<= ( const Tensor & other ) const ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **other** (const Tensor&) - 

返回
:::::::::::::::::::::
Tensor

Tensor operator = = ( const Tensor & other ) const ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **other** (const Tensor&) - 

返回
:::::::::::::::::::::
Tensor

Tensor operator ! = ( const Tensor & other ) const ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **other** (const Tensor&) - 

返回
:::::::::::::::::::::
Tensor

Tensor operator> ( const Tensor & other ) const ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **other** (const Tensor&) - 

返回
:::::::::::::::::::::
Tensor

Tensor operator> = ( const Tensor & other ) const ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **other** (const Tensor&) - 

返回
:::::::::::::::::::::
Tensor

Tensor operator - ( ) const ;
'''''''''
<name="desc">

</name>


返回
:::::::::::::::::::::
Tensor

Tensor operator ~ ( ) const ;
'''''''''
<name="desc">

</name>


返回
:::::::::::::::::::::
Tensor

Tensor operator & ( const Tensor & other ) const ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **other** (const Tensor&) - 

返回
:::::::::::::::::::::
Tensor

Tensor operator | ( const Tensor & other ) const ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **other** (const Tensor&) - 

返回
:::::::::::::::::::::
Tensor

Tensor operator ^ ( const Tensor & other ) const ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **other** (const Tensor&) - 

返回
:::::::::::::::::::::
Tensor

AbstractAutogradMeta * get_autograd_meta ( ) const ;
'''''''''
<name="desc">
 @brief Get the autograd meta object pointer @return AbstractAutogradMeta*

</name>


返回
:::::::::::::::::::::
AbstractAutogradMeta

const std::shared_ptr<AbstractAutogradMeta> & mutable_autograd_meta ( ) const ;
'''''''''
<name="desc">
 @brief Get the shared pointer of autograd meta object @return std::shared_ptr<AbstractAutogradMeta>&

</name>


返回
:::::::::::::::::::::
std::shared_ptr<AbstractAutogradMeta>

void set_autograd_meta ( std::shared_ptr<AbstractAutogradMeta> autograd_meta ) ;
'''''''''
<name="desc">
 @brief Set the autograd meta object @param autograd_meta

</name>


参数
:::::::::::::::::::::
	- **autograd_meta** (std::shared_ptr<AbstractAutogradMeta >) - 

返回
:::::::::::::::::::::
void

void bump_inplace_version ( ) ;
'''''''''
<name="desc">
 @brief Increase inplace version

</name>


返回
:::::::::::::::::::::
void

uint32_t current_inplace_version ( ) ;
'''''''''
<name="desc">
 @brief Get current inplace version @return uint32_t

</name>


返回
:::::::::::::::::::::
uint32_t

void reset_inplace_version ( bool set_to_zero = false ) ;
'''''''''
<name="desc">
 @brief Reset inplace version

</name>


参数
:::::::::::::::::::::
	- **set_to_zero** (bool) - 

返回
:::::::::::::::::::::
void

Tensor to_sparse_coo ( const int64_t sparse_dim ) const ;
'''''''''
<name="desc">
 @brief Convert DenseTensor or SparseCsrTensor to SparseCooTensor @param sparse_dim, The number of sparse dimensions @return Tensor

</name>


参数
:::::::::::::::::::::
	- **sparse_dim** (const int64_t) - 

返回
:::::::::::::::::::::
Tensor

Tensor to_sparse_csr ( ) const ;
'''''''''
<name="desc">
 @brief Convert DenseTensor or SparseCooTensor to SparseCsrTensor @return Tensor

</name>


返回
:::::::::::::::::::::
Tensor

Tensor to_dense ( ) const ;
'''''''''
<name="desc">
 @brief Convert SparseCooTensor or SparseCsrTensor to DenseTensor @return Tensor

</name>


返回
:::::::::::::::::::::
Tensor

Tensor add ( const Tensor & y ) const ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **y** (const Tensor&) - 

返回
:::::::::::::::::::::
Tensor

Tensor divide ( const Tensor & y ) const ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **y** (const Tensor&) - 

返回
:::::::::::::::::::::
Tensor

Tensor multiply ( const Tensor & y ) const ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **y** (const Tensor&) - 

返回
:::::::::::::::::::::
Tensor

Tensor subtract ( const Tensor & y ) const ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **y** (const Tensor&) - 

返回
:::::::::::::::::::::
Tensor

Tensor add ( const Scalar & y ) const ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **y** (Scalar&) - 

返回
:::::::::::::::::::::
Tensor

Tensor divide ( const Scalar & y ) const ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **y** (Scalar&) - 

返回
:::::::::::::::::::::
Tensor

Tensor multiply ( const Scalar & y ) const ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **y** (Scalar&) - 

返回
:::::::::::::::::::::
Tensor

Tensor subtract ( const Scalar & y ) const ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **y** (Scalar&) - 

返回
:::::::::::::::::::::
Tensor

Tensor less_equal ( const Tensor & y ) const ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **y** (const Tensor&) - 

返回
:::::::::::::::::::::
Tensor

Tensor less_than ( const Tensor & y ) const ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **y** (const Tensor&) - 

返回
:::::::::::::::::::::
Tensor

Tensor equal ( const Tensor & y ) const ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **y** (const Tensor&) - 

返回
:::::::::::::::::::::
Tensor

Tensor not_equal ( const Tensor & y ) const ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **y** (const Tensor&) - 

返回
:::::::::::::::::::::
Tensor

Tensor greater_equal ( const Tensor & y ) const ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **y** (const Tensor&) - 

返回
:::::::::::::::::::::
Tensor

Tensor greater_than ( const Tensor & y ) const ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **y** (const Tensor&) - 

返回
:::::::::::::::::::::
Tensor

Tensor bitwise_and ( const Tensor & y ) const ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **y** (const Tensor&) - 

返回
:::::::::::::::::::::
Tensor

Tensor bitwise_or ( const Tensor & y ) const ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **y** (const Tensor&) - 

返回
:::::::::::::::::::::
Tensor

Tensor bitwise_xor ( const Tensor & y ) const ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **y** (const Tensor&) - 

返回
:::::::::::::::::::::
Tensor

Tensor bitwise_not ( ) const ;
'''''''''
<name="desc">

</name>


返回
:::::::::::::::::::::
Tensor

Tensor pow ( const Tensor & y ) const ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **y** (const Tensor&) - 

返回
:::::::::::::::::::::
Tensor

Tensor pow ( const Scalar & y ) const ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **y** (Scalar&) - 

返回
:::::::::::::::::::::
Tensor

Tensor exp ( ) const ;
'''''''''
<name="desc">

</name>


返回
:::::::::::::::::::::
Tensor

Tensor floor ( ) const ;
'''''''''
<name="desc">

</name>


返回
:::::::::::::::::::::
Tensor

Tensor gather_nd ( const Tensor & index ) const ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **index** (const Tensor&) - 

返回
:::::::::::::::::::::
Tensor

Tensor log ( ) const ;
'''''''''
<name="desc">

</name>


返回
:::::::::::::::::::::
Tensor

Tensor roll ( const IntArray & shifts = { } , const std::vector<int64_t> & axis = { } ) const ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **shifts** (IntArray&) - 
	- **axis** (const std::vector<int64_t>&) - 

返回
:::::::::::::::::::::
Tensor

Tensor scatter ( const Tensor & index , const Tensor & updates , bool overwrite = true ) const ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **index** (const Tensor&) - 
	- **updates** (const Tensor&) - 
	- **overwrite** (bool) - 

返回
:::::::::::::::::::::
Tensor

Tensor scatter_nd_add ( const Tensor & index , const Tensor & updates ) const ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **index** (const Tensor&) - 
	- **updates** (const Tensor&) - 

返回
:::::::::::::::::::::
Tensor

Tensor abs ( ) const ;
'''''''''
<name="desc">

</name>


返回
:::::::::::::::::::::
Tensor

Tensor assign ( ) const ;
'''''''''
<name="desc">

</name>


返回
:::::::::::::::::::::
Tensor

Tensor elementwise_pow ( const Tensor & y ) const ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **y** (const Tensor&) - 

返回
:::::::::::::::::::::
Tensor

Tensor expand ( const IntArray & shape ) const ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **shape** (IntArray&) - 

返回
:::::::::::::::::::::
Tensor

Tensor matmul ( const Tensor & y , bool transpose_x = false , bool transpose_y = false ) const ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **y** (const Tensor&) - 
	- **transpose_x** (bool) - 
	- **transpose_y** (bool) - 

返回
:::::::::::::::::::::
Tensor

Tensor max ( const IntArray & axis = { } , bool keepdim = false ) const ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **axis** (IntArray&) - 
	- **keepdim** (bool) - 

返回
:::::::::::::::::::::
Tensor

Tensor maximum ( const Tensor & y ) const ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **y** (const Tensor&) - 

返回
:::::::::::::::::::::
Tensor

Tensor minimum ( const Tensor & y ) const ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **y** (const Tensor&) - 

返回
:::::::::::::::::::::
Tensor

Tensor scale ( const Scalar & scale = 1.0 , float bias = 0.0 , bool bias_after_scale = true ) const ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **scale** (Scalar&) - 
	- **bias** (float) - 
	- **bias_after_scale** (bool) - 

返回
:::::::::::::::::::::
Tensor

Tensor sum ( const IntArray & axis = { } , DataType dtype = DataType::UNDEFINED , bool keepdim = false ) const ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **axis** (IntArray&) - 
	- **dtype** (DataType) - 
	- **keepdim** (bool) - 

返回
:::::::::::::::::::::
Tensor

Tensor tile ( const IntArray & repeat_times = { } ) const ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **repeat_times** (IntArray&) - 

返回
:::::::::::::::::::::
Tensor



<name="reference_link">

</name>

