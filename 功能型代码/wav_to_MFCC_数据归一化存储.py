# This python script preforms an MFCC analysis of every .wav file in a specified directory and saves the filterbank
# energies for each file in a new directory (as a .csv).
#
# Please note: running this script multiple times will overwrite earlier analyses
#
# Requires python_speech_features. Documentation: https://github.com/jameslyons/python_speech_features)
# Requires scipy. Scipy documentation: https://www.scipy.org/install.html
#
# Script written by Rachael Tatman (rachael.tatman@gmail.com), supported by National Science Foundation grant DGE-1256082

# import things we're going to need
from python_speech_features import mfcc
from python_speech_features import logfbank
import scipy.io.wavfile as wav
import numpy
from sklearn import preprocessing
import os

# directory where we your .wav files are
directoryName = "F:/LMX/Wave/Data/1_正常" # put your own directory here
# directory to put our results in, you can change the name if you like
resultsDirectory = directoryName + "/1_MFCC_to1_results"

# make a new folder in this directory to save our results in
if not os.path.exists(resultsDirectory):
    os.makedirs(resultsDirectory)

# get MFCCs for every .wav file in our specified directory
for filename in os.listdir(directoryName):
    if filename.endswith('.wav'): # only get MFCCs from .wavs
        # read in our file
        (rate,sig) = wav.read(directoryName + "/" +filename)

        # get mfcc
        mfcc_feat = mfcc(sig,rate)
        data_normal = preprocessing.scale(mfcc_feat)

        # get filterbank energies
        fbank_feat = logfbank(sig,rate)

        # create a file to save our results in
        outputFile = resultsDirectory + "/" + os.path.splitext(filename)[0] + ".csv"
        file = open(outputFile, 'w+') # make file/over write existing file
        numpy.savetxt(file, data_normal, delimiter=",") #save MFCCs as .csv
        file.close() # close file

