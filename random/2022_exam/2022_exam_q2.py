def my_median(L):
    cur_ind = 0

    while cur_ind < len(L):
        cur_min = L[cur_ind]
        cur_min_ind = cur_ind

        for i in range (cur_ind + 1, len(L)):
            if L[i] < cur_min:
                cur_min_ind = i
                cur_min = L[i]

        temp = L[cur_ind]
        L[cur_ind] = cur_min
        L[cur_min_ind] = temp
        cur_ind += 1
    return L[len(L)//2]


print(my_median([5.0, 2.0, 4.0, 1.0, 3.0]))