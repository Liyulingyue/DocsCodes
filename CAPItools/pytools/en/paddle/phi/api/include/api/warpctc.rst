.. _en_api_paddle_experimental_warpctc:

warpctc
-------------------------------

..cpp: function::Tensor warpctc ( const Tensor & logits , const Tensor & label , const paddle::optional<Tensor> & logits_length , const paddle::optional<Tensor> & labels_length , int blank = 0 , bool norm_by_times = false ) ;


Path
:::::::::::::::::::::
paddle\phi\api\include\api.h

Parameters
:::::::::::::::::::::
	- **logits** (const Tensor&)
	- **label** (const Tensor&)
	- **logits_length** (const paddle::optional<Tensor>&)
	- **labels_length** (const paddle::optional<Tensor>&)
	- **blank** (int)
	- **norm_by_times** (bool)

Returns
:::::::::::::::::::::
Tensor
