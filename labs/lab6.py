# ESC180 Lab 6 (Part 1)
# October 16, 2024

import sys

# # problem 1
# L = [["CIV", 92],
# ["180", 98],
# ["103", 99],
# ["194", 95]]

# print (L[2][1])


# problem 2
def get_nums(L):
    res = []
    for i in range(len(L)):
        res.append(L[i][1])

    return res


# problem 3
def lookup(L, num):
    for i in range (len(L)):
        if (L[i][1] == num):
            return L[i][0]
    return None


if (__name__ == '__main__'):
    L = [["CIV", 92],
    ["180", 98],
    ["103", 99],
    ["194", 95]]

    print(lookup(L, 95))



# problem 4
def E(x0, x1, x2, w01, w02, w12):
    term1 = x0 * x1 * w01
    term2 = x0 * x2 * w02
    term3 = x1 * x2 * w12
    return -(term1 + term2 + term3)

def print_all_energies(w01, w02, w12):
    for x0 in [-1, 1]:
        for x1 in [-1, 1]:
            for x2 in [-1, 1]:
                print("x: (", x0, x1, x2, ")", "E:", E(x0, x1, x2, w01, w02, w12))


def get_memory(x0, x1, x2, w01, w02, w12):
    memory = []
    cur_min = 100000
    for x0 in [-1, 1]:
        for x1 in [-1, 1]:
            for x2 in [-1, 1]:
                if(E(x0, x1, x2, w01, w02, w12) < cur_min):
                    cur_min = E(x0, x1, x2, w01, w02, w12)
                    memory = [[x0, x1, x2]]
                elif(E(x0, x1, x2, w01, w02, w12) == cur_min):
                    memory.append([x0, x1, x2])
    return memory

if __name__ == '__main__':
    w01 = 2
    w02 = -1
    w12 = 1
    print_all_energies(w01, w02, w12)

    # (b)
    # memory =  [[-1, -1, -1], 
    #             [-1, -1, 1], 
    #             [1, 1, -1], 
    #             [1, 1, 1]]
    
    # x0 = -1
    # x1 = 1
    # x2 = 1
    

    # if (x0*x1 > 0):
    #     w01 += 0.1
    # else:
    #     w01 -= 0.1

    # if (x0*x2 > 0):
    #     w02 += 0.1
    # else:
    #     w02 -= 0.1

    # if (x1*x2 > 0):
    #     w12 += 0.1
    # else:
    #     w12 -= 0.1
    # print()
    # print_all_energies(w01, w02, w12)



    # (c)
    x0 = -1
    x1 = 1
    x2 = 1
    

    for i in range (5):
        if (x0*x1 > 0):
            w01 += 0.1
        else:
            w01 -= 0.1

        if (x0*x2 > 0):
            w02 += 0.1
        else:
            w02 -= 0.1

        if (x1*x2 > 0):
            w12 += 0.1
        else:
            w12 -= 0.1
        print("===========")
        print_all_energies(w01, w02, w12)
    
    print ("MEMORY: ")
    print (get_memory(x0, x1, x2, w01, w02, w12))

# (a) because since the total energy is NEGATIVE 1 times the sum of the energies between the nodes, the more positive the energies 
# between the nodes are, the smaller the sum will become after multiplying -1. Increasing a positive number will decrease the sum
