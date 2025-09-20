import numpy as np
def generate_sine_wave(frequency: float, duration: float, sample_rate: int)
    """
    Generate sin wave. 

    Parameters
    ----------
    frequency : float   # Hz
    duration  : float   # seconds
    sample_rate: int    # samples per second

    Returns
    -------
    t : np.ndarray  # time vector, shape (N,)
    x : np.ndarray  # samples, shape (N,)
    """
    N = int(duration * sample_rate)         # total number of samples
    
