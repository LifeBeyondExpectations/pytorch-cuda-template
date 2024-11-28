import torch  # isort:skip
import cppcuda_tutorial  # isort:skip


class Trilinear_interpolation_cuda(torch.autograd.Function):
    @staticmethod
    def forward(ctx, feats, points):
        feat_interp = cppcuda_tutorial.trilinear_interpolation_fw(feats, points)

        ctx.save_for_backward(feats, points)

        return feat_interp

    @staticmethod
    def backward(ctx, dL_dfeat_interp):
        feats, points = ctx.saved_tensors

        dL_dfeats = cppcuda_tutorial.trilinear_interpolation_bw(
            dL_dfeat_interp.contiguous(), feats, points
        )

        return dL_dfeats, None