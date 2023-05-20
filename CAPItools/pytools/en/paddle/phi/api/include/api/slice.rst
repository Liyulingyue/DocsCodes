.. _en_api_paddle_experimental_slice:

slice
-------------------------------

..cpp: function::Tensor slice ( const Tensor & input , const std::vector<int64_t> & axes , const IntArray & starts , const IntArray & ends , const std::vector<int64_t> & infer_flags , const std::vector<int64_t> & decrease_axis ) ;


Path
:::::::::::::::::::::
paddle\phi\api\include\api.h

Parameters
:::::::::::::::::::::
	- **input** (const Tensor&)
	- **axes** (const std::vector<int64_t>&)
	- **starts** (const IntArray&)
	- **ends** (const IntArray&)
	- **infer_flags** (const std::vector<int64_t>&)
	- **decrease_axis** (const std::vector<int64_t>&)

Returns
:::::::::::::::::::::
Tensor
