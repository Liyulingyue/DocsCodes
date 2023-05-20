.. _en_api_paddle_experimental_flash_attn:

flash_attn
-------------------------------

..cpp: function::std::tuple<Tensor , Tensor> flash_attn ( const Tensor & q , const Tensor & k , const Tensor & v , const paddle::optional<Tensor> & fixed_seed_offset , float dropout = 0.0 , bool causal = false , bool return_softmax = false , bool is_test = false , const std::string & rng_name = "" ) ;


定义目录
:::::::::::::::::::::
paddle\phi\api\include\api.h

参数
:::::::::::::::::::::
	- **q** (const Tensor&)
	- **k** (const Tensor&)
	- **v** (const Tensor&)
	- **fixed_seed_offset** (const paddle::optional<Tensor>&)
	- **dropout** (float)
	- **causal** (bool)
	- **return_softmax** (bool)
	- **is_test** (bool)
	- **rng_name** (const std::string&)

返回
:::::::::::::::::::::
std::tuple<Tensor , Tensor>
