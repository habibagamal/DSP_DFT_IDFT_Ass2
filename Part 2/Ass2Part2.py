import math
import cmath
import numpy as np
import matplotlib.pyplot as plt


#################
#DFT function
################
def dft(data, N):
	out = np.zeros(shape = N, dtype=np.complex_)
	for m in range (N):
		for n in range(N):
			out[m] += data[n] * ( np.cos(2 * cmath.pi * n * m / N) - (np.sin(2 * cmath.pi * n * m / N) * 1j))
	return out


#################
#Declaring constants
################
rate = 20
samples = 100
minT = 0.0
maxT = samples / rate
fundamental = float ( float(rate) / samples)
N = np.arange(0, 100)


#################
#Doing the integration and plotting its graph (NOT WORKING!!!!!!!!!!!!)
################
f = np.arange (0, 20, 1/1000.0)
x = 1.0 / (1 + (2 * np.pi * f * 1j))


plt.figure(1)
plt.plot(f , abs(x), 'r')
plt.hold()
plt.xlabel('frequency')
plt.ylabel('spectrum')
plt.grid(True)
plt.show()


#################
#doing the 100 samples for the e^(-t)
################
x1 = np.zeros(shape = 100)
for i in range (100):
	x1[i] = np.exp(-i)

#################
#doing dft and plotting the graph of part 1 (100 point DFT with 100 samples)
################
dom1 = N * fundamental
dft_out1 = dft (x1, 100)

plt.figure(2)
plt.plot(dom1 , abs(dft_out1), 'b')
plt.hold()
plt.xlabel('frequency')
plt.ylabel('spectrum')
plt.grid(True)
plt.show()


#################
#doing dft and plotting the graph of part 2 (200 point DFT with 100 samples)
################
fundamental2 = float ( float(rate) / 200.0)
N2 = np.arange (0, 200)
dom2 = N2 * fundamental2
x2 = np.pad(x1, (0,100), 'constant', constant_values=(0))
dft_out2 = dft (x2, 200)
plt.figure(3)
plt.plot(dom2 , abs(dft_out2), 'g')
plt.hold()
plt.xlabel('frequency')
plt.ylabel('spectrum')
plt.grid(True)
plt.show()

#################
#doing dft and plotting the graph of part 3 (200 point DFT with 20 samples)
################
x3 = np.zeros(shape = 20)
for i in range (20):
	x3[i] = x1[i]
x3 = np.pad(x3, (0,180), 'constant', constant_values=(0))
dft_out3 = dft (x3, 200)
plt.figure(4)
plt.plot(dom2 , abs(dft_out3), 'y')
plt.hold()
plt.xlabel('frequency')
plt.ylabel('spectrum')
plt.grid(True)
plt.show()