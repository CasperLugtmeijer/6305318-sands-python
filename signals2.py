import numpy as np
def generate_sine_wave(frequency, duration, sample_rate):
    N = int(duration * sample_rate) # Shows total number of samples
    t = np.arange(N) / sample_rate # Is the time vector
    x = np.sin(2 * np.pi * frequency * t) # Builds the real sine-wave samples
    return t, x

def generate_square(frequency, duration, sample_rate, amplitude = 1.0, duty = 0.5):
    N = int(duration * sample_rate)
    t = np.arange(N) / sample_rate
    phase = (t * frequency) % 1.0 # phase within each period (0,1)
    x = np.where(phase < duty, amplitude, -amplitude) #
    return t, x
