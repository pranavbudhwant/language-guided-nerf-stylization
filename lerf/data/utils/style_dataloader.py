import torch


class StyleDataLoader:
    """A dataloader for style images."""

    def __init__(self):
        self.image_cache = {}

    def __call__(self, indices: torch.Tensor) -> torch.Tensor:
        """Returns the style image for the given indices."""