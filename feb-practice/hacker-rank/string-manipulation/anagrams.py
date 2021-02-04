# Q1:
# Given two strings, 'a' and 'b', that may or may not be of the same length, determine the minimum number of character deletions required to make  and  anagrams. Any characters can be deleted from either of the strings.

# Test cases:
# I: a = 'cde'
#     b = 'dcf'
# O: 2

# I: a = 'cde'
#  b = 'abc'

# O: 4

# Thought/Pseudo Process:
# Create a function taking in two STRINGS as parameters
# Combine strings a and b together
# Put those strings into a dictionary and count the occurences of each letter
# Set a counter for the number of times the key has a value of 1
# Iterate through the dictionary
# if the value is equal to 1
# increment the counter

# return the counter

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    combine_words = a + b

    dict_words = {}
    for char in combine_words:
        dict_words[char] = dict_words.get(char, 0) + 1

    print(dict_words)
    count_deletions = 0
    for key, value in dict_words.items():
        if value == 1:
            count_deletions += 1

    return count_deletions


print(
    makeAnagram("fcrxzwscanmligyxyvym", "jxwtrhvujlmrpdoqbisbwhmgpmeoke")
)  # Won't pass this test case: Must be 30
print(makeAnagram("cde", "dcf"))  # Pass test case

# ======================
# Alt method:

from collections import Counter
import sys


def makeAnagram(a, b):

    res = 0

    str_1 = a.strip()
    print(str_1)

    str_2 = b.strip()
    print(str_2)

    cnt1 = Counter(str_1)
    print(
        cnt1
    )  # Counter({'y': 3, 'c': 2, 'x': 2, 'm': 2, 'f': 1, 'r': 1, 'z': 1, 'w': 1, 's': 1, 'a': 1, 'n': 1, 'l': 1, 'i': 1, 'g': 1, 'v': 1})
    # Sorts it in decsending order
    cnt2 = Counter(str_2)
    print(
        cnt2
    )  # Counter({'m': 3, 'j': 2, 'w': 2, 'r': 2, 'h': 2, 'p': 2, 'o': 2, 'b': 2, 'e': 2, 'x': 1, 't': 1, 'v': 1, 'u': 1, 'l': 1, 'd': 1, 'q': 1, 'i': 1, 's': 1, 'g': 1, 'k': 1})

    cnt3 = {}

    for (
        key,
        val,
    ) in (
        cnt1.items()
    ):  # Iterating over the dictionary; starts from key at 'f' and it's value, subtracts it from the same key 'f' (if present) in the second dictionary
        cnt3[key] = abs(val - cnt2[key])  # Returns absolute positive value in new dict

    # WE iterate again because checking the second dict for any differences
    for key, val in cnt2.items():
        cnt3[key] = abs(val - cnt1[key])

    for val in cnt3.values():
        res += val

    return res


print(makeAnagram("fcrxzwscanmligyxyvym", "jxwtrhvujlmrpdoqbisbwhmgpmeoke"))
print(makeAnagram("cde", "dcf"))

