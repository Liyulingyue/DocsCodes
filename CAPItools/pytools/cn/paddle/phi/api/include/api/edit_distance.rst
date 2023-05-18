.. _cn_api_paddle_experimental_edit_distance:

edit_distance
-------------------------------

..cpp: function::std::tuple<Tensor , Tensor> edit_distance ( const Tensor & hyps , const Tensor & refs , const paddle::optional<Tensor> & hypslength , const paddle::optional<Tensor> & refslength , bool normalized = false ) ;

定义目录
:::::::::::::::::::::
paddle\phi\api\include\api.h

参数
:::::::::::::::::::::
	- **hyps** (const Tensor&)
	- **refs** (const Tensor&)
	- **hypslength** (const paddle::optional<Tensor>&)
	- **refslength** (const paddle::optional<Tensor>&)
	- **normalized** (bool)

返回
:::::::::::::::::::::
std::tuple<Tensor , Tensor>
