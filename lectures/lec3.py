import math


def quad_r1(a, b, c):
    return (math.sqrt(b**2-4*a*c)-b)/(2*a)
    
if __name__ == '__main__':
    print (quad_r1(1, 2, 1))
