def string_times(str, n):
    """
    https://codingbat.com/prob/p193507
    
    Given a string and a non-negative int n, return a larger string that is n copies of the original string.

    string_times('Hi', 2) â†’ 'HiHi'
    string_times('Hi', 3) â†’ 'HiHiHi'
    string_times('Hi', 1) â†’ 'Hi'
    """

    return (str * n)

def front_times(str, n):
    """
    https://codingbat.com/prob/p165097

    Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;

    front_times('Chocolate', 2) â†’ 'ChoCho'
    front_times('Chocolate', 3) â†’ 'ChoChoCho'
    front_times('Abc', 3) â†’ 'AbcAbcAbc'
    """
    chopped = ""
    if (len(str) <= 3):
        chopped = str
    else:
        chopped = str[0:3]
    return (chopped * n)


def array_count9(nums):
    """
    https://codingbat.com/prob/p166170

    Given an array of ints, return the number of 9's in the array.

    array_count9([1, 2, 9]) â†’ 1
    array_count9([1, 9, 9]) â†’ 2
    array_count9([1, 9, 9, 3, 9]) â†’ 3
    """

    count = 0
    for i in range (len(nums)):
        if (nums[i] == 9):
            count += 1

    return count

def array_front9(nums):
    """
    https://codingbat.com/prob/p110166

    Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.

    array_front9([1, 2, 9, 3, 4]) â†’ True
    array_front9([1, 2, 3, 4, 9]) â†’ False
    array_front9([1, 2, 3, 4, 5]) â†’ False
    """


    if (len(nums) <= 4):
        for i in range (len(nums)):
            if (nums[i] == 9):
                return True
        return False
    
    else:
        for i in range (4):
            if (nums[i] == 9):
                return True
        return False
    
def array123(nums):
    """
    https://codingbat.com/prob/p193604
    
    Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.

    array123([1, 1, 2, 3, 1]) â†’ True
    array123([1, 1, 2, 4, 1]) â†’ False
    array123([1, 1, 2, 1, 2, 3]) â†’ True
    """

    if (len(nums) < 3):
        return False
    
    else:
        for i in range (len(nums) - 2):
            if (nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3):
                return True
        return False

def string_match(a, b):
    """
    https://codingbat.com/prob/p182414
    
    Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.

    string_match('xxcaazz', 'xxbaaz') â†’ 3
    string_match('abc', 'abc') â†’ 2
    string_match('abc', 'axc') â†’ 0
    """
    
    count = 0

    for i in range (min(len(a), len(b)) - 1):
        if (a[i] == b[i] and a[i+1] == b[i+1]):
            count += 1
    return count

def first_half(str):
    """
    https://codingbat.com/prob/p107010

    Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".

    first_half('WooHoo') â†’ 'Woo'
    first_half('HelloThere') â†’ 'Hello'
    first_half('abcdef') â†’ 'abc'
    """
    return (str[0:(int)(len(str)/2)])

def without_end(str):
    """
    https://codingbat.com/prob/p138533
    
    Given a string, return a version without the first and last char, so "Hello" yields "ell". The string length will be at least 2.

    without_end('Hello') â†’ 'ell'
    without_end('java') â†’ 'av'
    without_end('coding') â†’ 'odin'
    """

    return(str[1:len(str)-1])

def combo_string(a, b):
    """
    https://codingbat.com/prob/p194053

    Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside and the longer string on the inside. The strings will not be the same length, but they may be empty (length 0).

    combo_string('Hello', 'hi') â†’ 'hiHellohi'
    combo_string('hi', 'Hello') â†’ 'hiHellohi'
    combo_string('aaa', 'b') â†’ 'baaab'
    """

    short = ""
    long = ""
    if (len(a) < len(b)):
        short = a
        long = b
    else:
        short = b
        long = a

    return (short + long + short)

def left2(str):
    """
    https://codingbat.com/prob/p160545
    
    Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. The string length will be at least 2.

    left2('Hello') â†’ 'lloHe'
    left2('java') â†’ 'vaja'
    left2('Hi') â†’ 'Hi'
    """

    return (str[2:] + str[:2])

def near_ten(num):
    """
    https://codingbat.com/prob/p165321

    Given a non-negative number "num", return True if num is within 2 of a multiple of 10. Note: (a % b) is the remainder of dividing a by b, so (7 % 5) is 2. See also: Introduction to Mod

    near_ten(12) â†’ True
    near_ten(17) â†’ False
    near_ten(19) â†’ True
    """
    if (num % 10 <= 2 or num % 10 >= 8):
        return True
    return False

def count_code(str):
    """
    https://codingbat.com/prob/p186048

    Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.

    count_code('aaacodebbb') â†’ 1
    count_code('codexxcode') â†’ 2
    count_code('cozexxcope') â†’ 2
    """
    
    count = 0

    if (len(str) < 4):
        return 0
    
    else:
        for i in range (len(str) - 3):
            if (str[i:i+2] == "co" and str[i+3] == "e"):
                count += 1
        return count


def end_other(a, b):
    """
    https://codingbat.com/prob/p174314

    Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string.

    end_other('Hiabc', 'abc') â†’ True
    end_other('AbC', 'HiaBc') â†’ True
    end_other('abc', 'abXabc') â†’ True
    """

    a = a.lower()
    b = b.lower()

    longer = ""
    shorter = ""

    if (len(a) > len(b)):
        longer = a
        shorter = b
    else:
        longer = b
        shorter = a

    if (longer[(len(longer)-len(shorter)):] == shorter):
        return True
    return False

def centered_average(nums):
    """
    https://codingbat.com/prob/p126968

    Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value. Use int division to produce the final average. You may assume that the array is length 3 or more.

    centered_average([1, 2, 3, 4, 100]) â†’ 3
    centered_average([1, 1, 5, 5, 10, 8, 7]) â†’ 5
    centered_average([-10, -4, -2, -4, -2, 0]) â†’ -3
    """

    smallest = nums[0]
    largest = nums[0]
    sum = 0

    for i in range (len(nums)):
        sum += nums[i]
        smallest = min(smallest, nums[i])
        largest = max(largest, nums[i])

    sum -= smallest
    sum -= largest

    return (sum//(len(nums) - 2))
    

"""
https://www.cs.toronto.edu/~guerzhoy/180/midterm/mt2022/paper.pdf#page=7

Write a function that, when called, returns the next digit of Ï€ (approx 3.14159...). You may assume that
the function will not be called more than 10 times.

The function would be used like this:

print(next_digit_pi()) # 3
print(next_digit_pi()) # 1
print(next_digit_pi()) # 4
print(next_digit_pi()) # 1

You may import math and use math.pi
"""


import math

# Define any additional global variables here
cur_digit = 0

def next_digit_pi():
    global cur_digit
    cur_digit += 1

    return((int)(math.pi * 10**(cur_digit-1)) % 10)

# print (array123([7, 4, 1, 2, 4, 1, 2, 3, 4, 6]))
# print(string_match('xxcaazz', 'xxbaaz'))
# print(string_match('abc', 'abc'))
# print(string_match('abc', 'axc'))
# print(first_half("WooHoo"))
# print(without_end("WooHoo"))
# print(combo_string("Hiiiiiii", "Hello"))
# print(left2("Hello"))
# print(near_ten(12))
# print(near_ten(13))
# print(count_code('cozexxcope'))
# print(end_other('Hiabc', 'abc'))
# print(end_other('AbC', 'HiaBc'))
# print(end_other('abc', 'abXabc'))
# print(end_other('abcf', 'abXabc'))

# print(centered_average([1, 2, 3, 4, 100]))
# print(centered_average([1, 1, 5, 5, 10, 8, 7]))
# print(centered_average([-10, -4, -2, -4, -2, 0]))
# print(next_digit_pi()) # 3
# print(next_digit_pi()) # 1
# print(next_digit_pi()) # 4
# print(next_digit_pi()) # 1
# print(next_digit_pi()) # 5
# print(next_digit_pi()) # 9