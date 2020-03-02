# code in order to analyze given data file
aNat = 'aNatAmp.txt'
timeList, ampList = createTimeAmpList(aNat)


# when getting results from sonic visualizer, to calibrate data between sonic vis data to time domain
for i in range(len(timeList)):
    timeList[i] = timeList[i] / 46305.66


# set interval size = 10000
# r = 100: f range = 0-499Hz
# r = 50: f range = 0-1000Hz 
#880 Hz is the highest pitch in orchestra(instruments)
newTimeList, pitchList = pitch(timeList, ampList, 10000, 50)
plt.plot(newTimeList, pitchList)
plt.xlabel('time')
plt.ylabel('pitch')
plt.legend('Time-Pitch Graph)
plt.show()
