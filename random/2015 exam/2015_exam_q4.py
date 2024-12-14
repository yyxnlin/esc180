def merge(L1, L2):
    if len(L1) == 0:
        return L2
    elif len(L2) == 0:
        return L1
    if L1[0] > L2[0]:
        return [L2[0]] + merge(L1, L2[1:])
    else:
        return [L1[0]] + merge(L1[1:], L2)

print(merge([4, 8, 10], [2, 5]))