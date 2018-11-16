from scipy.io import wavfile
import math
import cmath
import numpy as np
import matplotlib.pyplot as plt


###########
#DFT function
############
def dft(data, N):
	out = np.zeros(shape = N, dtype=np.complex_)
	for m in range (N):
		for n in range(N):
			out[m] += data[n] * ( np.cos(2 * cmath.pi * n * m / N) - (np.sin(2 * cmath.pi * n * m / N) * 1j))
	return out


###########
#IDFT function
############
def idft(x, N):
	out = np.zeros(shape = N, dtype=np.complex_)
	for n in xrange (N):
		for m in xrange (N):
			out [n] += x[m] * (np.cos(2 * cmath.pi * n * m / N) + (np.sin(2 * cmath.pi * n * m / N) * 1j))
		out[n] /= N
	return out


# ##########
# #Trying idft and dft on a small signal
# ###########
# x = [0, 1, 2, 3]
# dft_out = dft (x,4)
# print "My DFT output: ", dft_out
# print "Numpy dft output: ", np.fft.fft(x)
# idft_out = idft(dft_out,4)
# print "My idft output: ", idft_out
# print "Numpy idft output: ", np.fft.ifft(np.fft.fft(x))
# mag = abs(dft_out)
# print "My Magnitude is: ", mag
# t1 = np.linspace(0.0,1.0,4)

# ##########
# #Trying wav file generation for small file
# ###########
# wavIn = np.zeros(shape = 4)
# print t1
# wavIn = idft_out.real.astype(np.int16) 
# print wavIn
# wavfile.write("output1.wav", 4, wavIn)


###########
#Reading from wav file
############
rate, data = wavfile.read("try4.wav")

# ###########
# #GETTING THE DFT AND ITS MAGNITUDE
# ############
DFT = dft (data, rate)
magnitude = abs(DFT)


###########
#Plotting the magnitude 
############
t = np.linspace(0.0,1.0,rate)
plt.figure(1)
plt.plot(t , magnitude)
plt.xlabel('Time')
plt.ylabel('Magnitude')
plt.grid(True)
plt.show()


# ###########
# #GETTING THE IDFT AND DOING THE OUTPUT WAV FILE
# ############
IDFT = idft(DFT, rate)
wavfile.write("output.wav", rate, IDFT.real)
