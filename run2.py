"""
Generates a sine wave, prints first 10 samples, and plots it.
Generates a square wave, plots it, then plots a time-shifted version.
Generates two sines and plots their sum.

Parameters:
Set as variables in the script:
frequency, duration, sample_rate, amplitude, duty, tau, f1, f2.

Returns:
None
"""

from signals2 import generate_sine_wave
import matplotlib.pyplot as plt

frequency = 5 
duration = 2
sample_rate = 100
t, x = generate_sine_wave(frequency, duration, sample_rate)

print("First 10 time samples:", t[:10])
print("First 10 signal samples:", x[:10])

plt.plot(t, x)
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.title("5 Hz sine, 2 s, 100 Hz sampling")
plt.grid(True)
plt.show()

# Square function
from signals2 import generate_square, time_shift

amplitude = 1.0
duty = 0.5
t2, x2 = generate_square(frequency, duration, sample_rate, amplitude=amplitude, duty=duty)
tau = 0.2
_,x2_shift = time_shift(t2,x2, shift_seconds=tau, sample_rate=sample_rate)

plt.plot(t2, x2, drawstyle="steps-post")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.title("Square wave")
plt.grid(True)
plt.show()

plt.plot(t2, x2, drawstyle="steps-post", label="original")
plt.plot(t2, x2_shift, drawstyle="steps-post", label=f"shift +{tau}s")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.title("Square wave with time shift")
plt.grid(True)
plt.legend()
plt.show()

from signals2 import add_signals
f1 = 5
f2 = 12
t,x1 = generate_sine_wave(f1, duration, sample_rate)
_, x2 = generate_sine_wave(f2, duration, sample_rate)
_, y = add_signals(t, x1, x2)

plt.figure()
plt.plot(t, x1, label=f"{f1} Hz")
plt.plot(t, x2, label=f"{f2} Hz")
plt.plot(t, y,  label="sum", linewidth=2)
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.title("Addition of two sines")
plt.grid(True)
plt.legend()
plt.show()