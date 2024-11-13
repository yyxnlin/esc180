# ESC180 Lab 5
# October 9, 2024

import random

# problem 1
# def sum_nums(L):
#     s = 0
#     for num in L:
#         s += num
#     return s


# def count_evens(L):
#     even_count = 0
#     for num in L:
#         if (num % 2 == 0):
#             even_count+=1
#     return even_count

# if (__name__ == '__main__'):
#     print(count_evens([3, 5, 4, 3, 2]))



# # problem 2
# def list_to_str(lis):
#    string = '['


#    for i in range(len(lis)):
#        if i != (len(lis) - 1):
#            string += str(lis[i]) + ", "
#        else:
#            string += str(lis[i]) + "]"


#    return string


# print(list_to_str([1, 2, 3]))


# # problem 3
# def lists_are_the_same(list1, list2):
#    small_l = []
#    if len(list1) <= len(list2):
#        small_l = list1
#    else:
#        small_l = list2
#    for i in range(len(small_l)):
#        if list1[i] != list2[i]:
#            return False
#    return True


# # problem 4
# def list1_start_with_list2(list1, list2):
#    sum = 0


#    if len(list1) >= len(list2):
#        for i in range(len(list2)):
#            if list1[i] == list2[i]:
#                sum += 1


#        if sum == len(list2):
#            return True
#    return False




# problem 5
def match_pattern(list1, list2):
    count = 0
    for i in range (len(list1)):
        if (list1[i] == list2[count]):
            count+=1
            if (count == len(list2)):
                return True
        else:
            count = 0
    
    return False

if (__name__ == '__main__'):
    print(match_pattern([4, 10, 2, 3, 50, 100], [3, 50, 100]))



# problem 6
# def duplicates(list0):
#    adjacent = 0


#    for i in range(len(list0)):
#        if list0[i] == list0[i+1]:
#            adjacent += 1


#        if adjacent >= 2:
#            return True
#    return False


# question 7
# (a)

def find_avg(list, i):
    velocity = 0

    if (i >= 2 and i <= len(list)-3):
        velocity = (list[i+1] - list[i-1])/0.2 + (list[i+2] - list[i-2])/0.4

    elif (i == 1 or i == len(list)-2):
        velocity = (list[i+1] - list[i-1])/0.2

    elif (i == 0):
        velocity = (list[1] - list[0])/0.1

    elif (i == len(list)-1):
        velocity = (list[i] - list[i-1])/0.1

    else:
        return None

    return velocity

# print (find_avg([8, 7, 6, 5, 4, 3, 2, 1], 2))

# (b)
list = []
for i in range (10):
    list.append(0.1*random.randint(1, 100))
print(list)


i = 3
print ("weighted: ", find_avg(list, i))
print ("simple: ", (list[i+1] - list[i-1])/0.2)
