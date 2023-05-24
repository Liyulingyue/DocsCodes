.. _en_api_OpMetaInfoBuilder:

OpMetaInfoBuilder[source](https://github.com/PaddlePaddle/Paddle/blob/develop/paddle\phi\api\ext\op_meta_info.h)
-------------------------------

.. cpp:class:: explicit OpMetaInfoBuilder ( std::string & & name , size_t index ) ;


Path
:::::::::::::::::::::
paddle\phi\api\ext\op_meta_info.h

Methods
:::::::::::::::::::::

explicit OpMetaInfoBuilder ( std::string & & name , size_t index ) ;
'''''''''''


**Parameters**
'''''''''''
	- **name** (std::string)
	- **index** (size_t)

OpMetaInfoBuilder & Inputs ( std::vector<std::string> & & inputs ) ;
'''''''''''


**Parameters**
'''''''''''
	- **inputs** (std::vector<std::string>)

**Returns**
'''''''''''
OpMetaInfoBuilder &
OpMetaInfoBuilder & Outputs ( std::vector<std::string> & & outputs ) ;
'''''''''''


**Parameters**
'''''''''''
	- **outputs** (std::vector<std::string>)

**Returns**
'''''''''''
OpMetaInfoBuilder &
OpMetaInfoBuilder & Attrs ( std::vector<std::string> & & attrs ) ;
'''''''''''


**Parameters**
'''''''''''
	- **attrs** (std::vector<std::string>)

**Returns**
'''''''''''
OpMetaInfoBuilder &
OpMetaInfoBuilder & SetInplaceMap ( std::unordered_map<std::string , std::string> & & inplace_map ) ;
'''''''''''


**Parameters**
'''''''''''
	- **inplace_map** (std::unordered_map<std::string, std::string>)

**Returns**
'''''''''''
OpMetaInfoBuilder &
OpMetaInfoBuilder & SetKernelFn ( KernelFunc func ) ;
'''''''''''


**Parameters**
'''''''''''
	- **func** (void ( ) ( CustomOpKernelContext ))

**Returns**
'''''''''''
OpMetaInfoBuilder &
OpMetaInfoBuilder & SetInferShapeFn ( InferShapeFunc func ) ;
'''''''''''


**Parameters**
'''''''''''
	- **func** (vector<std::vector<int64_t> > ( ) ( const std::vector<std::vector<int64_t> > input_shapes, const std::vector<std::vector<std::vector<int64_t> > > vec_input_shapes, const std::vector<paddle::any> attrs ))

**Returns**
'''''''''''
OpMetaInfoBuilder &
OpMetaInfoBuilder & SetInferDtypeFn ( InferDtypeFunc func ) ;
'''''''''''


**Parameters**
'''''''''''
	- **func** (vector<DataType> ( ) ( const std::vector<DataType> input_dtypes, const std::vector<std::vector<DataType> > vec_input_dtypes ))

**Returns**
'''''''''''
OpMetaInfoBuilder &
