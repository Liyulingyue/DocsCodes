.. _cn_api_OpMetaInfoMap:

OpMetaInfoMap[Դ����](https://github.com/PaddlePaddle/Paddle/blob/develop/paddle\phi\api\ext\op_meta_info.h)
-------------------------------

.. cpp:class:: OpMetaInfoMap

<name="desc">

</name>

����Ŀ¼
:::::::::::::::::::::
paddle\phi\api\ext\op_meta_info.h

����
:::::::::::::::::::::
static OpMetaInfoMap & Instance ( ) {
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
OpMetaInfoMap

std::vector<OpMetaInfo> & operator [ ] ( const std::string & name ) ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
	- **name** (const std::string&) - 

����
:::::::::::::::::::::
std :: vector< OpMetaInfo >

const std::unordered_map<std::string , std::vector<OpMetaInfo> > & GetMap ( ) const ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
std::unordered_map<std::string , std::vector<OpMetaInfo> >



<name="reference_link">

</name>

