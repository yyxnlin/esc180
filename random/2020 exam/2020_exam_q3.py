#   Problem 3 (10 pts)
#
#    Without using for-loops or while-loops, write  function for which
#    the tight asymptotic bound on the runtime complexity is O((n^2)*log(n)).
#    You may create helper functions, as long as they also do not use while-
#    and for-loops.
#    Justify your answer in a comment. The signature of the function must be

def f(n):
    return h(h(g(n)))


def g(n):
    if n == 0:
        return 0
    return g(abs(n)//2)


def h(n):
    if n == 0:
        return 0
    return h(abs(n)-1)

