from signals import generate_sine_wave

if __name__ == "__main__":
    frequency = 5
    duration = 2
    sample_rate = 100
    t, x = generate_sine_wave(frequency, duration, sample_rate)

print("First 10 time samples:", t[:10])
print("First 10 signal samples:", x[:10])

