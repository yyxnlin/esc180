def sorted_timestamps(timestamps):
    time_count = [0]*60*24

    for i in range (len(timestamps)):
        seconds = 60*timestamps[i][0] + timestamps[i][1]
        time_count[i] = seconds

    res = []

    time_count = sorted(time_count)
    for i in range (len(time_count)):
        if (time_count[i] > 0):
            res.append([time_count[i]//60, time_count[i]%60])

    return res

print(sorted_timestamps([(5, 10), (2, 40), (22, 59), (5, 10)]))