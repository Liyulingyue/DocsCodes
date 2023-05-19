.. _cn_api_paddle_experimental_batch_norm:

batch_norm
-------------------------------

..cpp: function::std::tuple<Tensor , Tensor , Tensor , Tensor , Tensor , Tensor> batch_norm ( const Tensor & x , const Tensor & mean , const Tensor & variance , const Tensor & scale , const Tensor & bias , bool is_test , float momentum , float epsilon , const std::string & data_layout , bool use_global_stats , bool trainable_statistics ) ;


定义目录
:::::::::::::::::::::
paddle\phi\api\include\api.h

参数
:::::::::::::::::::::
	- **x** (const Tensor&)
	- **mean** (const Tensor&)
	- **variance** (const Tensor&)
	- **scale** (const Tensor&)
	- **bias** (const Tensor&)
	- **is_test** (bool)
	- **momentum** (float)
	- **epsilon** (float)
	- **data_layout** (const std::string&)
	- **use_global_stats** (bool)
	- **trainable_statistics** (bool)

返回
:::::::::::::::::::::
std::tuple<Tensor , Tensor , Tensor , Tensor , Tensor , Tensor>
