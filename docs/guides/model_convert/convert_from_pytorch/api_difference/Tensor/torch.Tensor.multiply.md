## [ 仅 paddle 参数更多 ] torch.Tensor.multiply

### [torch.Tensor.multiply](https://pytorch.org/docs/1.13/generated/torch.Tensor.multiply.html)

```python
torch.Tensor.multiply(value)
```

### [paddle.Tensor.multiply](https://www.paddlepaddle.org.cn/documentation/docs/zh/api/paddle/Tensor_cn.html#multiply-y-axis-1-name-none)

```python
paddle.Tensor.multiply(y,
                axis=-1,
                name=None)
```

Paddle 相比 PyTorch 支持更多其他参数，具体如下：

### 参数映射
| PyTorch       | PaddlePaddle | 备注                                             |
| ------------- | ------------ | ----------------------------------------------- |
| value         | y            | 相乘的矩阵，仅参数名不一致。                       |
| -             | axis         | 计算的维度，PyTorch 无此参数， Paddle 保持默认即可。|
