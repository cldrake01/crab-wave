from typing import Collection, Callable, Any

from py.errors import WaveDuplicityError, WaveUnsuppliedError, WaveTypeError
from py.types import TensorGeneric, Scalar


class Wavelet:
    def __init__(
        self,
        tensor: TensorGeneric | None = None,
        function: Callable[[Any], Any] | None = None,
    ):
        assert tensor is not None or function is not None, WaveUnsuppliedError()
        assert not (tensor is not None and function is not None), WaveDuplicityError()
        assert isinstance(tensor, Collection) or callable(function), WaveTypeError()

        self.wave: TensorGeneric = tensor
        self.function: Callable[[Any], Any] = function


def transform(wavelet: Wavelet, data: Collection[Scalar]) -> Collection[Scalar]:
    if wavelet.wave is not None:
        return wavelet.wave
    return wavelet.function(data)
