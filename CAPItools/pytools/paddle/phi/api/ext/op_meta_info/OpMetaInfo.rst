.. _cn_api_OpMetaInfo:

OpMetaInfo[Դ����](https://github.com/PaddlePaddle/Paddle/blob/develop/paddle\phi\api\ext\op_meta_info.h)
-------------------------------

.. cpp:class:: explicit OpMetaInfo ( const std::string & op_name ) :

<name="desc">

</name>

����Ŀ¼
:::::::::::::::::::::
paddle\phi\api\ext\op_meta_info.h

����
:::::::::::::::::::::
explicit OpMetaInfo ( const std::string & op_name ) :
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
	- **op_name** (const std::string&) - 

����
:::::::::::::::::::::
��

OpMetaInfo & Inputs ( std::vector<std::string> & & inputs ) ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
	- **inputs** (std::vector<std::string>) - 

����
:::::::::::::::::::::
OpMetaInfo

OpMetaInfo & Outputs ( std::vector<std::string> & & outputs ) ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
	- **outputs** (std::vector<std::string>) - 

����
:::::::::::::::::::::
OpMetaInfo

OpMetaInfo & Attrs ( std::vector<std::string> & & attrs ) ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
	- **attrs** (std::vector<std::string>) - 

����
:::::::::::::::::::::
OpMetaInfo

OpMetaInfo & SetInplaceMap ( std::unordered_map<std::string , std::string> & & inplace_map ) ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
	- **inplace_map** (std::unordered_map<std::string, std::string>) - 

����
:::::::::::::::::::::
OpMetaInfo

OpMetaInfo & SetKernelFn ( KernelFunc & & func ) ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
	- **func** (void ( ) ( CustomOpKernelContext )) - 

����
:::::::::::::::::::::
OpMetaInfo

OpMetaInfo & SetInferShapeFn ( InferShapeFunc & & func ) ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
	- **func** (vector<std::vector<int64_t> > ( ) ( const std::vector<std::vector<int64_t> > input_shapes, const std::vector<std::vector<std::vector<int64_t> > > vec_input_shapes, const std::vector<paddle::any> attrs )) - 

����
:::::::::::::::::::::
OpMetaInfo

OpMetaInfo & SetInferDtypeFn ( InferDtypeFunc & & func ) ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
	- **func** (vector<DataType> ( ) ( const std::vector<DataType> input_dtypes, const std::vector<std::vector<DataType> > vec_input_dtypes )) - 

����
:::::::::::::::::::::
OpMetaInfo



<name="reference_link">

</name>

