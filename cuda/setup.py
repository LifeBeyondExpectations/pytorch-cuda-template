import os
from glob import glob

from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

setup(
    name="cppcuda_tutorial",
    version="1.0",
    author="jaesungchoe",
    author_email="jchoe@nvidia.com",
    description="cppcuda_tutorial",
    long_description="cppcuda_tutorial",
    ext_modules=[
        CUDAExtension(
            name="cppcuda_tutorial",
            sources=[
                "src/main.cpp",
                "src/forward_kernel.cu",
                "src/backward_kernel.cu",
            ],
            # sources=sources,
            # include_dirs=include_dirs,
            extra_compile_args={
                "cxx": ["-O2"],
                "nvcc": ["-O2"],
            },
        )
    ],
    cmdclass={"build_ext": BuildExtension},
)
