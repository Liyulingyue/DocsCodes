.. _cn_api_OpMetaInfoMap:

OpMetaInfoMap[源代码](https://github.com/PaddlePaddle/Paddle/blob/develop/paddle\phi\api\ext\op_meta_info.h)
-------------------------------

.. cpp:class:: OpMetaInfoMap

<name="desc">

</name>

定义目录
:::::::::::::::::::::
paddle\phi\api\ext\op_meta_info.h

方法
:::::::::::::::::::::
static OpMetaInfoMap & Instance ( ) {
'''''''''
<name="desc">

</name>


返回
:::::::::::::::::::::
OpMetaInfoMap

std::vector<OpMetaInfo> & operator [ ] ( const std::string & name ) ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **name** (const std::string&) - 

返回
:::::::::::::::::::::
std :: vector< OpMetaInfo >

const std::unordered_map<std::string , std::vector<OpMetaInfo> > & GetMap ( ) const ;
'''''''''
<name="desc">

</name>


返回
:::::::::::::::::::::
std::unordered_map<std::string , std::vector<OpMetaInfo> >



<name="reference_link">

</name>

