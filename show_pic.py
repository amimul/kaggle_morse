# Beat tracking example
# from __future__ import print_function
import librosa
import matplotlib.pyplot as plt
import librosa.display
import numpy as np

# 1. Get the file path to the included audio example
# Sonify detected beat events
y, sr = librosa.load('audio/cw178.wav',sr=None)
#y,sr=librosa.load(librosa.util.example_audio_file())

# sr=900
# y=y1[10:910]

# plt.subplot(2,1,1)
# librosa.display.waveplot(y,sr)
#
# plt.subplot(2,1,2)
D = librosa.amplitude_to_db(librosa.stft(y, n_fft=512, hop_length=100, win_length=512), ref=np.max)
librosa.display.specshow(D, x_axis='time',y_axis='log')
plt.colorbar(format='%+2.0f dB')
plt.title('Linear-frequency power spectrogram')
plt.show()
'''
y : np.ndarray [shape=(n,)] or None
        audio time series

    sr : number > 0 [scalar]
        sampling rate of `y`
'''
