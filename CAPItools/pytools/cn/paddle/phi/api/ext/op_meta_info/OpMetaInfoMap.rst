.. _cn_api_OpMetaInfoMap:

OpMetaInfoMap[源代码](https://github.com/PaddlePaddle/Paddle/blob/develop/paddle\phi\api\ext\op_meta_info.h)
-------------------------------

.. cpp:class:: OpMetaInfoMap


定义目录
:::::::::::::::::::::
paddle\phi\api\ext\op_meta_info.h

方法
:::::::::::::::::::::

static OpMetaInfoMap & Instance ( ) {
'''''''''''



**返回**
'''''''''''
OpMetaInfoMap &
std::vector<OpMetaInfo> & operator [ ] ( const std::string & name ) ;
'''''''''''


**参数**
'''''''''''
	- **name** (const std::string&)

**返回**
'''''''''''
std::vector<OpMetaInfo> &
const std::unordered_map<std::string , std::vector<OpMetaInfo> > & GetMap ( ) const ;
'''''''''''



**返回**
'''''''''''
const std::unordered_map<std::string, std::vector<OpMetaInfo> > &
