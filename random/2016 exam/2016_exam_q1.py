def insert(L, e):
    done = False
    list = []

    for i in range(len(L)):
        if (L[i] > e):
            list.extend(L[0:i])
            list.append(e)
            list.extend(L[i:])
            done = True
            break
    
    if not done:
        list = L[:] + [e]

    return list

print(insert([4, 6, 8, 15], 16))