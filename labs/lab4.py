# ESC180 Lab 4
# October 2, 2024

import math

# question 1
sum = 0

for i in range (10001):
    sum += ((-1)**i)/(2*i+1)
    print(sum*4)




# question 2
sum = 0
i = 0

while (i <= 1000):
    sum += ((-1)**i)/(2*i+1)
    i = i + 1


print(sum*4)



# question 3
#(a)
def gcd(n, m):
    value = 0

    for i in range (1, min(n, m)):
        if (n % i == 0 and m % i == 0):
            value = i
    return value

print (gcd (15, 21))

#(b)
def gcd_better(n, m):
    i = min(n, m)

    while (i > 0):
        if (n % i == 0 and m % i == 0):
            return i
        i-=1

    return 1

print (gcd_better (17, 21))


# question 4
def simpify_fraction(n, m):
    gcd = gcd_better(n, m)

    print (str(int(n/gcd)) + "/" + str(int(m/gcd)))

simpify_fraction(15, 21)


# question 5
# names = ""
# new_name = input("Enter a name: ")

# if (new_name != "END"):
#     names += new_name


# while (new_name != "END"):
#     new_name = input("Enter a name: ")

#     if (new_name != "END"):
#         names += ", " + new_name


# print ("The names are: " + names)


# question 6

# def num_terms(n):
#     target = round(math.pi*(10**(n-1)))
    
#     sum = 0
#     i = 0

#     while (round(sum*4*(10**(n-1))) != target):
#         sum += ((-1)**i)/(2*i+1)
#         # print (sum*4)
#         i+=1

#     return i

# print (num_terms(5))




