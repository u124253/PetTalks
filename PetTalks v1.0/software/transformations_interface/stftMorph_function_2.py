# function for doing a morph between two sounds using the stft

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import get_window
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../models/'))
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../transformations/'))
import stft as STFT
import utilFunctions as UF
import stftTransformations as STFTT

def main(inputFile1='../../software/sounds/ocean.wav', inputFile2='../../software/sounds/speech-male.wav', window1='hamming',  window2='hamming',
	M1=1024, M2=1024, N1=1024, N2=1024, H1=256, smoothf = .5, balancef = 0.5):
	"""
	Function to perform a morph between two sounds
	inputFile1: name of input sound file to be used as source
	inputFile2: name of input sound file to be used as filter
	window1 and window2: windows for both files
	M1 and M2: window sizes for both files
	N1 and N2: fft sizes for both sounds
	H1: hop size for sound 1 (the one for sound 2 is computed automatically)
	smoothf: smoothing factor to be applyed to magnitude spectrum of sound 2 before morphing
	balancef: balance factor between booth sounds, 0 is sound 1 and 1 is sound 2
	"""

	# read input sounds                
	(fs, x1) = UF.wavread(inputFile1)
	(fs, x2) = UF.wavread(inputFile2)    #totalmente

	# compute analysis windows
	w1 = get_window(window1, M1)
	w2 = get_window(window2, M2)

	# perform morphing
	y = STFTT.stftMorph(x1, x2, fs, w1, N1, w2, N2, H1, smoothf, balancef)

	# write output sound
	outputFile = 'output_sounds/' + os.path.basename(inputFile1)[:-4] + '_stftMorph.wav'
	UF.wavwrite(y, fs, outputFile)


if __name__ == '__main__':
	main(inputFile1='../../software/sounds/ocean.wav', inputFile2='../../software/sounds/speech-male.wav', smoothf = .5, balancef = 0.5)
