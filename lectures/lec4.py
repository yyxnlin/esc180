import math
import time

def equals4(x):
    return x==4

def has_roots(a, b, c):
    disc = b**2-4*a*c
    return disc>=0

def praxify_str(s):
    return "In my opinion, " + s

if __name__=='__main__':
    print(praxify_str("Lynn is cooler than cindy"))
    print (time.time()) # number of seconds since jan 1 1970 ("epoch time")
    print (math.cos(math.pi))
