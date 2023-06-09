# Introduction to VisualDL Toolset

<p align="center">
  <img src="https://raw.githubusercontent.com/PaddlePaddle/VisualDL/develop/docs/images/vs-logo.png" width="60%" />
</p>

## Introduction
VisualDL is a deep learning visualization tool that can help design deep learning jobs.
It includes features such as scalar, parameter distribution, model structure and image visualization.
Currently it is being developed at a high pace.
New features will be continuously added.

At present, most DNN frameworks use Python as their primary language. VisualDL supports Python by nature.
Users can get plentiful visualization results by simply add a few lines of Python code into their model before training.

Besides Python SDK, VisualDL was writen in C++ on the low level. It also provides C++ SDK that
can be integrated into other platforms.


## Component
VisualDL provides following components:

- scalar
- histogram
- image
- audio
- graph
- high dimensional

### Scalar
Scalar can be used to show the trends of error during training.

<p align="center">
<img src="https://raw.githubusercontent.com/daming-lu/large_files/master/loss_scalar.gif" width="60%"/>
</p>

### Histogram
Histogram can be used to visualize parameter distribution and trends for any tensor.

<p align="center">
<img src="https://raw.githubusercontent.com/daming-lu/large_files/master/histogram.gif" width="60%"/>
</p>

### Image
Image can be used to visualize any tensor or intermediate generated image.

<p align="center">
<img src="https://raw.githubusercontent.com/daming-lu/large_files/master/loss_image.gif" width="60%"/>
</p>

### Audio
Audio can be used to play input audio samples or generated audio samples.

### Graph

VisualDL graph supports displaying paddle model, furthermore is compatible with ONNX ([Open Neural Network Exchange](https://github.com/onnx/onnx)),
Cooperated with Python SDK, VisualDL can be compatible with most major DNN frameworks, including
PaddlePaddle, PyTorch and MXNet.

<p align="center">
  <img src="https://raw.githubusercontent.com/PaddlePaddle/VisualDL/develop/docs/images/graph_demo.gif" width="60%" />
</p>

To display the paddle model, all you have to do is:

1. call the `fluid.io.save_inference_model()`interface to save paddle model
2. use `visualdl --model_pb [paddle_model_dir]` to load paddle model in command line


### High Dimensional
High Dimensional can be used to visualize data embeddings by projecting high-dimensional data into 2D / 3D.

<p align="center">
<img src="https://raw.githubusercontent.com/PaddlePaddle/VisualDL/develop/docs/getting_started/high_dimensional_3d.png" width="60%"/>
</p>

## Quick Start
To give the VisualDL a quick test, please use the following commands.

```
# Install the VisualDL. Preferably under a virtual environment or anaconda.
pip install --upgrade visualdl

# run a demo, vdl_create_scratch_log will create logs for testing.
vdl_create_scratch_log
visualdl --logdir=scratch_log --port=8080

# visit http://127.0.0.1:8080
```

If you encounter the error `TypeError: __init__() got an unexpected keyword argument 'file'`, that is due to protobuf version is not 3.5+，simply run `pip install --upgrade protobuf` will fix the issue.

If you run into any other issues in above steps, it could be error caused by environmental issues by different python or pip versions.
Following installation methods might fix the issues.

## Install with Virtualenv

[Virtualenv](https://virtualenv.pypa.io/en/stable/) creates isolated Python environment that prevents interfering
by other Python programs on the same machine and make sure Python and pip are located properly.

On macOS, install pip and virtualenv by:
```
sudo easy_install pip
pip install --upgrade virtualenv
```

On Linux, install pip and virtualenv by:
```
sudo apt-get install python3-pip python3-dev python-virtualenv
```

Then create a Virtualenv environment by one of following command:
```
virtualenv -p python3 ~/vdl for Python 3.x
```

```~/vdl``` will be your Virtualenv directory, you may choose to install anywhere.

Activate your Virtualenv environment by:
```
source ~/vdl/bin/activate
```

Now you should be able to install VisualDL and run our demo:

```
pip install --upgrade visualdl

# run a demo, vdl_create_scratch_log will create logs for testing.
vdl_create_scratch_log
visualdl --logdir=scratch_log --port=8080

# visit http://127.0.0.1:8080
```

If you still have issues installing VisualDL from Virtualenv, try following installation method.


## Install with Anaconda

Anaconda is a python distribution, with installation and package management tools. Also it is an environment manager,
which provides the facility to create different python environments, each with their own settings.

Follow the instructions on the [Anaconda download site](https://www.anaconda.com/download) to download and install Anaconda.
Download Python 3.6 version command-Line installer.

Create a conda environment named ```vdl``` or anything you want by:
```
conda create -n vdl pip python=2.7 # or python=3.3, etc.
```

Activate the conda environment by:
```
source activate vdl
```

Now you should be able to install VisualDL and run our demo:

```
pip install --upgrade visualdl

# run a demo, vdl_create_scratch_log will create logs for testing.
vdl_create_scratch_log
visualdl --logdir=scratch_log --port=8080

# visit http://127.0.0.1:8080
```

If you still have issues installing VisualDL, try installing from sources as in following section.


### Install from source
```
#Preferably under a virtualenv or anaconda.
git clone https://github.com/PaddlePaddle/VisualDL.git
cd VisualDL

python setup.py bdist_wheel
pip install --upgrade dist/visualdl-*.whl
```

If there are still issues regarding the ```pip install```, you can still start Visual DL by starting the dev server
[here](https://github.com/PaddlePaddle/VisualDL/tree/develop/docs#%E5%AE%89%E8%A3%85%E6%96%B9%E5%BC%8F)


## SDK
VisualDL provides both Python SDK and C++ SDK in order to fit more use cases.


### Python SDK
VisualDL now supports both Python 2 and Python 3.
Below is an example of creating a simple Scalar component and inserting data from different timestamps:

```python
import random
from visualdl import LogWriter

logdir = "./tmp"
logger = LogWriter(logdir, sync_cycle=10000)

# mark the components with 'train' label.
with logger.mode("train"):
    # create a scalar component called 'scalars/scalar0'
    scalar0 = logger.scalar("scalars/scalar0")

# add some records during DL model running.
for step in range(100):
    scalar0.add_record(step, random.random())
```

### C++ SDK
Here is the C++ SDK identical to the Python SDK example above:

```c++
#include <cstdlib>
#include <string>
#include "visualdl/logic/sdk.h"

namespace vs = visualdl;
namespace cp = visualdl::components;

int main() {
  const std::string dir = "./tmp";
  vs::LogWriter logger(dir, 10000);

  logger.SetMode("train");
  auto tablet = logger.AddTablet("scalars/scalar0");

  cp::Scalar<float> scalar0(tablet);

  for (int step = 0; step < 1000; step++) {
    float v = (float)std::rand() / RAND_MAX;
    scalar0.AddRecord(step, v);
  }

  return 0;
}
```

## Launch Visual DL
After some logs have been generated during training, users can launch Visual DL application to see real-time data visualization by:


```
visualdl --logdir <some log dir>
```

visualDL also supports following optional parameters:

- `--host` set IP
- `--port` set port
- `-m / --model_pb` specify ONNX format for model file to view graph


### Contribute

VisualDL is initially created by [PaddlePaddle](http://www.paddlepaddle.org/) and
[ECharts](http://echarts.baidu.com/).
We welcome everyone to use, comment and contribute to VisualDL :)

## More details

For more details about how to use VisualDL, please take a look at [documents](https://github.com/PaddlePaddle/VisualDL/tree/develop/demo)
