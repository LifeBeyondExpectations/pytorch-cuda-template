#include <torch/extension.h>


torch::Tensor trilinear_fw_cu(
    const torch::Tensor feats,
    const torch::Tensor points
);
