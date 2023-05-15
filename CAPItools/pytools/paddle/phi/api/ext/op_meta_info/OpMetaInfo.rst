.. _cn_api_OpMetaInfo:

OpMetaInfo[源代码](https://github.com/PaddlePaddle/Paddle/blob/develop/paddle\phi\api\ext\op_meta_info.h)
-------------------------------

.. cpp:class:: explicit OpMetaInfo ( const std::string & op_name ) :


定义目录
:::::::::::::::::::::
paddle\phi\api\ext\op_meta_info.h

方法
:::::::::::::::::::::

explicit OpMetaInfo ( const std::string & op_name ) :
'''''''''''


**参数**
'''''''''''
	- **op_name** (const std::string&) - 



OpMetaInfo & Inputs ( std::vector<std::string> & & inputs ) ;
'''''''''''


**参数**
'''''''''''
	- **inputs** (std::vector<std::string>) - 



**返回**
'''''''''''
OpMetaInfo
OpMetaInfo & Outputs ( std::vector<std::string> & & outputs ) ;
'''''''''''


**参数**
'''''''''''
	- **outputs** (std::vector<std::string>) - 



**返回**
'''''''''''
OpMetaInfo
OpMetaInfo & Attrs ( std::vector<std::string> & & attrs ) ;
'''''''''''


**参数**
'''''''''''
	- **attrs** (std::vector<std::string>) - 



**返回**
'''''''''''
OpMetaInfo
OpMetaInfo & SetInplaceMap ( std::unordered_map<std::string , std::string> & & inplace_map ) ;
'''''''''''


**参数**
'''''''''''
	- **inplace_map** (std::unordered_map<std::string, std::string>) - 



**返回**
'''''''''''
OpMetaInfo
OpMetaInfo & SetKernelFn ( KernelFunc & & func ) ;
'''''''''''


**参数**
'''''''''''
	- **func** (void ( ) ( CustomOpKernelContext )) - 



**返回**
'''''''''''
OpMetaInfo
OpMetaInfo & SetInferShapeFn ( InferShapeFunc & & func ) ;
'''''''''''


**参数**
'''''''''''
	- **func** (vector<std::vector<int64_t> > ( ) ( const std::vector<std::vector<int64_t> > input_shapes, const std::vector<std::vector<std::vector<int64_t> > > vec_input_shapes, const std::vector<paddle::any> attrs )) - 



**返回**
'''''''''''
OpMetaInfo
OpMetaInfo & SetInferDtypeFn ( InferDtypeFunc & & func ) ;
'''''''''''


**参数**
'''''''''''
	- **func** (vector<DataType> ( ) ( const std::vector<DataType> input_dtypes, const std::vector<std::vector<DataType> > vec_input_dtypes )) - 



**返回**
'''''''''''
OpMetaInfo
