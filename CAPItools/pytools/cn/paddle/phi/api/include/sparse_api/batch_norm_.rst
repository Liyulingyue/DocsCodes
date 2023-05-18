.. _cn_api_paddle_experimental_sparse_batch_norm_:

batch_norm_
-------------------------------

..cpp: function::std::tuple<Tensor , Tensor & , Tensor & , Tensor , Tensor , Tensor> batch_norm_ ( const Tensor & x , Tensor & mean , Tensor & variance , const Tensor & scale , const Tensor & bias , bool is_test , float momentum , float epsilon , const std::string & data_layout , bool use_global_stats , bool trainable_statistics ) ;

定义目录
:::::::::::::::::::::
paddle\phi\api\include\sparse_api.h

参数
:::::::::::::::::::::
	- **x** (const Tensor&)
	- **mean** (Tensor&)
	- **variance** (Tensor&)
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
