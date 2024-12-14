def get_repeating_ints(L):
    unique = []
    dup = []

    for i in range (len(L)):
        if L[i] in unique:
            if L[i] not in dup:
                dup.append(L[i])
        else:
            unique.append(L[i])
    dup = sorted(dup)
    return dup


print(get_repeating_ints([6, 7, 6, 5, 1, 5, 6]))