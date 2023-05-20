.. _en_api_paddle_experimental_linear_interp:

linear_interp
-------------------------------

..cpp: function::Tensor linear_interp ( const Tensor & x , const paddle::optional<Tensor> & out_size , const paddle::optional<std::vector<Tensor> > & size_tensor , const paddle::optional<Tensor> & scale_tensor , const std::string & data_layout = "NCHW" , int out_d = 0 , int out_h = 0 , int out_w = 0 , const std::vector<float> & scale = { } , const std::string & interp_method = "bilinear" , bool align_corners = true , int align_mode = 1 ) ;


Path
:::::::::::::::::::::
paddle\phi\api\include\api.h

Parameters
:::::::::::::::::::::
	- **x** (const Tensor&)
	- **out_size** (const paddle::optional<Tensor>&)
	- **size_tensor** (const paddle::optional<std::vector<Tensor> >&)
	- **scale_tensor** (const paddle::optional<Tensor>&)
	- **data_layout** (const std::string&)
	- **out_d** (int)
	- **out_h** (int)
	- **out_w** (int)
	- **scale** (const std::vector<float>&)
	- **interp_method** (const std::string&)
	- **align_corners** (bool)
	- **align_mode** (int)

Returns
:::::::::::::::::::::
Tensor
