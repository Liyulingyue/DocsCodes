.. _en_api_paddle_experimental_weighted_sample_neighbors:

weighted_sample_neighbors
-------------------------------

..cpp: function::std::tuple<Tensor , Tensor , Tensor> weighted_sample_neighbors ( const Tensor & row , const Tensor & colptr , const Tensor & edge_weight , const Tensor & input_nodes , const paddle::optional<Tensor> & eids , int sample_size , bool return_eids ) ;


Path
:::::::::::::::::::::
paddle\phi\api\include\api.h

Parameters
:::::::::::::::::::::
	- **row** (const Tensor&)
	- **colptr** (const Tensor&)
	- **edge_weight** (const Tensor&)
	- **input_nodes** (const Tensor&)
	- **eids** (const paddle::optional<Tensor>&)
	- **sample_size** (int)
	- **return_eids** (bool)

Returns
:::::::::::::::::::::
std::tuple<Tensor , Tensor , Tensor>
