.. _cn_api_CPUContext:

CPUContext[Դ����](https://github.com/PaddlePaddle/Paddle/blob/develop/paddle\phi\backends\cpu\cpu_context.h)
-------------------------------

.. cpp:class:: explicit CPUContext ( const Place & ) ;

<name="desc">

</name>

����Ŀ¼
:::::::::::::::::::::
paddle\phi\backends\cpu\cpu_context.h

����
:::::::::::::::::::::
CPUContext ( ) ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
��

CPUContext ( CPUContext & & ) ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
	- **&** (CPUContext&) - 

����
:::::::::::::::::::::
��

CPUContext & operator = ( CPUContext & & ) ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
	- **&** (CPUContext&) - 

����
:::::::::::::::::::::
CPUContext

explicit CPUContext ( const Place & ) ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
	- **&** (const Place) - 

����
:::::::::::::::::::::
��

virtual ~CPUContext ( ) ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
��

Eigen::DefaultDevice * eigen_device ( ) const ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
Eigen::DefaultDevice

const Place & GetPlace ( ) const override ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
Place

static const char * name ( ) {
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
char



<name="reference_link">

</name>

