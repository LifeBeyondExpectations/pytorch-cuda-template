#include <torch/extension.h>


torch::Tensor trilinear_bw_cu(
    const torch::Tensor dL_dfeat_interp,
    const torch::Tensor feats,
    const torch::Tensor points
);
