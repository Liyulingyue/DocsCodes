.. _en_api_OpMetaInfo:

OpMetaInfo[source](https://github.com/PaddlePaddle/Paddle/blob/develop/paddle\phi\api\ext\op_meta_info.h)
-------------------------------

.. cpp:class:: explicit OpMetaInfo ( const std::string & op_name ) :


Path
:::::::::::::::::::::
paddle\phi\api\ext\op_meta_info.h

Methods
:::::::::::::::::::::

explicit OpMetaInfo ( const std::string & op_name ) :
'''''''''''


**Parameters**
'''''''''''
	- **op_name** (const std::string&)

OpMetaInfo & Inputs ( std::vector<std::string> & & inputs ) ;
'''''''''''


**Parameters**
'''''''''''
	- **inputs** (std::vector<std::string>)

**Returns**
'''''''''''
OpMetaInfo
OpMetaInfo & Outputs ( std::vector<std::string> & & outputs ) ;
'''''''''''


**Parameters**
'''''''''''
	- **outputs** (std::vector<std::string>)

**Returns**
'''''''''''
OpMetaInfo
OpMetaInfo & Attrs ( std::vector<std::string> & & attrs ) ;
'''''''''''


**Parameters**
'''''''''''
	- **attrs** (std::vector<std::string>)

**Returns**
'''''''''''
OpMetaInfo
OpMetaInfo & SetInplaceMap ( std::unordered_map<std::string , std::string> & & inplace_map ) ;
'''''''''''


**Parameters**
'''''''''''
	- **inplace_map** (std::unordered_map<std::string, std::string>)

**Returns**
'''''''''''
OpMetaInfo
OpMetaInfo & SetKernelFn ( KernelFunc & & func ) ;
'''''''''''


**Parameters**
'''''''''''
	- **func** (void ( ) ( CustomOpKernelContext ))

**Returns**
'''''''''''
OpMetaInfo
OpMetaInfo & SetInferShapeFn ( InferShapeFunc & & func ) ;
'''''''''''


**Parameters**
'''''''''''
	- **func** (vector<std::vector<int64_t> > ( ) ( const std::vector<std::vector<int64_t> > input_shapes, const std::vector<std::vector<std::vector<int64_t> > > vec_input_shapes, const std::vector<paddle::any> attrs ))

**Returns**
'''''''''''
OpMetaInfo
OpMetaInfo & SetInferDtypeFn ( InferDtypeFunc & & func ) ;
'''''''''''


**Parameters**
'''''''''''
	- **func** (vector<DataType> ( ) ( const std::vector<DataType> input_dtypes, const std::vector<std::vector<DataType> > vec_input_dtypes ))

**Returns**
'''''''''''
OpMetaInfo
