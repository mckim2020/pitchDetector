# code in order to analyze given data file
aNat = 'C:/Users/HOME/Desktop/2학년 1학기/performers_research/csvFiles/aNatAmp.csv'
timeList, ampList = createTimeAmpList(aNat)


# when getting results from sonic visualizer, to calibrate data between sonic vis data to time domain
for i in range(len(timeList)):
    timeList[i] = timeList[i] / 46305.66


# set interval size = 10000
newTimeList, pitchList = pitch(timeList, ampList, 10000)
plt.plot(newTimeList, pitchList)
plt.xlabel('time')
plt.ylabel('pitch')
plt.legend('Time-Pitch Graph)
plt.show()
