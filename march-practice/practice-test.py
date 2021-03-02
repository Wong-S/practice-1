# You are given two arrays of integers a and b of the same length, and an integer k. We will be iterating through array a from left to right, and simultaneously through array b from right to left, and looking at pairs (x, y), where x is from a and y is from b. Such a pair is called tiny if the concatenation xy is strictly less than k.

# Your task is to return the number of tiny pairs that you'll encounter during the simultaneous iteration through a and b.

# possibly use zip() and reverse() the second list
# Example

# For a = [1, 2, 3], b = [1, 2, 3], and k = 31, the output should be
# countTinyPairs(a, b, k) = 2.

# We're considering the following pairs during iteration:

# (1, 3). Their concatenation equals 13, which is less than 31, so the pair is tiny;
# (2, 2). Their concatenation equals 22, which is less than 31, so the pair is tiny;
# (3, 1). Their concatenation equals 31, which is not less than 31, so the pair is not tiny.
# As you can see, there are 2 tiny pairs during the iteration, so the answer is 2.

# For a = [16, 1, 4, 2, 14], b = [7, 11, 2, 0, 15], and k = 743, the output should be
# countTinyPairs(a, b, k) = 4.

# We're considering the following pairs during iteration:

# (16, 15). Their concatenation equals 1615, which is greater than 743, so the pair is not tiny;
# (1, 0). Their concatenation equals 10, which is less than 743, so the pair is tiny;
# (4, 2). Their concatenation equals 42, which is less than 743, so the pair is tiny.
# (2, 11). Their concatenation equals 211, which is less than 743, so the pair is tiny;
# (14, 7). Their concatenation equals 147, which is less than 743, so the pair is tiny.
# There are 4 tiny pairs during the iteration, so the answer is 4.

# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] array.integer a

# An array of non-negative integers.

# Guaranteed constraints:
# 0 ≤ a.length ≤ 105,
# 0 ≤ a[i] ≤ 104.

# [input] array.integer b

# An array of non-negative integers.

# Guaranteed constraints:
# b.length = a.length,
# 0 ≤ b[i] ≤ 104.

# [input] integer k

# An integer to compare concatenated pairs with.

# Guaranteed constraints:
# 0 ≤ k ≤ 109.

# [output] integer

# The number of tiny pairs during the iteration.


def countTinyPairs(a, b, k):
    # reverese the second list
    b.reverse()
    # set concatenated elements to empty list
    concat_elements = []
    # keep track of tiny pairs
    count_of_pairs = 0

    # iterate through zipped lists of a and b
    for ele, num in zip(a, b):
        # change each element from int into str
        string_ele = str(ele)
        num_string = str(num)
        # add to the list
        concat_elements.append(string_ele + num_string)
    # iterate through the pairs in the concatenated list
    for pair in concat_elements:
        # change pair into int
        # set conditional if the pair is less than k
        if int(pair) < k:
            count_of_pairs += 1

    # return the count
    return count_of_pairs


# print(countTinyPairs([1, 2, 3],[1, 2, 3],31))
# print(countTinyPairs([16, 1, 4, 2, 14],[7, 11, 2, 0, 15],743))

# ======================================================#

# You are given an array of arrays a. Your task is to group the arrays a[i] by their mean values, so that arrays with equal mean values are in the same group, and arrays with different mean values are in different groups.

# Each group should contain a set of indices (i, j, etc), such that the corresponding arrays (a[i], a[j], etc) all have the same mean. Return the set of groups as an array of arrays, where the indices within each group are sorted in ascending order, and the groups are sorted in ascending order of their minimum element.

# Example

# For

# a = [[3, 3, 4, 2],
#      [4, 4],
#      [4, 0, 3, 3],
#      [2, 3],
#      [3, 3, 3]]
# the output should be

# meanGroups(a) = [[0, 4],
#                  [1],
#                  [2, 3]]
# mean(a[0]) = (3 + 3 + 4 + 2) / 4 = 3;
# mean(a[1]) = (4 + 4) / 2 = 4;
# mean(a[2]) = (4 + 0 + 3 + 3) / 4 = 2.5;
# mean(a[3]) = (2 + 3) / 2 = 2.5;
# mean(a[4]) = (3 + 3 + 3) / 3 = 3.
# There are three groups of means: those with mean 2.5, 3, and 4. And they form the following groups:

# Arrays with indices 0 and 4 form a group with mean 3;
# Array with index 1 forms a group with mean 4;
# Arrays with indices 2 and 3 form a group with mean 2.5.
# Note that neither

# meanGroups(a) = [[0, 4],
#                  [2, 3],
#                  [1]]
# nor

# meanGroups(a) = [[0, 4],
#                  [1],
#                  [3, 2]]
# will be considered as a correct answer:

# In the first case, the minimal element in the array at index 2 is 1, and it is less then the minimal element in the array at index 1, which is 2.
# In the second case, the array at index 2 is not sorted in ascending order.
# For

# a = [[-5, 2, 3],
#      [0, 0],
#      [0],
#      [-100, 100]]
# the output should be

# meanGroups(a) = [[0, 1, 2, 3]]
# The mean values of all of the arrays are 0, so all of them are in the same group.

# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] array.array.integer a

# An array of arrays of integers.

# Guaranteed constraints:
# 1 ≤ a.length ≤ 100,
# 1 ≤ a[i].length ≤ 100,
# -100 ≤ a[i][j] ≤ 100.

# [output] array.array.integer

# An array of arrays, representing the groups of indices.

# ======================================================#

# You're developing a new programming language with some unusual features for strings! Among these is a method that returns the longest palindrome that can be formed with the characters of a given string.


# Given a string s, your task is to find this longest possible palindrome. You may use any number of the characters from s, and arrange them in any order (so long as it results in a palindrome).

# If there are multiple longest palindromes that can be formed, return the one among them that's lexicographically smallest.

# Example

# For s = "aaabb", the output should be maximalPalindrome(s) = "ababa".

# There are two possible palindromes of length 5 that can be obtained ("ababa" and "baaab"), but "ababa" is lexicographically smaller, thus it is the answer.

# For s = "aaabbbcc", the output should be maximalPalindrome(s) = "abcacba".

# It's not possible to form a palindrome of length 8, but from several palindromes of length 7, "abcacba" is the lexicographically smallest, thus it is the answer.

# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] string s

# The given string.

# Guaranteed constraints:
# 1 ≤ s.length ≤ 105.

# [output] string

# The lexicographically smallest palindrome with maximal length that can be built from the given string s.

# ======================================================#

# You are given an array of integers a and two integers l and r. You task is to calculate a boolean array b, where b[i] = true if there exists an integer x, such that a[i] = (i + 1) * x and l ≤ x ≤ r. Otherwise, b[i] should be set to false.

# Example

# For a = [8, 5, 6, 16, 5], l = 1, and r = 3, the output should be boundedRatio(a, l, r) = [false, false, true, false, true].

# For a[0] = 8, we need to find a value of x such that 1 * x = 8, but the only value that would work is x = 8 which doesn't satisfy the boundaries 1 ≤ x ≤ 3, so b[0] = false.
# For a[1] = 5, we need to find a value of x such that 2 * x = 5, but there is no integer value that would satisfy this equation, so b[1] = false.  (NOTE: because it's a float, not integer)
# For a[2] = 6, we can choose x = 2 because 3 * 2 = 6 and 1 ≤ 2 ≤ 3, so b[2] = true.
# For a[3] = 16, there is no an integer 1 ≤ x ≤ 3, such that 4 * x = 16, so b[3] = false.
# For a[4] = 5, we can choose x = 1 because 5 * 1 = 5 and 1 ≤ 1 ≤ 3, so b[4] = true.
# Input/Output

# Edge cases:
# In case of negative numbers, use abs() method
# Be aware of floats

# [execution time limit] 4 seconds (py3)

# [input] array.integer a

# An array of integers.

# Guaranteed constraints:
# 1 ≤ a.length ≤ 100,
# 1 ≤ a[i] ≤ 106.

# [input] integer l

# An integer representing the lower bound for x.

# Guaranteed constraints:
# 1 ≤ l ≤ 104.

# [input] integer r

# An integer representing the upper bound for x.

# Guaranteed constraints:
# 1 ≤ r ≤ 104,
# l ≤ r.

# [output] array.boolean

# A boolean array.


def get_boolean(arr, l, r):

    for i in range(len(arr)):
        item = arr[i]
        if i != 0:
            result = item / i
            print(result >= l and result <= r)
        else:
            print(False)


print(get_boolean([8, 5, 6, 16, 5], 1, 3))

