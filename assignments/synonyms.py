
# to do
# two of same word in one sentence counts twice (shouldnt do that)
# what if word and choice are both not in semantic descriptors

# return "not" if unknown word is queried?
# return first choice if none of choices are in the dict?

import math
import re


def norm(vec):
    '''Return the norm of a vector stored as a dictionary, as 
    described in the handout for Project 3.
    '''
    
    sum_of_squares = 0.0  
    for x in vec:
        sum_of_squares += vec[x] * vec[x]
    
    return math.sqrt(sum_of_squares)


def cosine_similarity(vec1, vec2):
    numerator = 0
    magnitude_vec1 = 0
    magnitude_vec2 = 0

    for word, num in vec1.items():
        if (word in vec2.keys()):
            numerator += num * vec2[word]
    
    for word, num in vec1.items():
        magnitude_vec1 += num**2
    magnitude_vec1 = math.sqrt(magnitude_vec1)

    for word, num in vec2.items():
        magnitude_vec2 += num**2
    magnitude_vec2 = math.sqrt(magnitude_vec2)

    prod = (magnitude_vec1*magnitude_vec2)

    if prod == 0:
        return -1
    res = numerator/prod

    return res

# input: must be a list of lists with distinct words
def build_semantic_descriptors(sentences):
    dict = {}

    for sentence in sentences:
        words = []
        for word in sentence:
            if word not in words:
                words.append(word)
        for cur_word in words:
            # word is not already in dictionary -> add it to dictionary
            if cur_word not in dict.keys():
                dict[cur_word] = {}

            # dict[word] is current semantic descriptor of the word
            for search_word in words: # loop through sentence again
                if search_word != cur_word: # different word than current word

                    if search_word in dict[cur_word]: # word 2 already in semantic descriptor of word
                        dict[cur_word][search_word] += 1
                    else:
                        dict[cur_word][search_word] = 1
    
    return dict

def build_semantic_descriptors_from_files(filenames):
    res = []
    sentences = []
    remove_str = " ,./;:-=_+"
    remove_chars=[]

    for ch in remove_str:
        remove_chars.append(ch)


    for filename in filenames:
        file = open(filename, "r", encoding="latin1").read().lower().replace("\n", " ")
        start_ind = 0
        for i in range (len(file)):
            if file[i] == "." or file[i] == "?" or file[i] == "!":
                sentences.append(file[start_ind:i])
                start_ind = i+1
                i += 1

    i = 0
    for sentence in sentences:
        start_ind = 0
        words = []

        for i in range(len(sentence)):
            a = sentence[i]

            # at last character of sentence 
            if i == len(sentence) - 1:
                ending = len(sentence)
                # if last character is invalid character
                if sentence[i] in remove_chars:
                    ending = len(sentence) - 1

                word = sentence[start_ind:ending]
                words.append(word)

            # not at last character and invalid character at current position
            elif sentence[i] in remove_chars:
                if i - start_ind > 1: # not an empty string in between
                    word = sentence[start_ind:i]
                    words.append(word)
                start_ind = i+1
                i += 1

        if (len(words) > 0):
            res.append(words)

    return build_semantic_descriptors(res)


def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    max = -1
    res = choices[0]


    for choice in choices:
        if (word not in semantic_descriptors.keys()):
            break
        if (choice not in semantic_descriptors.keys()):
            continue
        sim = similarity_fn(semantic_descriptors[word], semantic_descriptors[choice])

        if (sim > max):
            res = choice
            max = sim
    
    return res



def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    tests = open(filename, "r", encoding="latin1").read().split("\n")
    num_tests = 0
    num_correct = 0

    for test in tests:
        words = test.split(" ")
        word = words[0]
        ans = words[1]
        choices = words[2:]
        res = most_similar_word(word, choices, semantic_descriptors, similarity_fn)

        if (res == ans):
            num_correct += 1
        num_tests += 1

    return (num_correct/num_tests)


# print(cosine_similarity({"a": 1, "b": 2, "c": 3}, {"b": 4, "c": 5, "d": 6}))
# print(build_semantic_descriptors(list2))
descriptors = build_semantic_descriptors_from_files(["warandpeace.txt", "swannsway.txt"])
# slist = [['this', 'is', 'file', 'one'],
#                     ['this', 'is', 'file', 'two'],
#                     ['file', 'two', 'has', 'two', 'sentences'],
#                     ['this', 'is', 'file', 'three'],
#                     ['file', 'three', 'has', 'three', 'sentences'],
#                     ['this', 'is', 'the', 'third', 'sentence']]
# descriptors = build_semantic_descriptors(slist)
# print(descriptors["file"])
# for s in descriptors.items():
#     print(s)

res = run_similarity_test("test.txt", descriptors, cosine_similarity)
print(res, "of the guesses were correct")