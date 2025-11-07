import numpy as np
def generate_sine_wave(frequency, duration, sample_rate):
    """
    Generate a sampled sine wave.

    Parameters:
    frequency : float # Hz
    duration : float # Seconds
    sample_rate : int # Samples/second
    
    Returns:
    t : np.ndarray #time vector (seconds), length N
    x : np.ndarray #sine samples, same shape as t
    """
    N = int(duration * sample_rate)
    t = np.arange(N) / sample_rate
    x = np.sin(2 * np.pi * frequency * t)
    return t, x

def generate_square(frequency, duration, sample_rate, amplitude = 1.0, duty = 0.5):
    """
    Generate a square wave with given amplitude and duty cycle.

    Parameters:
    frequency : float # Hz
    duration : float # Seconds
    sample_rate : int # Samples/second
    amplitude : float # output levels are ±amplitude
    duty : float # fraction of period at +amplitude (0..1)
    
    Returns:
    t : np.ndarray # time vector (seconds), length N
    x : np.ndarray # square-wave samples (±amplitude), same shape as t
    """
    N = int(duration * sample_rate)
    t = np.arange(N) / sample_rate
    phase = (t * frequency) % 1.0 # phase within each period (0,1)
    x = np.where(phase < duty, amplitude, -amplitude) 
    return t, x

def time_shift(t, x, shift_seconds, sample_rate):
    """
    Shift a signal in time using zero padding.

    Parameters:
    t : np.ndarray # time vector (returned unchanged)
    x : np.ndarray # input samples
    shift_seconds : float # seconds to shift
    sample_rate : int # samples/second

    Return:
    t : np.ndarray # same time vector as input
    y : np.ndarray # shifted signal, same shape as x
    """
    n = int(round(shift_seconds * sample_rate))
    y = np.zeros_like(x)
    if n >= 0:
        y[n:]=x[:len(x)-n]
    else:
        y[:len(x)+n] = x[-n:]
    return t, y

def add_signals(t, x1, x2):
    """
    Add wo signals sample by sample.

    Parameters:
    t : np.ndarray # time vector (returned unchanged)
    x1 : np.ndarray # first signal
    x2 : np.ndarray # second signal (same length as x1)

    Returns:
    t : np.ndarray # same time vector as input
    y : np.ndarray # x1 + x2
    """
    if len(x1) != len(x2): # not equal to
        raise ValueError ("Signals must have the same length")
    return t, x1+x2
