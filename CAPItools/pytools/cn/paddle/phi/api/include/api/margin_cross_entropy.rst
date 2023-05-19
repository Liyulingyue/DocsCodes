.. _cn_api_paddle_experimental_margin_cross_entropy:

margin_cross_entropy
-------------------------------

..cpp: function::std::tuple<Tensor , Tensor> margin_cross_entropy ( const Tensor & logits , const Tensor & label , bool return_softmax = false , int ring_id = 0 , int rank = 0 , int nranks = 1 , float margin1 = 1.0 f , float margin2 = 0.5 f , float margin3 = 0.0 f , float scale = 64.0 f ) ;


定义目录
:::::::::::::::::::::
paddle\phi\api\include\api.h

参数
:::::::::::::::::::::
	- **logits** (const Tensor&)
	- **label** (const Tensor&)
	- **return_softmax** (bool)
	- **ring_id** (int)
	- **rank** (int)
	- **nranks** (int)
	- **margin1** (float)
	- **margin2** (float)
	- **margin3** (float)
	- **scale** (float)

返回
:::::::::::::::::::::
std::tuple<Tensor , Tensor>
