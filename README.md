# Signals and Systems with python

Project for generating, manipulating and testing basic signals and plotting them

# Project metadata

This repo uses a `pyproject.toml` to declare the build system and dependencies.

# Requirements 
    To run the project:
        1) Python 
        2) NumPy
        3) Matplotlib
    To run tests:
        1) pytest

# Notes
    1) Change parameters (frequency, duration, sample_rate, amplitude, duty, tau) directly in "run2.py"
    2) File roles:
        - "signals2.py" -> all functions (generate & modify signals)
        - "run2.py" -> imports functions and makes plots
        - "test.py" -> pytest checks for each function
    3) Square waves are plotted with drawstyle="steps-post" so they look rectangular
    

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
    test.py:
        1) test_generate_sine_wave()
           - right length, starts at 0, hits +1 at quarter period
           - empty arrays when duration = 0
        2) test_generate_square()
           - values are only ±amplitude
           - share of +amplitude ≈ duty
           - empty arrays when duration = 0
        3) test_time_shift()
           - positive shift -> leading zeros, rest matches original
           - negative shift -> trailing zeros, rest matches original
        4) test_add_signals()
           - time unchanged; sum equals x1 + x2
           - error if signal lengths differ

