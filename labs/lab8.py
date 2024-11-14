# ESC180 Lab 8
# November 13, 2024

# problem 3
# f = open("labs/lab8data.txt")
# lines = f.readlines()

# for line in lines:
#     if (line.lower().find("lol") != -1):
#         print (line, end="")

# problem 4
def dict_to_str(d):
    """Return a str containing each key and value in dict d. Keys and
    values are separated by a comma. Key-value pairs are separated
    by a newline character from each other.
    For example, dict_to_str({1:2, 5:6}) should return "1, 2\n5, 6".
    (the order of the key-value pairs doesn’t matter and can be different
    every time).
    """

    res = ""
    count = 1

    for key, value in d.items():
        if (count != len(d)):
            res += key + ", " + value + "\n"
        else:
            res += key + ", " + value
        count += 1

    return res

# problem 5
def dict_to_str_sorted(d):
    """Return a str containing each key and value in dict d. Keys and
    values are separated by a comma. Key-value pairs are separated
    by a newline character from each other, and are sorted in
    ascending order by key.
    For example, dict_to_str_sorted({1:2, 0:3, 10:5}) should
    return "0, 3\n1, 2\n10, 5". The keys in the string must be sorted
    dict = {"hi":"bye", "meow": "cat", "quack":"duck"}
    print (dict_to_str(dict))
    in ascending order."""

    unsorted = dict_to_str(d)
    pairs = unsorted.split("\n")
    pairs.sort()
    res = ""

    for i in range(len(pairs)):
        res += pairs[i]
        if (i != len(pairs)-1):
            res += "\n"

    return res

# problem 6
# (a)
def get_word_count(words):
    dict = {}
    
    for word in words:
        if (word in dict.keys()):
            dict[word] += 1
        else:
            dict[word] = 1

    return dict

# (b)
def top10(L):
    L.sort(reverse=True)
    return (L[0:10])

dict = {"cow":"moo", "cat":"meow", "duck":"quack"}

# (c)
def invert_dict(d):
    res = {}

    for key, value in d.items():
        if (value in res.keys()):
            res[value].append(key)
        else:
            res[value] = [key]
    return res

def get_top_10(filename):
    words = open(filename, encoding="latin-1").read().split()
    inverted = invert_dict(get_word_count(words))
    sorted_freq = sorted(inverted.items())

    most_freq_words = []

    count = 0
    for i in reversed(sorted_freq):
        if count < 10:
            count += len(i[1])
            most_freq_words.extend(i[1])

    return most_freq_words

print (get_top_10("labs/lab8story.txt"))

# L = [92,14,455,304,75,295,115,201,6,354,161,225,244,129,328,274,203,184,343,370,481,493,71,436,186,232,199,112,152,247,255,243,259,226,245,350,220,323,449,257,113,83,412,90,371,176,9,136,489,216,394,250,337,463,230,97,375,273,425,318,457,468,36,179,22,159,360,338,157,173,155,353,77,39,272,166,49,479,34,128,348,372,111,193,28,321,123,192,475,260,234,322,156,424,450,364,55,163,486,474]
# print(top10(L))