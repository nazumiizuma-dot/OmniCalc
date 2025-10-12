import numpy as np
def dft(values):
    x = np.array(values, dtype=complex)
    X = np.fft.fft(x).tolist()
    return {"dft": [complex(z).real + 1j*complex(z).imag for z in X]}
