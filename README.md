# Morse Learning Machine Challenge - v2
[Kaggle Chakkenge Link](https://www.kaggle.com/c/morse-learning-machine-challenge-v2)
-  比赛源地址提供了基本的代码py2，我转成了py3当然这个效果不是很好
- CW初学者手册.txt是用来熟悉一下moorse的背景资料
- 有空得了解一下数字信号处理的内容

## Data Description
### CSV FILE
The "SampleSubmission.csv" contains both Training set and Validation set, 200 rows in total. Training set has "Prediction" field content pre-populated and this is to be used for training. Validation set has blank "Prediction" field - this needs to predicted by your Morse learning machine. You need to submit the entire file to this Kaggle competition.
### AUDIO FILES
Each audio file contains random Morse code with letters A..Z and numerals 0...9 and punctuation .?/ as defined in http://en.wikipedia.org/wiki/Morse_code. Audio files are in WAV format ( mono, 32 bit float, 8 kHz sampling rate). Morse signal (null beat) is between 600 ...1200 Hz in the computer generated files. Signal-to-noise ratio (SNR) varies randomly between -14 dB ... +20 dB per file. Morse speed varies randomly between 12 ... 80 WPM per file. Audio files are named cwNNN.wav where NNN is a number 001 ... 200. File size varies between 145 to 2100 kBytes.
### File descriptions
- audio.zip - contains 200 audio .WAV files
- sampleSubmission.csv - a sample submission file in the correct format
- Levenshtein.py - supplemental Python file that calculates Levenshtein distance between two text files divided by number of characters in the first file. You can use this for your own testing purposes. 
- morse.py - supplemental Python file that contains experimental Morse decoder software. This is meant for you to get started if you haven't worked on Morse decoding problem before. This software is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

2017.12.26

