.. _cn_api_Place:

Place[源代码](https://github.com/PaddlePaddle/Paddle/blob/develop/paddle\phi\common\place.h)
-------------------------------

.. cpp:class:: explicit Place ( AllocationType type , int8_t id , const std::string & dev_type = "" ) :

<name="desc">
/// \brief The place is used to specify where the data is stored.
</name>

定义目录
:::::::::::::::::::::
paddle\phi\common\place.h

方法
:::::::::::::::::::::
Place ( ) :
'''''''''
<name="desc">

</name>


返回
:::::::::::::::::::::
无

explicit Place ( AllocationType type , int8_t id , const std::string & dev_type = "" ) :
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **type** (AllocationType) - 
	- **id** (int8_t) - 
	- **dev_type** (const std::string&) - 

返回
:::::::::::::::::::::
无

explicit Place ( AllocationType type , const std::string & dev_type = "" ) :
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **type** (AllocationType) - 
	- **dev_type** (const std::string&) - 

返回
:::::::::::::::::::::
无

Place ( paddle::PlaceType type ) ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **type** (paddle::PlaceType) - 

返回
:::::::::::::::::::::
无

void Reset ( AllocationType type , int8_t device_id = 0 , const std::string & dev_type = "" ) noexcept {
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **type** (AllocationType) - 
	- **device_id** (int8_t) - 
	- **dev_type** (const std::string&) - 

返回
:::::::::::::::::::::
void

AllocationType GetType ( ) const {
'''''''''
<name="desc">

</name>


返回
:::::::::::::::::::::
int

int8_t GetDeviceId ( ) const {
'''''''''
<name="desc">

</name>


返回
:::::::::::::::::::::
int8_t

std::string GetDeviceType ( ) const {
'''''''''
<name="desc">

</name>


返回
:::::::::::::::::::::
std::string

std::string DebugString ( ) const ;
'''''''''
<name="desc">

</name>


返回
:::::::::::::::::::::
std::string

uint32_t HashValue ( ) const {
'''''''''
<name="desc">

</name>


返回
:::::::::::::::::::::
uint32_t

inline bool operator = = ( const Place & rhs ) const {
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **rhs** (const Place&) - 

返回
:::::::::::::::::::::
bool

inline bool operator ! = ( const Place & rhs ) const {
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **rhs** (const Place&) - 

返回
:::::::::::::::::::::
bool

inline bool operator<( const Place & rhs ) const {
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **rhs** (const Place&) - 

返回
:::::::::::::::::::::
bool



<name="reference_link">

</name>

