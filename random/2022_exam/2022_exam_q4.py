def every_third(L):
    if len(L) < 3:
        return []
    
    res = every_third(L[3:])
    return ([L[2]] + res)

print(every_third([5, 6, 7, 12, 0, 4, 6]))