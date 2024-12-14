def get_all_subsets(list):
    if len(list) == 0:
        return [[]]
    
    t = get_all_subsets(list[1:])
    res = []
    res.extend(t)

    for t1 in t:
        res.append([list[0]] + t1)
    return res

def get_all_permutations(list):
    if len(list) == 1:
        return [list]
    res = []

    for i in range (len(list)):
        other_perms = get_all_permutations(list[:i] + list[i+1:])
        for perm in other_perms:
            res.append([list[i]] + perm)

    return res
    
def check_chain(list, friends):
    for i in range (1, len(list)):
        if list[i] not in friends[list[i-1]]:
            return False
    return True

def get_longest_chain(friends):
    max_len = 0

    subs = get_all_subsets(list(friends.keys()))
    perms = []

    for subset in subs:
        perms.extend(get_all_permutations(subset))


    for perm in perms:
        if check_chain(perm, friends):
            if len(perm) > max_len:
                max_len = len(perm)

    return max_len


friends = {"Carl Gauss": ["Isaac Newton", "Gottfried Leibniz", "Charles Babbage"],
           "Gottfried Leibniz": ["Carl Gauss"],
           "Isaac Newton": ["Carl Gauss", "Charles Babbage"],
           "Ada Lovelace": ["Michael Faraday"],
           "Charles Babbage": ["Isaac Newton", "Carl Gauss"],
           "Michael Faraday": ["Ada Lovelace"]    }

print(get_longest_chain(friends))