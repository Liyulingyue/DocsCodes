# CAPI tools
CAPI tools用于一键生成 C++ 的 rst 文档。

## 调用方式
```python
python main.py [source dir] [target dir]
```

其中：
- source dir是安装后的Paddle C++ API声明路径。 例如`venv/Lib/site-packages/paddle/include/paddle`。
- target dir目标文件保存路径。

最终生成结果如下所示：
```python
target dir
| -cn
    |- index.rst
    |- Paddle
        |- fluid
        |- phi
        |- ...
| -en
    |- index.rst
    |- Paddle
        |- fluid
        |- phi
        |- ...
```

## 获取最新PaddlePaddle
pip install python -m pip install paddlepaddle==0.0.0 -f https://www.paddlepaddle.org.cn/whl/windows/cpu-mkl-avx/develop.html
