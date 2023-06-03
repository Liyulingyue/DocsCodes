.. _en_api_paddle_experimental_edit_distance:

edit_distance
-------------------------------

..cpp: function::std::tuple<Tensor , Tensor> edit_distance ( const Tensor & hyps , const Tensor & refs , const paddle::optional<Tensor> & hypslength , const paddle::optional<Tensor> & refslength , bool normalized = false ) ;


Path
:::::::::::::::::::::
paddle\phi\api\include\api.h

Parameters
:::::::::::::::::::::
	- **hyps** (const Tensor&)
	- **refs** (const Tensor&)
	- **hypslength** (const paddle::optional<Tensor>&)
	- **refslength** (const paddle::optional<Tensor>&)
	- **normalized** (bool)

Returns
:::::::::::::::::::::
std::tuple<Tensor , Tensor>
