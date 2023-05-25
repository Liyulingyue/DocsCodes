.. _en_api_OpMetaInfoMap:

OpMetaInfoMap[source](https://github.com/PaddlePaddle/Paddle/blob/develop/paddle\phi\api\ext\op_meta_info.h)
-------------------------------

.. cpp:class:: OpMetaInfoMap


Path
:::::::::::::::::::::
paddle\phi\api\ext\op_meta_info.h

Methods
:::::::::::::::::::::

static OpMetaInfoMap & Instance ( ) {
'''''''''''



**Returns**
'''''''''''
OpMetaInfoMap &

std::vector<OpMetaInfo> & operator [ ] ( const std::string & name ) ;
'''''''''''


**Parameters**
'''''''''''
	- **name** (const std::string&)

**Returns**
'''''''''''
std::vector<OpMetaInfo> &

const std::unordered_map<std::string , std::vector<OpMetaInfo> > & GetMap ( ) const ;
'''''''''''



**Returns**
'''''''''''
const std::unordered_map<std::string, std::vector<OpMetaInfo> > &

