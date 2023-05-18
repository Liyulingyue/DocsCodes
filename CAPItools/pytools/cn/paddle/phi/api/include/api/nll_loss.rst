.. _cn_api_paddle_experimental_nll_loss:

nll_loss
-------------------------------

..cpp: function::std::tuple<Tensor , Tensor> nll_loss ( const Tensor & input , const Tensor & label , const paddle::optional<Tensor> & weight , int64_t ignore_index = - 100 , const std::string & reduction = "mean" ) ;

本 API 与 Python API 对齐，详细用法可参考链接：[paddle.nll_loss](https://www.paddlepaddle.org.cn/documentation/docs/zh/api/paddle/nll_loss_cn.html)

定义目录
:::::::::::::::::::::
paddle\phi\api\include\api.h

参数
:::::::::::::::::::::
	- **input** (const Tensor&)
	- **label** (const Tensor&)
	- **weight** (const paddle::optional<Tensor>&)
	- **ignore_index** (int64_t)
	- **reduction** (const std::string&)

返回
:::::::::::::::::::::
std::tuple<Tensor , Tensor>
