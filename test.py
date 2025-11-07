import numpy as np
from signals2 import generate_sine_wave, generate_square, time_shift, add_signals

def test_generate_sine_wave():
    """
    Sine: correct length, starts at 0, and reaches +1 at a quarter period.Also checks the  edge case duration=0 returns empty arrays.
    """
    
    t, y = generate_sine_wave(5, 2, 100)
    assert len(t) == 200
    assert y[0] == 0

    fs, f = 100, 5
    k = int(fs / (4 * f))
    assert np.isclose(y[k], 1.0, atol=1e-6)

    t0, y0 = generate_sine_wave(5, 0, 100)
    assert len(t0) == 0 and len(y0) == 0


def test_generate_square():
    """
    quare: values only ±amplitude, duty cycle close to requested, and duration=0 returns empty arrays.
    """
    f, fs, dur, amp, duty = 5, 100, 1.0, 2.0, 0.25
    t, x = generate_square(f, dur, fs, amplitude=amp, duty=duty)

    assert set(np.unique(x)) <= {-amp, amp}

    frac_pos = (x == amp).mean()
    assert abs(frac_pos - duty) <= 0.05

    t0, x0 = generate_square(f, 0.0, fs, amplitude=amp, duty=duty)
    assert len(t0) == 0 and len(x0) == 0


def test_time_shift():
    """
    
    f, fs, dur = 2, 10, 1.0
    t, x = generate_sine_wave(f, dur, fs)

    _, y = time_shift(t, x, shift_seconds=0.2, sample_rate=fs)
    assert np.allclose(y[:2], 0.0)
    assert np.allclose(y[2:], x[:-2])

    _, z = time_shift(t, x, shift_seconds=-0.2, sample_rate=fs)
    assert np.allclose(z[-2:], 0.0)
    assert np.allclose(z[:-2], x[2:])


def test_add_signals():
    fs, dur = 50, 1.0
    t, x1 = generate_sine_wave(3, dur, fs)
    _, x2 = generate_sine_wave(7, dur, fs)

    tout, y = add_signals(t, x1, x2)
    assert np.allclose(tout, t)
    assert np.allclose(y, x1 + x2)

    try:
        add_signals(t, x1[:-1], x2)
        assert False, "Expected ValueError for different lengths"
    except ValueError:
        pass