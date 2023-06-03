.. _en_api_paddle_experimental_viterbi_decode:

viterbi_decode
-------------------------------

..cpp: function::std::tuple<Tensor , Tensor> viterbi_decode ( const Tensor & potentials , const Tensor & transition_params , const Tensor & lengths , bool include_bos_eos_tag = true ) ;


Path
:::::::::::::::::::::
paddle\phi\api\include\api.h

Parameters
:::::::::::::::::::::
	- **potentials** (const Tensor&)
	- **transition_params** (const Tensor&)
	- **lengths** (const Tensor&)
	- **include_bos_eos_tag** (bool)

Returns
:::::::::::::::::::::
std::tuple<Tensor , Tensor>
