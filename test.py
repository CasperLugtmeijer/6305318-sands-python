import numpy as np
from signals2 import generate_sine_wave, generate_square, time_shift, add_signals

def test_generate_sine_wave():
    t, y = generate_sine_wave(5, 2, 100)
    assert len(t) == 200
    assert y[0] == 0

    fs, f = 100, 5
    k = int(fs / (4 * f))
    assert np.isclose(y[k], 1.0, atol=1e-6)

    t0, y0 = generate_sine_wave(5, 0, 100)
    assert len(t0) == 0 and len(y0) == 0