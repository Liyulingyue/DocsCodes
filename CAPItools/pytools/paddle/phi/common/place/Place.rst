.. _cn_api_Place:

Place[Դ����](https://github.com/PaddlePaddle/Paddle/blob/develop/paddle\phi\common\place.h)
-------------------------------

.. cpp:class:: explicit Place ( AllocationType type , int8_t id , const std::string & dev_type = "" ) :

<name="desc">
/// \brief The place is used to specify where the data is stored.
</name>

����Ŀ¼
:::::::::::::::::::::
paddle\phi\common\place.h

����
:::::::::::::::::::::
Place ( ) :
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
��

explicit Place ( AllocationType type , int8_t id , const std::string & dev_type = "" ) :
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
	- **type** (AllocationType) - 
	- **id** (int8_t) - 
	- **dev_type** (const std::string&) - 

����
:::::::::::::::::::::
��

explicit Place ( AllocationType type , const std::string & dev_type = "" ) :
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
	- **type** (AllocationType) - 
	- **dev_type** (const std::string&) - 

����
:::::::::::::::::::::
��

Place ( paddle::PlaceType type ) ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
	- **type** (paddle::PlaceType) - 

����
:::::::::::::::::::::
��

void Reset ( AllocationType type , int8_t device_id = 0 , const std::string & dev_type = "" ) noexcept {
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
	- **type** (AllocationType) - 
	- **device_id** (int8_t) - 
	- **dev_type** (const std::string&) - 

����
:::::::::::::::::::::
void

AllocationType GetType ( ) const {
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
int

int8_t GetDeviceId ( ) const {
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
int8_t

std::string GetDeviceType ( ) const {
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
std::string

std::string DebugString ( ) const ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
std::string

uint32_t HashValue ( ) const {
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
uint32_t

inline bool operator = = ( const Place & rhs ) const {
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
	- **rhs** (const Place&) - 

����
:::::::::::::::::::::
bool

inline bool operator ! = ( const Place & rhs ) const {
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
	- **rhs** (const Place&) - 

����
:::::::::::::::::::::
bool

inline bool operator<( const Place & rhs ) const {
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
	- **rhs** (const Place&) - 

����
:::::::::::::::::::::
bool



<name="reference_link">

</name>

