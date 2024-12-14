def selection_sort(L):
    for i in range(len(L) - 1):
        cur_max = L[i]

        for j in range (0, i):
            if L[j] > cur_max:
                L[i], L[j] = L[j], L[i]
                cur_max = L[i]

L = [5, 10, 23, 1, 5, 34, 23]
selection_sort(L)
print(L)