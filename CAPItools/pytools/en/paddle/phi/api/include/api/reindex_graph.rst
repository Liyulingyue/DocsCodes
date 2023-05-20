.. _en_api_paddle_experimental_reindex_graph:

reindex_graph
-------------------------------

..cpp: function::std::tuple<Tensor , Tensor , Tensor> reindex_graph ( const Tensor & x , const Tensor & neighbors , const Tensor & count , const paddle::optional<Tensor> & hashtable_value , const paddle::optional<Tensor> & hashtable_index ) ;


Path
:::::::::::::::::::::
paddle\phi\api\include\api.h

Parameters
:::::::::::::::::::::
	- **x** (const Tensor&)
	- **neighbors** (const Tensor&)
	- **count** (const Tensor&)
	- **hashtable_value** (const paddle::optional<Tensor>&)
	- **hashtable_index** (const paddle::optional<Tensor>&)

Returns
:::::::::::::::::::::
std::tuple<Tensor , Tensor , Tensor>
