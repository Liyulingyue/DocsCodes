.. _cn_api_OpMetaInfoBuilder:

OpMetaInfoBuilder[源代码](https://github.com/PaddlePaddle/Paddle/blob/develop/paddle\phi\api\ext\op_meta_info.h)
-------------------------------

.. cpp:class:: explicit OpMetaInfoBuilder ( std::string & & name , size_t index ) ;

<name="desc">

</name>

定义目录
:::::::::::::::::::::
paddle\phi\api\ext\op_meta_info.h

方法
:::::::::::::::::::::
explicit OpMetaInfoBuilder ( std::string & & name , size_t index ) ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **name** (std::string) - 
	- **index** (size_t) - 

返回
:::::::::::::::::::::
无

OpMetaInfoBuilder & Inputs ( std::vector<std::string> & & inputs ) ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **inputs** (std::vector<std::string>) - 

返回
:::::::::::::::::::::
OpMetaInfoBuilder

OpMetaInfoBuilder & Outputs ( std::vector<std::string> & & outputs ) ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **outputs** (std::vector<std::string>) - 

返回
:::::::::::::::::::::
OpMetaInfoBuilder

OpMetaInfoBuilder & Attrs ( std::vector<std::string> & & attrs ) ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **attrs** (std::vector<std::string>) - 

返回
:::::::::::::::::::::
OpMetaInfoBuilder

OpMetaInfoBuilder & SetInplaceMap ( std::unordered_map<std::string , std::string> & & inplace_map ) ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **inplace_map** (std::unordered_map<std::string, std::string>) - 

返回
:::::::::::::::::::::
OpMetaInfoBuilder

OpMetaInfoBuilder & SetKernelFn ( KernelFunc func ) ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **func** (void ( ) ( CustomOpKernelContext )) - 

返回
:::::::::::::::::::::
OpMetaInfoBuilder

OpMetaInfoBuilder & SetInferShapeFn ( InferShapeFunc func ) ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **func** (vector<std::vector<int64_t> > ( ) ( const std::vector<std::vector<int64_t> > input_shapes, const std::vector<std::vector<std::vector<int64_t> > > vec_input_shapes, const std::vector<paddle::any> attrs )) - 

返回
:::::::::::::::::::::
OpMetaInfoBuilder

OpMetaInfoBuilder & SetInferDtypeFn ( InferDtypeFunc func ) ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **func** (vector<DataType> ( ) ( const std::vector<DataType> input_dtypes, const std::vector<std::vector<DataType> > vec_input_dtypes )) - 

返回
:::::::::::::::::::::
OpMetaInfoBuilder



<name="reference_link">

</name>

