.. _cn_api_CustomOpKernelContext:

CustomOpKernelContext[源代码](https://github.com/PaddlePaddle/Paddle/blob/develop/paddle\phi\api\ext\op_meta_info.h)
-------------------------------

.. cpp:class:: CustomOpKernelContext ( ) = default ;

<name="desc">

</name>

定义目录
:::::::::::::::::::::
paddle\phi\api\ext\op_meta_info.h

方法
:::::::::::::::::::::
CustomOpKernelContext ( ) = default ;
'''''''''
<name="desc">

</name>


返回
:::::::::::::::::::::
无

void EmplaceBackInput ( Tensor & & input ) ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **input** (Tensor) - 

返回
:::::::::::::::::::::
void

void EmplaceBackInputs ( const std::vector<Tensor> & inputs ) ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **inputs** (const std::vector<Tensor>&) - 

返回
:::::::::::::::::::::
void

void EmplaceBackOutput ( Tensor & & output ) ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **output** (Tensor) - 

返回
:::::::::::::::::::::
void

void EmplaceBackOutputs ( const std::vector<Tensor> & outputs ) ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **outputs** (const std::vector<Tensor>&) - 

返回
:::::::::::::::::::::
void

void EmplaceBackAttr ( paddle::any attr ) ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **attr** (paddle::any) - 

返回
:::::::::::::::::::::
void

void EmplaceBackAttrs ( const std::vector<paddle::any> & attrs ) {
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **attrs** (const std::vector<paddle::any>&) - 

返回
:::::::::::::::::::::
void

const std::pair<size_t , size_t> & InputRangeAt ( size_t idx ) const ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **idx** (size_t) - 

返回
:::::::::::::::::::::
std::pair<size_t , size_t>

const std::pair<size_t , size_t> & OutputRangeAt ( size_t idx ) const ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **idx** (size_t) - 

返回
:::::::::::::::::::::
std::pair<size_t , size_t>

const Tensor & InputAt ( size_t idx ) const ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **idx** (size_t) - 

返回
:::::::::::::::::::::
Tensor

std::vector<Tensor> InputsBetween ( size_t start , size_t end ) const ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **start** (size_t) - 
	- **end** (size_t) - 

返回
:::::::::::::::::::::
std::vector<Tensor>

Tensor & MutableInputAt ( size_t idx ) ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **idx** (size_t) - 

返回
:::::::::::::::::::::
Tensor

std::vector<Tensor> * AllMutableInput ( ) ;
'''''''''
<name="desc">

</name>


返回
:::::::::::::::::::::
std::vector<Tensor>

paddle::optional<Tensor> OptionalInputAt ( size_t idx ) ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **idx** (size_t) - 

返回
:::::::::::::::::::::
paddle::optional<Tensor>

paddle::optional<std::vector<Tensor> > OptionalInputsBetween ( size_t start , size_t end ) ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **start** (size_t) - 
	- **end** (size_t) - 

返回
:::::::::::::::::::::
paddle::optional<std::vector<Tensor> >

const std::vector<paddle::any> & Attrs ( ) const {
'''''''''
<name="desc">

</name>


返回
:::::::::::::::::::::
std::vector<paddle::any>

const std::vector<std::pair<size_t , size_t> > & InputRange ( ) {
'''''''''
<name="desc">

</name>


返回
:::::::::::::::::::::
std::vector<std::pair<size_t , size_t> >

const std::vector<std::pair<size_t , size_t> > & OutputRange ( ) {
'''''''''
<name="desc">

</name>


返回
:::::::::::::::::::::
std::vector<std::pair<size_t , size_t> >

Tensor * MutableOutputAt ( size_t idx ) ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **idx** (size_t) - 

返回
:::::::::::::::::::::
Tensor

std::vector<Tensor *> MutableOutputBetweeen ( size_t start , size_t end ) ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **start** (size_t) - 
	- **end** (size_t) - 

返回
:::::::::::::::::::::
std::vector<Tensor *>

std::vector<Tensor> OutputsBetweeen ( size_t start , size_t end ) ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **start** (size_t) - 
	- **end** (size_t) - 

返回
:::::::::::::::::::::
std::vector<Tensor>

std::vector<Tensor> * AllMutableOutput ( ) ;
'''''''''
<name="desc">

</name>


返回
:::::::::::::::::::::
std::vector<Tensor>

AttrType AttrAt ( size_t idx ) const {
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **idx** (size_t) - 

返回
:::::::::::::::::::::
AttrType

void ConstructInplaceIndex ( const std::vector<std::string> & inputs , const std::vector<std::string> & outputs , const std::unordered_map<std::string , std::string> & inplace_map ) ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **inputs** (const std::vector<std::string>&) - 
	- **outputs** (const std::vector<std::string>&) - 
	- **inplace_map** (const std::unordered_map<std::string, std::string>&) - 

返回
:::::::::::::::::::::
void

void UpdatePlainOutputs ( const std::vector<std::string> & inputs , const std::vector<std::string> & outputs , const std::unordered_map<std::string , std::string> & inplace_map ) ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **inputs** (const std::vector<std::string>&) - 
	- **outputs** (const std::vector<std::string>&) - 
	- **inplace_map** (const std::unordered_map<std::string, std::string>&) - 

返回
:::::::::::::::::::::
void

void AssignInplaceOutputs ( ) ;
'''''''''
<name="desc">

</name>


返回
:::::::::::::::::::::
void

std::vector<Tensor *> * AllMutablePlainOutput ( ) ;
'''''''''
<name="desc">

</name>


返回
:::::::::::::::::::::
std::vector<Tensor >

std::unordered_map<size_t , size_t> GetInplaceIndexMap ( ) ;
'''''''''
<name="desc">

</name>


返回
:::::::::::::::::::::
std::unordered_map<size_t , size_t>

std::unordered_map<size_t , size_t> GetInplaceReverseIndexMap ( ) ;
'''''''''
<name="desc">

</name>


返回
:::::::::::::::::::::
std::unordered_map<size_t , size_t>



<name="reference_link">

</name>

