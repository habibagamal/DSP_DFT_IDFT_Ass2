import math
import cmath
import numpy as np

def dft(x, N):
	real = np.zeros(shape = N)
	imaginary = np.zeros(shape = N)
	for m in xrange (N):
		for n in xrange (N):
			real[m] += x[n] * np.cos(2 * cmath.pi * n * m / N)  
			imaginary[m] -=  x[n] * np.sin(2 * cmath.pi * n * m / N)
	return real, imaginary

def idft(x, N):
	real = np.zeros(shape = N)
	imaginary = np.zeros(shape = N)
	print (real.shape, imaginary.shape)
	for n in xrange (N):
		for m in xrange (N):
			real[n] += x[m] * np.cos(2 * cmath.pi * n * m / N)
			imaginary[n] += x[m] * np.sin(2 * cmath.pi * n * m / N)
		real[n] /= N
		imaginary[n] /= N
	return real, imaginary


x = [0, 1, 2, 3]
real_dft, imm_dft = dft (x,4);
real_idft, imm_idft = idft(x,4)
print "Input array is: ", x
print "DFT real part is: ", real_dft
print "DFT imaginary part is: ", imm_dft
print "IDFT real part is: ", real_idft
print "IDFT imaginary part is: ", imm_idft
