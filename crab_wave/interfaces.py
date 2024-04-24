from typing import Collection, Callable, Any

import torch

from crab_wave.errors import WaveDuplicityError, WaveUnsuppliedError, WaveTypeError


class Wavelet:
    def __init__(
        self,
        tensor: Collection | None = None,
        function: Callable[[Any], Any] | None = None,
    ):
        assert tensor is not None or function is not None, WaveUnsuppliedError()
        assert not (tensor is not None and function is not None), WaveDuplicityError()
        assert isinstance(tensor, Collection) or callable(function), WaveTypeError()

        self.wave: Collection = tensor
        self.function: Callable[[Any], Any] = function


if __name__ == "__main__":
    # This will raise a WaveUnsuppliedError
    Wavelet()

    # This will raise a WaveDuplicityError
    Wavelet(tensor=[1, 2, 3], function=lambda x: x)

    # This will raise a WaveTypeError
    Wavelet(tensor=1)

    # This will not raise an error
    Wavelet(tensor=torch.tensor([1, 2, 3]))

    # This will not raise an error
    Wavelet(function=lambda x: x)
