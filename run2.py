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
from signals2 import generate_square

amplitude = 1.0
duty = 0.5
t2, x2 = generate_square(frequency, duration, sample_rate, amplitude=amplitude, duty=duty)
plt.plot(t2, x2, drawstyle="steps-post")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.title("Square wave")
plt.grid(True)
plt.show()