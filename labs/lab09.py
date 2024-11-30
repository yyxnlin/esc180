# Lab 9
# November 20, 2024

import copy
import time

# q1
# (a)
def make_lower(s):
    return(s.lower())

# s = "HI"
# s = make_lower(s)
# print (s)

# (b)
def changeList(L):
    L[2] = 5555
    return L

def changeList2(L):
    L = [1, 2, 2222]
    return L

# L = [1, 2, 3]
# print (id(L))
# # changeList(L)
# L = changeList(L) # will not change id
# print(L)
# print (id(L))

# # cannot just do changeList2(L)
# L = changeList2(L) # will change id
# print(L)
# print (id(L))

# (c)

def changeDict(d):
    d["dog"][1] = 1000
    return d


# L = [1, 2]
# dict = {"dog":L, "pig":"oink", "cow":"moo"}

# print("dict1:", dict)
# print("dict1:", id(dict))
# dict2 = dict.copy()
# print("dict2:", id(dict2)) # different id
# # changeDict(dict)
# changeDict(dict2)
# print("dict1:", dict) # dog:[1, 1000] will appear (instead of 1, 2)
# print("dict1:", id(dict)) # id will not change



# (d)
# L = [1, 2]
# dict = {"dog":L, "pig":"oink", "cow":"moo"}

# print("dict1:", dict)
# print("dict1:", id(dict))
# dict2 = copy.deepcopy(dict)
# print("dict2:", id(dict2)) # different id
# # changeDict(dict)
# changeDict(dict2)
# print("dict1:", dict) # dog:[1, 2] will appear (dict1 will not change)
# print("dict2:", dict2) # dog:[1, 1000] will appear (only dict2 changes)
# print("dict1:", id(dict)) # id will not change



# q2
def binary_search(L, e):
    low = 0
    high = len(L)-1
    count = 0
    while high-low >= 2:
        count += 1
        mid = (low+high)//2 #e.g. 7//2 == 3
        if L[mid] > e:
            high = mid-1
        elif L[mid] < e:
            low = mid+1
        else:
            return mid, count
    if L[low] == e:
        return low, count
    elif L[high] == e:
            return high, count
    else:
        return None, count

# print(binary_search([1, 35, 45, 12, 4, 23], 12))

# part c: if e is at middle of each list, it is most efficient

# (d)

# L = []
# for i in range (11):
#     L.append(i)

# print(10, binary_search(L, 0)[1])

# for i in range (101):
#     L.append(i)
# print(100, binary_search(L, 1)[1])

# for i in range (1001):
#     L.append(i)
# print(1000, binary_search(L, 0)[1])


# for i in range (10001):
#     L.append(i)
# print(10000, binary_search(L, 1)[1])

# for i in range (100001):
#     L.append(i)
# print(100000, binary_search(L, 5)[1])

# for i in range (1000001):
#     L.append(i)
# print(1000000, binary_search(L, 5)[1])


# for i in range (10000001):
#     L.append(i)
# print(10000000, binary_search(L, 1)[1])


# (e)
def print_results(L, e):
    start_time = time.clock()
    res = binary_search(L, e)
    end_time = time.clock()
    print(res, end=" ")
    print("Time:", end_time-start_time)


L = []
for i in range (11):
    L.append(i)

print_results(L, 0)

for i in range (101):
    L.append(i)
print_results(L, 1)

for i in range (1001):
    L.append(i)
print_results(L, 0)


for i in range (10001):
    L.append(i)
print_results(L, 1)

for i in range (100001):
    L.append(i)
print_results(L, 5)

for i in range (1000001):
    L.append(i)
print_results(L, 5)

for i in range (10000001):
    L.append(i)
print_results(L, 1)
