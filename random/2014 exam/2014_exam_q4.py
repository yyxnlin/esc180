def f(n):
    n = 5
m = 2
f(m)
print(m)

L = [[1, 2], 3]
M = L[:]
M[0][1] = 5
M[1] = 5
print(L)


def f(d):
    d1 = {}
    for k in d:
        d1[k] = d[k]
    return d1
d = {1:[[1, 2]], 0:[[3, 4]]}
d1 = f(d)
d1[0][0][0] = 5
print(d[0])


s = "HO HO HO"
su = s
s = "Merry Christmas!"
print(su)
