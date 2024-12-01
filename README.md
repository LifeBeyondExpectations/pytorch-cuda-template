# pytorch-cuda-template

This repository contains simple pytorch+CUDA template.

## File hierarchy.

- `function/*.py`: define your custom torch function.
- `src/main.cpp`: torch -> cpu
- `src/*.cu`: cpu -> cuda/kernel
- `test.py`: debug your implementation.

```
${root_dir}
├── function
│   └── trilinear_interpolation.py
├── src
│   ├── main.cpp
│   ├── forward_kernel.cu
│   └── backward_kernel.cu
└── test.py
```

## References

Dominantly refer to [pytorch-cppcuda-tutorial](https://github.com/kwea123/pytorch-cppcuda-tutorial). <br>
You can also refer to this nice tutorial, [pytorch-custom-cuda-tutorial](https://github.com/chrischoy/pytorch-custom-cuda-tutorial?tab=readme-ov-file).
