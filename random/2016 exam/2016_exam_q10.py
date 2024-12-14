def max_clique(friends):
    friends_list = list(friends.keys())
    res = []
    subsets = get_subsets(friends_list)
    max_len = 0

    for sub in subsets:
        if check_clique(sub, friends):
            if len(sub) > max_len:
                res = sub[:]
                max_len = len(sub)
    
    return res


def get_subsets(L):

    if len(L) == 0:
        return [[]]
    
    sub = get_subsets(L[1:])
    res = []
    res.extend(sub)

    for s in sub:
        res.append([L[0]]+s)

    return res

def check_clique(sub, friends):
    for i in range (len(sub)):
        p1 = sub[i]

        for j in range (i+1, len(sub)):
            p2 = sub[j]

            if p2 not in friends[p1]:
                return False
    return True


friends = {"Carl Gauss": ["Isaac Newton", "Gottfried Leibniz", "Charles Babbage"],
            "Gottfried Leibniz": ["Carl Gauss"],
            "Isaac Newton": ["Carl Gauss", "Charles Babbage"],
            "Ada Lovelace": ["Charles Babbage", "Michael Faraday"],
            "Charles Babbage": ["Isaac Newton", "Carl Gauss", "Ada Lovelace"],
            "Michael Faraday": ["Ada Lovelace"] }
print(max_clique(friends))