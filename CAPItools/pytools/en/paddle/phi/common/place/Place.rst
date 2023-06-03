.. _en_api_Place:

Place[source](https://github.com/PaddlePaddle/Paddle/blob/develop/paddle\phi\common\place.h)
-------------------------------

.. cpp:class:: explicit Place ( AllocationType type , int8_t id , const std::string & dev_type = "" ) :
/// \brief The place is used to specify where the data is stored.

Path
:::::::::::::::::::::
paddle\phi\common\place.h

Methods
:::::::::::::::::::::

Place ( ) :
'''''''''''



explicit Place ( AllocationType type , int8_t id , const std::string & dev_type = "" ) :
'''''''''''


**Parameters**
'''''''''''
	- **type** (AllocationType)
	- **id** (int8_t)
	- **dev_type** (const std::string&)

explicit Place ( AllocationType type , const std::string & dev_type = "" ) :
'''''''''''


**Parameters**
'''''''''''
	- **type** (AllocationType)
	- **dev_type** (const std::string&)

Place ( paddle::PlaceType type ) ;
'''''''''''


**Parameters**
'''''''''''
	- **type** (paddle::PlaceType)

void Reset ( AllocationType type , int8_t device_id = 0 , const std::string & dev_type = "" ) noexcept {
'''''''''''


**Parameters**
'''''''''''
	- **type** (AllocationType)
	- **device_id** (int8_t)
	- **dev_type** (const std::string&)

AllocationType GetType ( ) const {
'''''''''''



**Returns**
'''''''''''
AllocationType

int8_t GetDeviceId ( ) const {
'''''''''''



**Returns**
'''''''''''
int8_t

std::string GetDeviceType ( ) const {
'''''''''''



**Returns**
'''''''''''
std::string

std::string DebugString ( ) const ;
'''''''''''



**Returns**
'''''''''''
std::string

uint32_t HashValue ( ) const {
'''''''''''



**Returns**
'''''''''''
uint32_t

inline bool operator = = ( const Place & rhs ) const {
'''''''''''


**Parameters**
'''''''''''
	- **rhs** (const Place&)

**Returns**
'''''''''''
bool

inline bool operator ! = ( const Place & rhs ) const {
'''''''''''


**Parameters**
'''''''''''
	- **rhs** (const Place&)

**Returns**
'''''''''''
bool

inline bool operator<( const Place & rhs ) const {
'''''''''''


**Parameters**
'''''''''''
	- **rhs** (const Place&)

**Returns**
'''''''''''
bool

