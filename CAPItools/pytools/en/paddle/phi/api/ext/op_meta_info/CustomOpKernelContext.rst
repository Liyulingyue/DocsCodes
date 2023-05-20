.. _en_api_CustomOpKernelContext:

CustomOpKernelContext[source](https://github.com/PaddlePaddle/Paddle/blob/develop/paddle\phi\api\ext\op_meta_info.h)
-------------------------------

.. cpp:class:: CustomOpKernelContext ( ) = default ;


Path
:::::::::::::::::::::
paddle\phi\api\ext\op_meta_info.h

Methods
:::::::::::::::::::::

CustomOpKernelContext ( ) = default ;
'''''''''''



void EmplaceBackInput ( Tensor & & input ) ;
'''''''''''


**Parameters**
'''''''''''
	- **input** (Tensor)

void EmplaceBackInputs ( const std::vector<Tensor> & inputs ) ;
'''''''''''


**Parameters**
'''''''''''
	- **inputs** (const std::vector<Tensor>&)

void EmplaceBackOutput ( Tensor & & output ) ;
'''''''''''


**Parameters**
'''''''''''
	- **output** (Tensor)

void EmplaceBackOutputs ( const std::vector<Tensor> & outputs ) ;
'''''''''''


**Parameters**
'''''''''''
	- **outputs** (const std::vector<Tensor>&)

void EmplaceBackAttr ( paddle::any attr ) ;
'''''''''''


**Parameters**
'''''''''''
	- **attr** (paddle::any)

void EmplaceBackAttrs ( const std::vector<paddle::any> & attrs ) {
'''''''''''


**Parameters**
'''''''''''
	- **attrs** (const std::vector<paddle::any>&)

const std::pair<size_t , size_t> & InputRangeAt ( size_t idx ) const ;
'''''''''''


**Parameters**
'''''''''''
	- **idx** (size_t)

**Returns**
'''''''''''
std::pair<size_t , size_t>
const std::pair<size_t , size_t> & OutputRangeAt ( size_t idx ) const ;
'''''''''''


**Parameters**
'''''''''''
	- **idx** (size_t)

**Returns**
'''''''''''
std::pair<size_t , size_t>
const Tensor & InputAt ( size_t idx ) const ;
'''''''''''


**Parameters**
'''''''''''
	- **idx** (size_t)

**Returns**
'''''''''''
Tensor
std::vector<Tensor> InputsBetween ( size_t start , size_t end ) const ;
'''''''''''


**Parameters**
'''''''''''
	- **start** (size_t)
	- **end** (size_t)

**Returns**
'''''''''''
std::vector<Tensor>
Tensor & MutableInputAt ( size_t idx ) ;
'''''''''''


**Parameters**
'''''''''''
	- **idx** (size_t)

**Returns**
'''''''''''
Tensor
std::vector<Tensor> * AllMutableInput ( ) ;
'''''''''''



**Returns**
'''''''''''
std::vector<Tensor>
paddle::optional<Tensor> OptionalInputAt ( size_t idx ) ;
'''''''''''


**Parameters**
'''''''''''
	- **idx** (size_t)

**Returns**
'''''''''''
paddle::optional<Tensor>
paddle::optional<std::vector<Tensor> > OptionalInputsBetween ( size_t start , size_t end ) ;
'''''''''''


**Parameters**
'''''''''''
	- **start** (size_t)
	- **end** (size_t)

**Returns**
'''''''''''
paddle::optional<std::vector<Tensor> >
const std::vector<paddle::any> & Attrs ( ) const {
'''''''''''



**Returns**
'''''''''''
std::vector<paddle::any>
const std::vector<std::pair<size_t , size_t> > & InputRange ( ) {
'''''''''''



**Returns**
'''''''''''
std::vector<std::pair<size_t , size_t> >
const std::vector<std::pair<size_t , size_t> > & OutputRange ( ) {
'''''''''''



**Returns**
'''''''''''
std::vector<std::pair<size_t , size_t> >
Tensor * MutableOutputAt ( size_t idx ) ;
'''''''''''


**Parameters**
'''''''''''
	- **idx** (size_t)

**Returns**
'''''''''''
Tensor
std::vector<Tensor *> MutableOutputBetweeen ( size_t start , size_t end ) ;
'''''''''''


**Parameters**
'''''''''''
	- **start** (size_t)
	- **end** (size_t)

**Returns**
'''''''''''
std::vector<Tensor *>
std::vector<Tensor> OutputsBetweeen ( size_t start , size_t end ) ;
'''''''''''


**Parameters**
'''''''''''
	- **start** (size_t)
	- **end** (size_t)

**Returns**
'''''''''''
std::vector<Tensor>
std::vector<Tensor> * AllMutableOutput ( ) ;
'''''''''''



**Returns**
'''''''''''
std::vector<Tensor>
AttrType AttrAt ( size_t idx ) const {
'''''''''''


**Parameters**
'''''''''''
	- **idx** (size_t)

**Returns**
'''''''''''
AttrType
void ConstructInplaceIndex ( const std::vector<std::string> & inputs , const std::vector<std::string> & outputs , const std::unordered_map<std::string , std::string> & inplace_map ) ;
'''''''''''


**Parameters**
'''''''''''
	- **inputs** (const std::vector<std::string>&)
	- **outputs** (const std::vector<std::string>&)
	- **inplace_map** (const std::unordered_map<std::string, std::string>&)

void UpdatePlainOutputs ( const std::vector<std::string> & inputs , const std::vector<std::string> & outputs , const std::unordered_map<std::string , std::string> & inplace_map ) ;
'''''''''''


**Parameters**
'''''''''''
	- **inputs** (const std::vector<std::string>&)
	- **outputs** (const std::vector<std::string>&)
	- **inplace_map** (const std::unordered_map<std::string, std::string>&)

void AssignInplaceOutputs ( ) ;
'''''''''''



std::vector<Tensor *> * AllMutablePlainOutput ( ) ;
'''''''''''



**Returns**
'''''''''''
std::vector<Tensor >
std::unordered_map<size_t , size_t> GetInplaceIndexMap ( ) ;
'''''''''''



**Returns**
'''''''''''
std::unordered_map<size_t , size_t>
std::unordered_map<size_t , size_t> GetInplaceReverseIndexMap ( ) ;
'''''''''''



**Returns**
'''''''''''
std::unordered_map<size_t , size_t>
