# ESC180 Lab 7 (Part 2)
# November 16, 2024

import numpy as np

def print_matrix(M_lol):
    print("[", end="")
    j = 0
    for row in M_lol:
        j+=1
        print("[", end="")
        i = 0
        for val in row:
            i+=1
            if (i != len(row)):
                print (val, end = "  ")
            else:
                print(val, end="")

        if (j != len(M_lol)):
            print("]", end="\n ")
        else:
            print("]", end="")
    print("]")

def get_lead_ind(row):
    for i in range(len(row)):
        if row[i] != 0:
            return i
    return len(row)


def get_row_to_swap(M, start_i):
    i_leading = get_lead_ind(M[start_i])

    cur_row = start_i+1
    cur_leading_ind = get_lead_ind(M[start_i+1])

    for i in range (start_i+1, len(M)):
        if (get_lead_ind(M[i]) < cur_leading_ind):
            cur_leading_ind = get_lead_ind(M[i])
            cur_row = i

    if (cur_leading_ind > i_leading):
       return cur_row
    else:
        return -1


def add_rows_coefs(r1, c1, r2, c2):
    res = []

    res.append((np.array(r1)*c1).tolist())
    res.append((np.array(r2)*c2).tolist())

    return res


def eliminate(M, row_to_sub, best_lead_ind):

    for i in range(best_lead_ind, len(M)):
        multiple = M[i][get_lead_ind(M[row_to_sub])]/M[row_to_sub][get_lead_ind(M[row_to_sub])]
        # print(multiple)
        M[i] = (np.subtract(np.array(M[i]), multiple*np.array(M[row_to_sub]))).tolist()


def forward_step(M):
    for i in range(len(M)-1):
        swapped_row = get_row_to_swap(M, i)
        if (swapped_row == -1):
            continue
        M[i], M[swapped_row] = M[swapped_row], M[i]
        # print ("Leading:", get_lead_ind(M[i]))
        eliminate(M, i, get_lead_ind(M[i]))
        print_matrix(M)




# Convert a list of lists into an array:
M_listoflists = [[1,-2,3],[3,10,1],[1,5,3]]
M = np.array(M_listoflists)
# Now print it:
# print(M)

#Compute M*x for matrix M and vector x by using
#dot. To do that, we need to obtain arrays
#M and x
M = np.array([[1,-2,3],[3,10,1],[1,5,3]])
x = np.array([75,10,-11])
b = np.matmul(M,x)        

M = np.array([[0, 0, 1, 0, 2],
            [1, 0, 2, 3, 4],
            [3, 0, 4, 2, 1],
            [1, 0, 1, 1, 2]])

# print(M)
#[[ 1 -2  3]
# [ 3 10  1]
# [ 1  5  3]]

# To obtain a list of lists from the array M, we use .tolist()
M_listoflists = M.tolist() 

# print(M_listoflists) #[[1, -2, 3], [3, 10, 1], [1, 5, 3]]
print_matrix(M_listoflists)
# print(get_lead_ind(M_listoflists[0]))

# print(get_row_to_swap(M, 1))
# print (add_rows_coefs(M_listoflists[0], 2, M_listoflists[1], 3))

print ("\n\nPost elimination:")
eliminate(M, 1, 2)
M_listoflists = M.tolist() 
print_matrix(M_listoflists)


# print ("\n\nPost forward step:")
# forward_step(M)
# M_listoflists = M.tolist() 
# print_matrix(M_listoflists)