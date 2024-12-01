# pytorch-cuda-template

This repository contains simple pytorch+CUDA template and its packaging

## Build

```
python setup.py install
```

## Test

```
python test_extension/test.py
```

## Import

```
from cppcuda_tutorial import Trilinear_interpolation_cuda
out_cuda = Trilinear_interpolation_cuda.apply(
    feats2, points
)
```

## File hierarchy.

- `function.py`: define your custom torch function to be imported.
- `.../main.cpp`: torch -> cpu
- `.../*.cu`: cpu -> cuda/kernel
- `test.py`: debug your implementation.

```
${root_dir}
├── cppcuda_tutorial
│   ├── csrc
│   │   ├── main.cpp
│   │   └── cuda
│   │       ├── forward_kernel.cu
│   │       └── backward_kernel.cu
│   ├── __init__.py
│   └── function.py
├── test_extension
│   └── test.py
├── pyproject.toml
└── setup.py
```

## References

Dominantly refer to [pytorch-cppcuda-tutorial](https://github.com/kwea123/pytorch-cppcuda-tutorial) and [official-extension-cpp](https://github.com/pytorch/extension-cpp). <br>
You can also refer to this nice tutorial, [pytorch-custom-cuda-tutorial](https://github.com/chrischoy/pytorch-custom-cuda-tutorial?tab=readme-ov-file).
