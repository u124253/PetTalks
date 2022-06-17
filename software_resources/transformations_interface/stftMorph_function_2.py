# function for doing a morph between two sounds_resources using the stft

from scipy.signal import get_window
import sys, os
from pathlib import Path

path = str(Path(os.path.abspath(__file__)).parent)
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../models/'))
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../transformations/'))

import utilFunctions as UF
import stftTransformations as STFTT

def main(inputFile1, inputFile2, window1='hamming',  window2='hamming',
	M1=1024, M2=1024, N1=1024, N2=1024, H1=256, smoothf = .5, balancef = 0.5):

	"""
	Function to perform a morph between two sounds_resources
	inputFile1: name of input sound file to be used as source
	inputFile2: name of input sound file to be used as filter
	window1 and window2: windows for both files
	M1 and M2: window sizes for both files
	N1 and N2: fft sizes for both sounds_resources
	H1: hop size for sound 1 (the one for sound 2 is computed automatically)
	smoothf: smoothing factor to be applyed to magnitude spectrum of sound 2 before morphing
	balancef: balance factor between booth sounds_resources, 0 is sound 1 and 1 is sound 2
	"""

	# read input sounds_resources
	(fs, x1) = UF.wavread(inputFile1)
	(fs, x2) = UF.wavread(inputFile2)

	# compute analysis windows
	w1 = get_window(window1, M1)
	w2 = get_window(window2, M2)

	# perform morphing
	y = STFTT.stftMorph(x1, x2, fs, w1, N1, w2, N2, H1, smoothf, balancef)

	# write output sound
	name_Inputfile1 = inputFile1.split('/')[-1].split('.')[0]
	name_Inputfile2 = inputFile2.split('/')[-1].split('.')[0]
	outputFile = path + '/Temp/' + os.path.basename("petTalks_" + name_Inputfile1 + '_'+name_Inputfile2 + ".wav")
	UF.wavwrite(y, fs, outputFile)
	#Play file
	UF.wavplay(path + '/Temp/' + os.path.basename("petTalks_" + name_Inputfile1 + '_'+name_Inputfile2 + ".wav"))
	return y
if __name__ == '__main__':
	main()
