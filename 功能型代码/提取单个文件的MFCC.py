import scipy.io.wavfile as wav
import numpy as np
from python_speech_features import mfcc


fs1, audio1 = wav.read("Z2002284552.wav")

feature_mfcc1 = mfcc(audio1, samplerate=fs1,winlen=0.025, winstep=0.01,
                           nfilt=26, nfft=512, lowfreq=0, highfreq=None, preemph=0.97)

print(feature_mfcc1)
print(feature_mfcc1.shape)
np.savetxt('mfcc.csv', feature_mfcc1, delimiter= ',')