.. _cn_api_CPUContext:

CPUContext[源代码](https://github.com/PaddlePaddle/Paddle/blob/develop/paddle\phi\backends\cpu\cpu_context.h)
-------------------------------

.. cpp:class:: explicit CPUContext ( const Place & ) ;

<name="desc">

</name>

定义目录
:::::::::::::::::::::
paddle\phi\backends\cpu\cpu_context.h

方法
:::::::::::::::::::::
CPUContext ( ) ;
'''''''''
<name="desc">

</name>


返回
:::::::::::::::::::::
无

CPUContext ( CPUContext & & ) ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **&** (CPUContext&) - 

返回
:::::::::::::::::::::
无

CPUContext & operator = ( CPUContext & & ) ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **&** (CPUContext&) - 

返回
:::::::::::::::::::::
CPUContext

explicit CPUContext ( const Place & ) ;
'''''''''
<name="desc">

</name>


参数
:::::::::::::::::::::
	- **&** (const Place) - 

返回
:::::::::::::::::::::
无

virtual ~CPUContext ( ) ;
'''''''''
<name="desc">

</name>


返回
:::::::::::::::::::::
无

Eigen::DefaultDevice * eigen_device ( ) const ;
'''''''''
<name="desc">

</name>


返回
:::::::::::::::::::::
Eigen::DefaultDevice

const Place & GetPlace ( ) const override ;
'''''''''
<name="desc">

</name>


返回
:::::::::::::::::::::
Place

static const char * name ( ) {
'''''''''
<name="desc">

</name>


返回
:::::::::::::::::::::
char



<name="reference_link">

</name>

