.. _en_api_paddle_experimental_rnn:

rnn
-------------------------------

..cpp: function::std::tuple<Tensor , Tensor , std::vector<Tensor> > rnn ( const Tensor & x , const std::vector<Tensor> & pre_state , const std::vector<Tensor> & weight_list , const paddle::optional<Tensor> & sequence_length , const Tensor & dropout_state_in , float dropout_prob = 0.0 , bool is_bidirec = false , int input_size = 10 , int hidden_size = 100 , int num_layers = 1 , const std::string & mode = "RNN_TANH" , int seed = 0 , bool is_test = false ) ;


Path
:::::::::::::::::::::
paddle\phi\api\include\api.h

Parameters
:::::::::::::::::::::
	- **x** (const Tensor&)
	- **pre_state** (const std::vector<Tensor>&)
	- **weight_list** (const std::vector<Tensor>&)
	- **sequence_length** (const paddle::optional<Tensor>&)
	- **dropout_state_in** (const Tensor&)
	- **dropout_prob** (float)
	- **is_bidirec** (bool)
	- **input_size** (int)
	- **hidden_size** (int)
	- **num_layers** (int)
	- **mode** (const std::string&)
	- **seed** (int)
	- **is_test** (bool)

Returns
:::::::::::::::::::::
std::tuple<Tensor , Tensor , std::vector<Tensor> >
