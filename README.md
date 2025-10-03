# Signals and Systems with python

Project for generating and manipulating basic signals and plotting them

# Requirements 
    1) NumPy
    2) Matplotlib

# Notes
    1) Change parameters (frequency, duration, sample_rate, amplitude, duty, tau) directly in "run2.py"
    2) Square waves are plotted with drawstyle="steps-post" so they look rectangular
    3) All signal generation functions are in "signals2.py", plotting happens in "run2.py"

# Whats inside the files
    signals2.py:
        1) generate_sine_wave(frequency, duration, sample_rate)
        2) generate_square(frequency, duration, sample_rate, amplitude=1.0, duty=0.5)
        3) time_shift(t, x, shift_seconds, sample_rate), y(t)=x(t - τ)
        4) add_signals(t, x1, x2)
    run2.py:
        1) plots a sine wave
        2) plots a square wave
        3) plots square and its time shifted version
        4) adds two sines and plots the result

