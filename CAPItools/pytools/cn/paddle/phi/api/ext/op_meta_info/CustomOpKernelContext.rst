.. _cn_api_CustomOpKernelContext:

CustomOpKernelContext[源代码](https://github.com/PaddlePaddle/Paddle/blob/develop/paddle\phi\api\ext\op_meta_info.h)
-------------------------------

.. cpp:class:: CustomOpKernelContext


定义目录
:::::::::::::::::::::
paddle\phi\api\ext\op_meta_info.h

方法
:::::::::::::::::::::

CustomOpKernelContext ( ) = default ;
'''''''''''



void EmplaceBackInput ( Tensor & & input ) ;
'''''''''''


**参数**
'''''''''''
	- **input** (Tensor&&)

void EmplaceBackInputs ( const std::vector<Tensor> & inputs ) ;
'''''''''''


**参数**
'''''''''''
	- **inputs** (const std::vector<Tensor>&)

void EmplaceBackOutput ( Tensor & & output ) ;
'''''''''''


**参数**
'''''''''''
	- **output** (Tensor&&)

void EmplaceBackOutputs ( const std::vector<Tensor> & outputs ) ;
'''''''''''


**参数**
'''''''''''
	- **outputs** (const std::vector<Tensor>&)

void EmplaceBackAttr ( paddle::any attr ) ;
'''''''''''


**参数**
'''''''''''
	- **attr** (paddle::any)

void EmplaceBackAttrs ( const std::vector<paddle::any> & attrs ) ;
'''''''''''


**参数**
'''''''''''
	- **attrs** (const std::vector<paddle::any>&)

const std::pair<size_t , size_t> & InputRangeAt ( size_t idx ) const ;
'''''''''''


**参数**
'''''''''''
	- **idx** (size_t)

**返回**
'''''''''''
const std::pair<size_t, size_t> &

const std::pair<size_t , size_t> & OutputRangeAt ( size_t idx ) const ;
'''''''''''


**参数**
'''''''''''
	- **idx** (size_t)

**返回**
'''''''''''
const std::pair<size_t, size_t> &

const Tensor & InputAt ( size_t idx ) const ;
'''''''''''


**参数**
'''''''''''
	- **idx** (size_t)

**返回**
'''''''''''
const Tensor &

std::vector<Tensor> InputsBetween ( size_t start , size_t end ) const ;
'''''''''''


**参数**
'''''''''''
	- **start** (size_t)
	- **end** (size_t)

**返回**
'''''''''''
std::vector<Tensor >

Tensor & MutableInputAt ( size_t idx ) ;
'''''''''''


**参数**
'''''''''''
	- **idx** (size_t)

**返回**
'''''''''''
Tensor &

std::vector<Tensor> * AllMutableInput ( ) ;
'''''''''''



**返回**
'''''''''''
std::vector<Tensor> *

paddle::optional<Tensor> OptionalInputAt ( size_t idx ) ;
'''''''''''


**参数**
'''''''''''
	- **idx** (size_t)

**返回**
'''''''''''
paddle::optional<Tensor >

paddle::optional<std::vector<Tensor> > OptionalInputsBetween ( size_t start , size_t end ) ;
'''''''''''


**参数**
'''''''''''
	- **start** (size_t)
	- **end** (size_t)

**返回**
'''''''''''
paddle::optional<std::vector<Tensor> >

const std::vector<paddle::any> & Attrs ( ) const ;
'''''''''''



**返回**
'''''''''''
const std::vector<paddle::any> &

const std::vector<std::pair<size_t , size_t> > & InputRange ( ) ;
'''''''''''



**返回**
'''''''''''
const std::vector<std::pair<size_t, size_t> > &

const std::vector<std::pair<size_t , size_t> > & OutputRange ( ) ;
'''''''''''



**返回**
'''''''''''
const std::vector<std::pair<size_t, size_t> > &

Tensor * MutableOutputAt ( size_t idx ) ;
'''''''''''


**参数**
'''''''''''
	- **idx** (size_t)

**返回**
'''''''''''
Tensor *

std::vector<Tensor *> MutableOutputBetween ( size_t start , size_t end ) ;
'''''''''''


**参数**
'''''''''''
	- **start** (size_t)
	- **end** (size_t)

**返回**
'''''''''''
std::vector<Tensor * >

std::vector<Tensor> OutputsBetween ( size_t start , size_t end ) ;
'''''''''''


**参数**
'''''''''''
	- **start** (size_t)
	- **end** (size_t)

**返回**
'''''''''''
std::vector<Tensor >

std::vector<Tensor> * AllMutableOutput ( ) ;
'''''''''''



**返回**
'''''''''''
std::vector<Tensor> *

template<typename AttrType>
AttrType AttrAt ( size_t idx ) const {
'''''''''''


**参数**
'''''''''''
	- **idx** (size_t)

**返回**
'''''''''''
AttrType

void ConstructInplaceIndex ( const std::vector<std::string> & inputs , const std::vector<std::string> & outputs , const std::unordered_map<std::string , std::string> & inplace_map ) ;
'''''''''''


**参数**
'''''''''''
	- **inputs** (const std::vector<std::string>&)
	- **outputs** (const std::vector<std::string>&)
	- **inplace_map** (const std::unordered_map<std::string, std::string>&)

void UpdatePlainOutputs ( const std::vector<std::string> & inputs , const std::vector<std::string> & outputs , const std::unordered_map<std::string , std::string> & inplace_map ) ;
'''''''''''


**参数**
'''''''''''
	- **inputs** (const std::vector<std::string>&)
	- **outputs** (const std::vector<std::string>&)
	- **inplace_map** (const std::unordered_map<std::string, std::string>&)

void AssignInplaceOutputs ( ) ;
'''''''''''



std::vector<Tensor *> * AllMutablePlainOutput ( ) ;
'''''''''''



**返回**
'''''''''''
std::vector<Tensor *> *

std::unordered_map<size_t , size_t> GetInplaceIndexMap ( ) ;
'''''''''''



**返回**
'''''''''''
std::unordered_map<size_t, size_t >

std::unordered_map<size_t , size_t> GetInplaceReverseIndexMap ( ) ;
'''''''''''



**返回**
'''''''''''
std::unordered_map<size_t, size_t >

