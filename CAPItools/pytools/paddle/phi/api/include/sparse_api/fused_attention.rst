.. _cn_api_paddle_experimental_sparse_fused_attention:

fused_attention
-------------------------------

..cpp: function::Tensor fused_attention ( const Tensor & query , const Tensor & key , const Tensor & value , const Tensor & sparse_mask , const paddle::optional<Tensor> & key_padding_mask , const paddle::optional<Tensor> & attn_mask ) ;

定义目录
:::::::::::::::::::::
paddle\phi\api\include\sparse_api.h

参数
:::::::::::::::::::::
	- **query** (const Tensor&) - 
	- **key** (const Tensor&) - 
	- **value** (const Tensor&) - 
	- **sparse_mask** (const Tensor&) - 
	- **key_padding_mask** (const paddle::optional<Tensor>&) - 
	- **attn_mask** (const paddle::optional<Tensor>&) - 



返回
:::::::::::::::::::::
Tensor
