# pitchDetector
This program can detect pitches from mp3 files and its purpose is to convert time - amplitude data file into time - pitch file

# Library Usages
SciPy, NumPy, matplotlib.pyplot

# Intro
variables: n, k, timeList, amplitudeList(ampList)
n: Number of time intervals needed for each FFT
k: Range of frequency to focus on 
timeList&amplitudeList: csv file format(loaded from Sonic Visualizer)

# +++
Sonic Visualizer's time data needs initial calibration
