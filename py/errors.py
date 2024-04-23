import torch

from py.interfaces import Wavelet


class WaveUnsuppliedError(Exception):
    def __init__(self):
        self.message = (
            "Wavelet not supplied. A wavelet can be a derived from data or a function."
            "In the case of a tensor, it must be a Collection of integers or floats."
            "In the case of a function, the supplied function must ingest a tensor of identical shape"
            "to the data tensor comprised entirely of ones – akin to `torch.ones_like(x)` – whereupon it will"
            "be applied to that tensor."
            " See `py.callbacks` for further reference."
            "In either case, the tensor derived from them will be used to compute the dot product of your data and "
            "the wave function."
        )
        super().__init__(self.message)


class WaveDuplicityError(Exception):
    def __init__(self):
        self.message = "Wave must have a wave or a function, not both."
        super().__init__(self.message)


class WaveTypeError(Exception):
    def __init__(self):
        self.message = (
            "If a tensor is supplied, it must be a Collection of integers or floats."
            "If a function is supplied, it must be a callable"
        )
        super().__init__(self.message)


if __name__ == "__main__":
    # This will raise a WaveUnsuppliedError
    # Wavelet()

    # This will raise a WaveDuplicityError
    # Wavelet(tensor=[1, 2, 3], function=lambda x: x)

    # This will raise a WaveTypeError
    # Wavelet(tensor=1)

    # This will not raise an error
    Wavelet(tensor=torch.tensor([1, 2, 3]))

    # This will not raise an error
    Wavelet(function=lambda x: x)
