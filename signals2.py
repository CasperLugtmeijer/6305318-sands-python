import numpy as np
def generate_sine_wave(frequency, duration, sample_rate):
    N = int(duration * sample_rate) # Shows total number of samples
    t = np.arange(N) / sample_rate # Is the time vector
    x = np.sin(2 * np.pi * frequency * t) # Builds the real sine-wave samples
    return t, x
