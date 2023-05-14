.. _cn_api_DeviceContextPool:

DeviceContextPool[Դ����](https://github.com/PaddlePaddle/Paddle/blob/develop/paddle\phi\api\include\context_pool.h)
-------------------------------

.. cpp:class:: DeviceContextPool

<name="desc">
 The DeviceContextPool here is just a mirror of the DeviceContextPool in fluid, and does not manage the life cycle of the DeviceContext. It is mainly used for external custom operator calls and high-performance C++ APIs. Since DeviceContextPool in fluid is a global singleton, it always exists in program running, so DeviceContextPool here can always access the correct DeviceContext pointer. In order not to depend on the fluid's DeviceContextPool, the DeviceContextPool here needs to be initialized in the fluid, and cannot be initialized by itself. Note: DeviceContextPool is an experimental API and may be removed in the future. From 2.3, we recommend directly using the C++ API to combine new operators.

</name>

����Ŀ¼
:::::::::::::::::::::
paddle\phi\api\include\context_pool.h

����
:::::::::::::::::::::
static DeviceContextPool & Instance ( ) ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
DeviceContextPool

const phi::DeviceContext * Get ( const Place & place ) ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
	- **place** (const Place&) - 

����
:::::::::::::::::::::
phi::DeviceContext

phi::DeviceContext * GetMutable ( const Place & place ) ;
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
	- **place** (const Place&) - 

����
:::::::::::::::::::::
phi::DeviceContext

const typename DefaultDeviceContextType<T>::TYPE * Get ( const Place & place ) {
'''''''''
<name="desc">

</name>


����
:::::::::::::::::::::
	- **place** (const Place&) - 

����
:::::::::::::::::::::
typename DefaultDeviceContextType<T >::TYPE



<name="reference_link">

</name>

