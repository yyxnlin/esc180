# def h(L):
#     L[1] = [7, 8]
#     L[0] = [5, 6]
#     L[0][0] = 9
#     L[2] = 5
#     L[0] = 3
#     print(L)
# L = [[1, 2], [3, 4], 3]
# h(L)
# print(L)

# print("*****")
# def f(L):
#     L = [3]
#     print(L)
# L = [5]
# f(L)
# print(L)


# L = [[[1, 2], [3, 4]]]
# L1 = L[:]
# L1[0][0] = 5
# L1[0][1][0] = 6
# print(L1)
# print(L)


# print()
# print()



# print()
# print()

# L = [12, 13]
# M = L[:]
# M[0] = 5
# M[1] = 5
# print(M)
# print(L)

# L = [[1, 2], 3]
# M = L[:]
# M[0][1] = 5
# M[1] = 6
# print(M)
# print(L)



# L = [[1, 2], [3, 4], 2]
# M = L[:]
# M[1] = [7, 8]
# M[0].extend([5, 6])
# M[0][0] = 9
# M[1] = 5
# print(M)
# print(L)


# def greeting(st):
#     global s
#     s = "Happy " + st
# s = ""
# print(s)
# res = greeting("meow")
# print(s)



# def g(n):
#     res = []

#     for i in range((int)(n**0.5)+1):
#         res.append(i**2)
#     return res

# print(g(35))



# def matrix_sum(A, B):
#     if (len(A) != len(B) or len(A[0]) != len(B[0])):
#         return "ERROR"
#     res = []

#     for i in range (len(A)):
#         row = []
#         for j in range(len(A[i])):
#             row.append(A[i][j] + B[i][j])
#         res.append(row)
#     return res

# print(matrix_sum([[5, 5, 0], [6, 6, 2]], [[1, 2, 3], [4, 5, 6]]))




# import math
# digit = 0
# def next_digit_pi():
#     global digit
#     res = (int)((math.pi * (10**digit)) % 10)
#     digit += 1
#     return res

# print(next_digit_pi())
# print(next_digit_pi())
# print(next_digit_pi())
# print(next_digit_pi())
# print(next_digit_pi())
# print(next_digit_pi())



# print (3.14%1)


# def near_anagram(s1, s2):
#     # diff1_2 = 0
#     # diff2_1 = 0
#     # for c in set(s1+s2):
#     #     if s1.count(c)-s2.count(c) == 1:
#     #         diff1_2 += 1
#     #     elif s1.count(c)-s2.count(c) == -1:
#     #         diff2_1 += 1
#     #     elif abs(s1.count(c)-s2.count(c)) > 1:
#     #         return False
#     # return diff1_2 == diff2_1 == 1


#     count = len(s2)
#     for i in range(len(s2)):
#         j = 0

#         while (j<len(s1)):
#             if (s2[i] == s1[j]):
#                 s1 = s1[0:j] + s1[j+1:]
#                 j-=1
#                 count-=1
#                 break
#             j+=1
    
#     if count == len(s1) == 1:
#         return True
#     return False





# print (near_anagram("cat", "tap"))
# print (near_anagram("tacocat", "cattaco"))



def doubler(L):
    dL = L[:]
    for index in range(len(dL)):
        dL[index] = dL[index] * 2
    print(dL)
    print (L)
my_list = [1, 2, 3]
doubler(my_list)
print(my_list)