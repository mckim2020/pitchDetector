import numpy as np
import csv
import matplotlib.pyplot as plt
import scipy.fftpack


# returns time interval of sampled csv file
def interval(timeList):
    return abs(timeList[-1] - timeList[0])/(len(timeList) - 1)


# returns freq distribution
# r indicates interval of frequency you would like to focus on
# ie) r = 100 means focusing on 0~400Hz interval
def plotFreq(timeList, ampList, r):
    # number of sample points
    n = len(timeList)

    # sample spacing
    ts = interval(timeList)
    x = y = np.linspace(0.0, n*ts, n)
    for i in range(len(y)):
        y[i] = ampList[i]
    # apply FFT: Nyquist interval --> [-0.5*fs, 0.5fs]
    # basically a DFT
    xf = np.linspace(0, 1/(r*ts), n//r)
    yf = scipy.fftpack.fft(y)

    return xf, yf


# makes timeList and pitchList
def createTimeAmpList(fileName):
    timeList = []
    ampList = []

    # open file
    f = open(fileName, 'r')

    # append until end comes
    count = 0
    for line in f:
        a, b = line.split(',')
        count += 1
        a = a.strip()
        b = b.strip()
        if b == '*':
            break
        timeList.append(float(a))
        ampList.append(float(b))
    # f.close()
    return timeList, ampList


# return most often frequency
def maxFreq(x, y):
    freq = 0
    max = 0

    for i in range(len(x)):
        if y[i] > max:
            freq = x[i]
            max = y[i]

    return freq


# return pitchList
# r indicates how rapid you will sample/test your mp3(data) file: same as plotFreq function's r value
def pitch(timeList, ampList, n, r):
    newTimeList = []
    pitchList = []
    chunks = [timeList[x:x+n] for x in range(0, len(timeList), n)]
    # following chunks may run on your computer but not mine: less noise
    # chunks = [timeList[x:x + n] for x in range(0, len(timeList) - n-1)]
    amps = [ampList[x:x+n] for x in range(0, len(ampList), n)]
    for i in range(len(chunks)):
        newTimeList.append(chunks[i][len(chunks[i]) // 2])
        xf, yf = plotFreq(chunks[i], amps[i], r)
        pitch = maxFreq(xf, yf)
        pitchList.append(pitch)

    return newTimeList, pitchList



