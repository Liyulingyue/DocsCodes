.. _en_api_CPUContext:

CPUContext[source](https://github.com/PaddlePaddle/Paddle/blob/develop/paddle\phi\backends\cpu\cpu_context.h)
-------------------------------

.. cpp:class:: explicit CPUContext ( const Place & ) ;


Path
:::::::::::::::::::::
paddle\phi\backends\cpu\cpu_context.h

Methods
:::::::::::::::::::::

CPUContext ( ) ;
'''''''''''



CPUContext ( CPUContext & & ) ;
'''''''''''



CPUContext & operator = ( CPUContext & & ) ;
'''''''''''



**Returns**
'''''''''''
CPUContext &

explicit CPUContext ( const Place & ) ;
'''''''''''



virtual ~CPUContext ( ) ;
'''''''''''



Eigen::DefaultDevice * eigen_device ( ) const ;
'''''''''''



**Returns**
'''''''''''
Eigen::DefaultDevice *

const Place & GetPlace ( ) const override ;
'''''''''''



**Returns**
'''''''''''
const Place &

static const char * name ( ) {
'''''''''''



**Returns**
'''''''''''
const char *

