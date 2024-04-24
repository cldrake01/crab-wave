class WaveUnsuppliedError(Exception):
    def __init__(self):
        self.message = (
            "Wavelet not supplied. A wavelet can be a derived from data or a function. "
            "In the case of a tensor, it must be a Collection of integers or floats. "
            "In the case of a function, the supplied function must ingest a tensor of identical shape "
            "to the data tensor comprised entirely of ones – akin to `torch.ones_like(x)` – whereupon it will "
            "be applied to that tensor. "
            "See `py.callbacks` for further reference. "
            "In either case, the tensor derived from them will be used to compute the dot product of your data and "
            "the wave function."
        )
        super().__init__(self.message)


class WaveDuplicityError(Exception):
    def __init__(self):
        self.message = "Wave must have a tensor or a function, not both."
        super().__init__(self.message)


class WaveTypeError(Exception):
    def __init__(self):
        self.message = (
            "If a tensor is supplied, it must be a Collection of integers or floats. "
            "Collections (tuples, lists), NumPy arrays, PyTorch tensors, and TensorFlow tensors all qualify. "
            "If a function is supplied, it must be a callable. As for its signature, it must be able to ingest "
            "the collection supplied to `transform`, and its return type must, of course, be the same as the input. "
            "After which, its output will be dot-ed with the data tensor, e.g., `dot(data, function(data))`."
        )
        super().__init__(self.message)
