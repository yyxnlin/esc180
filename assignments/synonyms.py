
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

    res = numerator/(magnitude_vec1*magnitude_vec2)

    return res


def build_semantic_descriptors(sentences):
    print (sentences)
    dict = {}

    for sentence in sentences:
        for cur_word in sentence:
            # word is not already in dictionary -> add it to dictionary
            if (cur_word not in dict.keys()):
                dict[cur_word] = {}

            # dict[word] is current semantic descriptor of the word
            for search_word in sentence: # loop through sentence again
                if search_word != cur_word: # different word than current word
                    if search_word in dict[cur_word]: # word 2 already in semantic descriptor of word
                        dict[cur_word][search_word] += 1
                    else:
                        dict[cur_word][search_word] = 1
    
    return dict

def build_semantic_descriptors_from_files(filenames):
    res = []
    sentences = []

    for filename in filenames:
        file = open(filename, "r", encoding="latin1").read().lower().replace("\n", " ")
        start_ind = 0
        for i in range (len(file)):
            if file[i] == "." or file[i] == "?" or file[i] == "!":
                sentences.append(file[start_ind:i])
                start_ind = i+1
                i += 1

        # sentences.extend(re.split("[.?!]+", file))

    i = 0
    for sentence in sentences:
        # print(sentence)
        # sentence = sentence.lower()  # lowercase
        # if 0 < i < 20:
        # print(sentence + "\n\n\n")
        # i+=1

        start_ind = 0
        words = []

        for i in range(len(sentence)):
            if (sentence[i] == " " or sentence[i] == "\'" or sentence[i] == "," or sentence[i] == ";" or sentence[i] == " "):
                if (i - start_ind > 1):
                    word = sentence[start_ind:i]

                    exists = False

                    for e in words:
                        if word == e:
                            exists = True
                    if not exists:
                        words.append(word)
                start_ind = i+1
                i += 1

        if (len(words) > 0):
            res.append(words)
    
    # print(res)
    return build_semantic_descriptors(res)



def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    max = -1
    res = choices[0]


    for choice in choices:
        if (word not in semantic_descriptors.keys()):
            return "not"
        if (choice not in semantic_descriptors.keys()):
            continue
        sim = similarity_fn(semantic_descriptors[word], semantic_descriptors[choice])
        print (word, choice, sim)
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

        print(word + ", " + ans + ", " + res)

        # if (ans != res):
        #     print(semantic_descriptors[word])

        if (res == ans):
            num_correct += 1
        num_tests += 1

    return (num_correct/num_tests)

list = [["i", "am", "a", "sick", "man"],
["i", "am", "a", "spiteful", "man"],
["i", "am", "an", "unattractive", "man"],
["i", "believe", "my", "liver", "is", "diseased"],
["however", "i", "know", "nothing", "at", "all", "about", "my",
"disease", "and", "do", "not", "know", "for", "certain", "what", "ails", "me"]]


list2 = [["i", "am", "a", "sick", "man"],
["i", "am", "a", "spiteful", "man"],
["i", "am", "an", "unattractive", "man"]]

# print(cosine_similarity({"a": 1, "b": 2, "c": 3}, {"b": 4, "c": 5, "d": 6}))
# print(build_semantic_descriptors(list2))
# descriptors = build_semantic_descriptors_from_files(["warandpeace.txt", "swannsway.txt"])
# descriptors = build_semantic_descriptors_from_files(["moderately-sized-file.txt"])
descriptors = build_semantic_descriptors_from_files(["test2.txt"])
# print(descriptors.keys())
print (descriptors["one"])

# print(cosine_similarity(descriptors["watch"], descriptors["hear"]))
# print(cosine_similarity(descriptors["watch"], descriptors["see"]))

# print(most_similar_word("onsse", ["two", "see"], descriptors, cosine_similarity))
# res = run_similarity_test("test.txt", descriptors, cosine_similarity)
# print(res, "of the guesses were correct")