# Lab 10
# November 27, 2024

# problem 1
# base case: if n = 0, return 1
# recursive step: if n is not 1, return x*power(x, n-1)

def power(x, n):
    if n == 0:
        return 1
    else:
        return x*power(x, n-1)
    
print (power(2, 3))

'''
power(2, 0)
    \
    /1
power(2, 1)
    \
    /2*1
power(2, 2)
    \
    /2*2*1
power(2, 3)
    \
     \ 2*2*2*1
'''
# problem 2
def sum_digits(x):
    if x == 0:
        return 0
    else:
        return x%10 + sum_digits((int)(x/10))

print(sum_digits(123))

'''
sum_digits(0)
    \
    /0
sum_digits(1)
    \
    /1+0
sum_digits(12)
    \
    /2+1+0
sum_digits(123)
    \
     \ 3+2+1+0
'''

# problem 3
def split_list(list, element):
    res = []
    start = 0
    for i in range (len(list)):
        if list[i] == element:
            if (start != i):
                res.append(list[start:i])
            start = i+1

    if (start != len(list)):
        res.append(list[start:])

    return res

def split_list_multiple_elements(list, elements):
    for i in range(len(list)):
        if (list[i] in split_elements):
            list[i] = split_elements[0]
    return split_list(list, split_elements[0])

list = [33, 2, 3, 6, 33, 33, 25, 33, 2, 12, 3, 2, 5, 2, 1, 3, 3, 33, 5, 4, 3, 2, 1]
split_elements = [33, 3]
print (split_list_multiple_elements(list, split_elements))