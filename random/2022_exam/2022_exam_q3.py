def top10requests(requests):
    dict = {}

    for item in requests:
        if item in dict.keys():
            dict[item] += 1
        else:
            dict[item] = 1
    
    counts=[]

    for item, count in dict.items():
        counts.append((count, item))
    
    counts.sort()

    res = []
    for i in range (-1, -11, -1):
        res.append(counts[i][1])

    return sorted(res)

requests = ["socks", "calculus textbook", "calculator", "A+ in ESC180", "socks", "socks", "calculator", "a", "b", "c", "d", "e", "f"]
print(top10requests(requests))