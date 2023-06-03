.. _cn_api_Place:

Place[源代码](https://github.com/PaddlePaddle/Paddle/blob/develop/paddle\phi\common\place.h)
-------------------------------

.. cpp:class:: Place
/// \brief The place is used to specify where the data is stored.

定义目录
:::::::::::::::::::::
paddle\phi\common\place.h

方法
:::::::::::::::::::::

Place ( ) :
'''''''''''



explicit Place ( AllocationType type , int8_t id , const std::string & dev_type = "" ) :
'''''''''''


**参数**
'''''''''''
	- **type** (AllocationType)
	- **id** (int8_t)
	- **dev_type** (const std::string&)

explicit Place ( AllocationType type , const std::string & dev_type = "" ) :
'''''''''''


**参数**
'''''''''''
	- **type** (AllocationType)
	- **dev_type** (const std::string&)

Place ( paddle::PlaceType type ) ;
'''''''''''


**参数**
'''''''''''
	- **type** (paddle::PlaceType)

void Reset ( AllocationType type , int8_t device_id = 0 , const std::string & dev_type = "" ) noexcept {
'''''''''''


**参数**
'''''''''''
	- **type** (AllocationType)
	- **device_id** (int8_t)
	- **dev_type** (const std::string&)

AllocationType GetType ( ) const {
'''''''''''



**返回**
'''''''''''
AllocationType

int8_t GetDeviceId ( ) const {
'''''''''''



**返回**
'''''''''''
int8_t

std::string GetDeviceType ( ) const {
'''''''''''



**返回**
'''''''''''
std::string

std::string DebugString ( ) const ;
'''''''''''



**返回**
'''''''''''
std::string

uint32_t HashValue ( ) const {
'''''''''''



**返回**
'''''''''''
uint32_t

inline bool operator = = ( const Place & rhs ) const {
'''''''''''


**参数**
'''''''''''
	- **rhs** (const Place&)

**返回**
'''''''''''
bool

inline bool operator ! = ( const Place & rhs ) const {
'''''''''''


**参数**
'''''''''''
	- **rhs** (const Place&)

**返回**
'''''''''''
bool

inline bool operator<( const Place & rhs ) const {
'''''''''''


**参数**
'''''''''''
	- **rhs** (const Place&)

**返回**
'''''''''''
bool

