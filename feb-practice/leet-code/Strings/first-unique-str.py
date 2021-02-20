# Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.
# Note: You may assume the string contains only lowercase English letters.


# Test cases:

# s = "leetcode"
# return 0.

# s = "loveleetcode"
# return 2.

# s = ""
# return -1

# s = "lll"
# return -1

from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict_count = Counter(s)

        letter_key = ""

        for letter, value in dict_count.items():
            if value == 1:
                letter_key += letter
                break

        if letter_key == "":
            return -1

        for index, char in enumerate(s):
            if char == letter_key:
                return index

