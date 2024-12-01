import os
from glob import glob

from setuptools import find_packages, setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

library_name = "cppcuda_tutorial"

setup(
    name=library_name,
    version="1.0.0",
    author="jaesungchoe",
    author_email="jchoe@nvidia.com",
    packages=find_packages(),
    ext_modules=[
        CUDAExtension(
            name=f"{library_name}._C",
            sources=[
                f"{library_name}/csrc/main.cpp",
                f"{library_name}/csrc/cuda/forward_kernel.cu",
                f"{library_name}/csrc/cuda/backward_kernel.cu",
            ],
            extra_compile_args={
                "cxx": ["-O2"],
                "nvcc": ["-O2"],
            },
        )
    ],
    install_requires=["torch"],
    cmdclass={"build_ext": BuildExtension},
)
