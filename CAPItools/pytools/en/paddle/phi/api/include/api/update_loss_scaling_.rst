.. _en_api_paddle_experimental_update_loss_scaling_:

update_loss_scaling_
-------------------------------

..cpp: function::std::tuple<std::vector<Tensor> & , Tensor & , Tensor & , Tensor &> update_loss_scaling_ ( std::vector<Tensor> & x , const Tensor & found_infinite , Tensor & prev_loss_scaling , Tensor & in_good_steps , Tensor & in_bad_steps , int incr_every_n_steps , int decr_every_n_nan_or_inf , float incr_ratio , float decr_ratio , const Scalar & stop_update = false ) ;


Path
:::::::::::::::::::::
paddle\phi\api\include\api.h

Parameters
:::::::::::::::::::::
	- **x** (std::vector<Tensor>&)
	- **found_infinite** (const Tensor&)
	- **prev_loss_scaling** (Tensor&)
	- **in_good_steps** (Tensor&)
	- **in_bad_steps** (Tensor&)
	- **incr_every_n_steps** (int)
	- **decr_every_n_nan_or_inf** (int)
	- **incr_ratio** (float)
	- **decr_ratio** (float)
	- **stop_update** (const Scalar&)

Returns
:::::::::::::::::::::
std::tuple<std::vector<Tensor> , Tensor , Tensor , Tensor >
