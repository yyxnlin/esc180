#    Problem 1 (25 pts)
#
#    Up to 5 points will be awarded for making progress toward a correct
#    solution.
#
#    Assume you are given a list of filenames of text files. Assume
#    that the text files only contain the punctuation
#    [".", ",", "!", "?", "-"].
#    The files may also contain the newline character "\n".
#
#    For each file, there is a word that occurs in that file the most often --
#    the most frequent word. We want to find the word that is the most frequent
#    word in the most files.
#    Write a function that takes in a list of file names, and returns the word
#    that is the most frequent word in the most files. You can assume that there
#    are no ties: each file has one word that is the most frequent, and there
#    is one word that is the most frequent word in the most files.
#    For example, the function might be called as follows:
#
#    most_common_frequent_word(["diseases/" + filenames[0],
#                                "diseases/" + filenames[1],
#                                "diseases/" + filenames[2])
#    If the most frequent word in filesnames[0] is "a", the most frequent word in
#    filenames[1] is "the", and the most frequent word in filenames[2] is
#    "the", most_common_frequent_word should return "the"                               .
#    A non-word, such as "<a", would be considered a valid word for the files
#    given to you.
#
#    The words "Dog" and "dog" should be considered to be the same when computing
#    the frequency of words. The words "dogs" and "dog" should be considered
#    to be different.
#
#    You are encouraged to use helper functions.
#
#    For this problem, you may *not* import any Python modules.
# 
# 
def most_common_frequent_word(files):
    punc = [".", ",", "!", "?", "-", "\\n"]
    freq_words = []

    for file in files:
        raw = open(file).read().lower()

        for p in punc:
            raw.replace(p, " ")

        words = raw.split()
        dict = put_into_dict(words)
        freq_words.append(most_frequent_word(dict))

    master_dict = put_into_dict(freq_words)
    return most_frequent_word(master_dict)


def put_into_dict(words):
    dict = {}

    for word in words:
        if word in dict.keys():
            dict[word] += 1
        else:
            dict[word] = 1
    return dict

def most_frequent_word(dict):
    max_word = ""
    max_value = 0

    for word, freq in dict.items():
        if freq > max_value:
            max_value = freq
            max_word = word
    return max_word

print(most_common_frequent_word(["random/2020 exam/file1.txt", "random/2020 exam/file2.txt", "random/2020 exam/file3.txt"]))