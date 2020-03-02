# return most often frequency
def maxFreq(x, y):
    freq = 0
    max = 0

    for i in range(len(x)):
        if y[i] > max:
            freq = x[i]
            max = y[i]

    return freq
