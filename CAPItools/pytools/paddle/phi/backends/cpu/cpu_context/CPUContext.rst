.. _cn_api_CPUContext:

CPUContext[源代码](https://github.com/PaddlePaddle/Paddle/blob/develop/paddle\phi\backends\cpu\cpu_context.h)
-------------------------------

.. cpp:class:: explicit CPUContext ( const Place & ) ;


定义目录
:::::::::::::::::::::
paddle\phi\backends\cpu\cpu_context.h

方法
:::::::::::::::::::::

CPUContext ( ) ;
'''''''''''


**参数**
'''''''''''



CPUContext ( CPUContext & & ) ;
'''''''''''


**参数**
'''''''''''
	- **&** (CPUContext&) - 



CPUContext & operator = ( CPUContext & & ) ;
'''''''''''


**参数**
'''''''''''
	- **&** (CPUContext&) - 



**返回**
'''''''''''
CPUContext
explicit CPUContext ( const Place & ) ;
'''''''''''


**参数**
'''''''''''
	- **&** (const Place) - 



virtual ~CPUContext ( ) ;
'''''''''''


**参数**
'''''''''''



Eigen::DefaultDevice * eigen_device ( ) const ;
'''''''''''


**参数**
'''''''''''



**返回**
'''''''''''
Eigen::DefaultDevice
const Place & GetPlace ( ) const override ;
'''''''''''


**参数**
'''''''''''



**返回**
'''''''''''
Place
static const char * name ( ) {
'''''''''''


**参数**
'''''''''''



**返回**
'''''''''''
char
