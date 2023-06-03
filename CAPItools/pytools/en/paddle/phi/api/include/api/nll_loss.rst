.. _en_api_paddle_experimental_nll_loss:

nll_loss
-------------------------------

..cpp: function::std::tuple<Tensor , Tensor> nll_loss ( const Tensor & input , const Tensor & label , const paddle::optional<Tensor> & weight , int64_t ignore_index = - 100 , const std::string & reduction = "mean" ) ;


This API is aligned with Python API, more details are shown in [paddle.nll_loss](https://www.paddlepaddle.org.cn/documentation/docs/zh/api/paddle/nll_loss_en.html)

Path
:::::::::::::::::::::
paddle\phi\api\include\api.h

Parameters
:::::::::::::::::::::
	- **input** (const Tensor&)
	- **label** (const Tensor&)
	- **weight** (const paddle::optional<Tensor>&)
	- **ignore_index** (int64_t)
	- **reduction** (const std::string&)

Returns
:::::::::::::::::::::
std::tuple<Tensor , Tensor>
