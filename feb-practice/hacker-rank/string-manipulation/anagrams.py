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
# Alt method.
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


print(makeAnagram("fcrxzwscanmligyxyvym", "jxwtrhvujlmrpdoqbisbwhmgpmeoke"))
print(makeAnagram("cde", "dcf"))

