.. _cn_api_CustomOpKernelContext:

CustomOpKernelContext[Դ����](https://github.com/PaddlePaddle/Paddle/blob/develop/paddle\phi\api\ext\op_meta_info.h)
-------------------------------

.. cpp:class:: CustomOpKernelContext ( ) = default ;

<name="desc">

</name>

����Ŀ¼
:::::::::::::::::::::
paddle\phi\api\ext\op_meta_info.h

����
:::::::::::::::::::::
CustomOpKernelContext ( ) = default ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
��

void EmplaceBackInput ( Tensor & & input ) ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
	- **input** (Tensor) - 

����
:::::::::::::::::::::
void

void EmplaceBackInputs ( const std::vector<Tensor> & inputs ) ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
	- **inputs** (const std::vector<Tensor>&) - 

����
:::::::::::::::::::::
void

void EmplaceBackOutput ( Tensor & & output ) ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
	- **output** (Tensor) - 

����
:::::::::::::::::::::
void

void EmplaceBackOutputs ( const std::vector<Tensor> & outputs ) ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
	- **outputs** (const std::vector<Tensor>&) - 

����
:::::::::::::::::::::
void

void EmplaceBackAttr ( paddle::any attr ) ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
	- **attr** (paddle::any) - 

����
:::::::::::::::::::::
void

void EmplaceBackAttrs ( const std::vector<paddle::any> & attrs ) {
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
	- **attrs** (const std::vector<paddle::any>&) - 

����
:::::::::::::::::::::
void

const std::pair<size_t , size_t> & InputRangeAt ( size_t idx ) const ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
	- **idx** (size_t) - 

����
:::::::::::::::::::::
std::pair<size_t , size_t>

const std::pair<size_t , size_t> & OutputRangeAt ( size_t idx ) const ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
	- **idx** (size_t) - 

����
:::::::::::::::::::::
std::pair<size_t , size_t>

const Tensor & InputAt ( size_t idx ) const ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
	- **idx** (size_t) - 

����
:::::::::::::::::::::
Tensor

std::vector<Tensor> InputsBetween ( size_t start , size_t end ) const ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
	- **start** (size_t) - 
	- **end** (size_t) - 

����
:::::::::::::::::::::
std::vector<Tensor>

Tensor & MutableInputAt ( size_t idx ) ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
	- **idx** (size_t) - 

����
:::::::::::::::::::::
Tensor

std::vector<Tensor> * AllMutableInput ( ) ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
std::vector<Tensor>

paddle::optional<Tensor> OptionalInputAt ( size_t idx ) ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
	- **idx** (size_t) - 

����
:::::::::::::::::::::
paddle::optional<Tensor>

paddle::optional<std::vector<Tensor> > OptionalInputsBetween ( size_t start , size_t end ) ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
	- **start** (size_t) - 
	- **end** (size_t) - 

����
:::::::::::::::::::::
paddle::optional<std::vector<Tensor> >

const std::vector<paddle::any> & Attrs ( ) const {
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
std::vector<paddle::any>

const std::vector<std::pair<size_t , size_t> > & InputRange ( ) {
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
std::vector<std::pair<size_t , size_t> >

const std::vector<std::pair<size_t , size_t> > & OutputRange ( ) {
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
std::vector<std::pair<size_t , size_t> >

Tensor * MutableOutputAt ( size_t idx ) ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
	- **idx** (size_t) - 

����
:::::::::::::::::::::
Tensor

std::vector<Tensor *> MutableOutputBetweeen ( size_t start , size_t end ) ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
	- **start** (size_t) - 
	- **end** (size_t) - 

����
:::::::::::::::::::::
std::vector<Tensor *>

std::vector<Tensor> OutputsBetweeen ( size_t start , size_t end ) ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
	- **start** (size_t) - 
	- **end** (size_t) - 

����
:::::::::::::::::::::
std::vector<Tensor>

std::vector<Tensor> * AllMutableOutput ( ) ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
std::vector<Tensor>

AttrType AttrAt ( size_t idx ) const {
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
	- **idx** (size_t) - 

����
:::::::::::::::::::::
AttrType

void ConstructInplaceIndex ( const std::vector<std::string> & inputs , const std::vector<std::string> & outputs , const std::unordered_map<std::string , std::string> & inplace_map ) ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
	- **inputs** (const std::vector<std::string>&) - 
	- **outputs** (const std::vector<std::string>&) - 
	- **inplace_map** (const std::unordered_map<std::string, std::string>&) - 

����
:::::::::::::::::::::
void

void UpdatePlainOutputs ( const std::vector<std::string> & inputs , const std::vector<std::string> & outputs , const std::unordered_map<std::string , std::string> & inplace_map ) ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
	- **inputs** (const std::vector<std::string>&) - 
	- **outputs** (const std::vector<std::string>&) - 
	- **inplace_map** (const std::unordered_map<std::string, std::string>&) - 

����
:::::::::::::::::::::
void

void AssignInplaceOutputs ( ) ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
void

std::vector<Tensor *> * AllMutablePlainOutput ( ) ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
std::vector<Tensor >

std::unordered_map<size_t , size_t> GetInplaceIndexMap ( ) ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
std::unordered_map<size_t , size_t>

std::unordered_map<size_t , size_t> GetInplaceReverseIndexMap ( ) ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
std::unordered_map<size_t , size_t>



<name="reference_link">

</name>

