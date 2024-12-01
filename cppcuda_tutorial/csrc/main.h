#include <torch/extension.h>


torch::Tensor trilinear_interpolation_fw(
    const torch::Tensor feats,
    const torch::Tensor points
);


torch::Tensor trilinear_interpolation_bw(
    const torch::Tensor dL_dfeat_interp,
    const torch::Tensor feats,
    const torch::Tensor points
);
