#Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# time axis
t = np.linspace(0, 1, 1000)

# signal parameters
amplitude = int(input("Enter amplitude: "))
frequency = int(input("Enter frequency (Hz): "))

# sine wave signal
#SIGNAL = A * sin(2 * pi * f * t) = A * sin(2πft)
signal = amplitude * np.sin(2 * np.pi * frequency * t)

# plot
plt.figure()
plt.plot(t, signal)

plt.title("Signal Visualizer - Sine Wave")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)

plt.show()