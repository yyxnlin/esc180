# def add_sparse_matrices(A, B, dim):
#   res = []
#   for i in range(dim[0]):
#     res.append([0] * dim[1])

#   for coords, value in A.items():
#     res[coords[0]][coords[1]] += value

#   for coords, value in B.items():
#     res[coords[0]][coords[1]] += value

#   return res

# result = add_sparse_matrices({(0, 0): 5, (1, 2): 1}, {(0, 0):5}, (2, 3))
# print(result)



# last=""
# last_2=""
# last_3=""

# def unlock(input):
#     global last, last_2, last_3
    
#     if (input == "pumpkin"):
#         if (last == "costumes" and last_2 == "costumes" and last_3 == "fall"):
#             last, last_2, last_3 = input, last, last_2
#             print ("unlocked")
#             return
#     last, last_2, last_3 = input, last, last_2
#     print("locked")
#     return

# unlock("ghosts") # returns "locked"
# unlock("leaves") # returns "locked"
# unlock("fall") # returns "locked"
# unlock("costumes") # returns "locked"
# unlock("costumes") # returns "locked"
# unlock("pumpkin") # returns "unlocked"
# unlock("pumpkin") # returns "locked"
# unlock("fall") # returns "locked"
# unlock("costumes") # returns "locked"
# unlock("costumes") # returns "locked"
# unlock("pumpkin") # returns "unlocked"
# unlock("fall") # returns "locked"





# def h(L):
#     L[1] = [7, 8]
#     L[0] = [5, 6]
#     L[0][0] = 9
#     print(L)

# L = [[1, 2], [3, 4]]
# h(L)
# print(L)



# L = [[[1, 2], [3, 4], [10, 11]]]
# L1 = L[0:1]
# L1[0][0] = 5
# L1[0][1][0] = 6
# print(L1)
# print(L)



# def sum_cubes_num_terms(n):
#     res = 0
#     k = 0
#     while res < n:
#         k += 1
#         res += k**3
#     return k

# print(sum_cubes_num_terms(25))



# def moving_average(measurements):
#     res = []
#     for i in range(len(measurements)-2):
#         res.append((measurements[i] + measurements[i+1] + measurements[i+2])/3)
#     return res

# print (moving_average([2, 5, 3, 4, 5, 2, 3, 4, 3, 87, 9]))



# def match(pattern, text):
#     i=0
#     j=0

#     while (i <= len(pattern) -1):
#         if (text[j%len(text)] == pattern[i]):
#             i+=1
#         else:
#             i=0
#         j+=1
#         if (i == 0 and j >= len(text)):
#             return False
#     return True


# print (match("abc", "abcd"))
# print (match("abc", "ee3abcd"))
# print (match("abc", "ee3abdcd"))
# print (match("abc", "cee3abdcdab"))
# print (match("abdcdabcee3ab", "cee3abdcdab"))


def share_n1(M1, M2):
    M1_columns = []

    for i in range(len(M1[0])):
        col = []
        for j in range(len(M1)):
            col.append(M1[j][i])
        M1_columns.append(col)

    count = 0
    for i in range(len(M2[0])):
        col = []
        for j in range(len(M2)):
            col.append(M2[j][i])
        for i in range(len(M1_columns)):
            if(col == M1_columns[i]):
                count += 1
    if (count >= len(M1[0])-1):
        return True
    return False

M1 = [[1, 2, 4],
      [1, 5, 1],
      [1, 2, 2]]

M2 = [[3, 1, 0],
      [1, 1, 2],
      [2, 1, 0]]

print (share_n1(M1, M2))