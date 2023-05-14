.. _cn_api_OpMetaInfoBuilder:

OpMetaInfoBuilder[Դ����](https://github.com/PaddlePaddle/Paddle/blob/develop/paddle\phi\api\ext\op_meta_info.h)
-------------------------------

.. cpp:class:: explicit OpMetaInfoBuilder ( std::string & & name , size_t index ) ;

<name="desc">

</name>

����Ŀ¼
:::::::::::::::::::::
paddle\phi\api\ext\op_meta_info.h

����
:::::::::::::::::::::
explicit OpMetaInfoBuilder ( std::string & & name , size_t index ) ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
	- **name** (std::string) - 
	- **index** (size_t) - 

����
:::::::::::::::::::::
��

OpMetaInfoBuilder & Inputs ( std::vector<std::string> & & inputs ) ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
	- **inputs** (std::vector<std::string>) - 

����
:::::::::::::::::::::
OpMetaInfoBuilder

OpMetaInfoBuilder & Outputs ( std::vector<std::string> & & outputs ) ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
	- **outputs** (std::vector<std::string>) - 

����
:::::::::::::::::::::
OpMetaInfoBuilder

OpMetaInfoBuilder & Attrs ( std::vector<std::string> & & attrs ) ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
	- **attrs** (std::vector<std::string>) - 

����
:::::::::::::::::::::
OpMetaInfoBuilder

OpMetaInfoBuilder & SetInplaceMap ( std::unordered_map<std::string , std::string> & & inplace_map ) ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
	- **inplace_map** (std::unordered_map<std::string, std::string>) - 

����
:::::::::::::::::::::
OpMetaInfoBuilder

OpMetaInfoBuilder & SetKernelFn ( KernelFunc func ) ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
	- **func** (void ( ) ( CustomOpKernelContext )) - 

����
:::::::::::::::::::::
OpMetaInfoBuilder

OpMetaInfoBuilder & SetInferShapeFn ( InferShapeFunc func ) ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
	- **func** (vector<std::vector<int64_t> > ( ) ( const std::vector<std::vector<int64_t> > input_shapes, const std::vector<std::vector<std::vector<int64_t> > > vec_input_shapes, const std::vector<paddle::any> attrs )) - 

����
:::::::::::::::::::::
OpMetaInfoBuilder

OpMetaInfoBuilder & SetInferDtypeFn ( InferDtypeFunc func ) ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
	- **func** (vector<DataType> ( ) ( const std::vector<DataType> input_dtypes, const std::vector<std::vector<DataType> > vec_input_dtypes )) - 

����
:::::::::::::::::::::
OpMetaInfoBuilder



<name="reference_link">

</name>

