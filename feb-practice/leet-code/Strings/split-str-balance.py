# Question (1221) Split a String in Balanced Strings


# Balanced strings are those that have an equal quantity of 'L' and 'R' characters.
# Given a balanced string s, split it in the maximum amount of balanced strings.
# Return the maximum amount of split balanced strings.


# Example 1:

# Input: s = "RLRRLLRLRL"
# Output: 4
# Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
# Example 2:

# Input: s = "RLLLLRRRLR"
# Output: 3
# Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.
# Example 3:

# Input: s = "LLLLRRRR"
# Output: 1
# Explanation: s can be split into "LLLLRRRR".
# Example 4:

# Input: s = "RLRRRLLRLL"
# Output: 2
# Explanation: s can be split into "RL", "RRRLLRLL", since each substring contains an equal number of 'L' and 'R'


# Thought/Pseudo:

# Iterate through the string
# Create a list of tracked pairs.
# Keep track of R's and L's
# Check if you start with R or L, check if the next letter is R or L.
# If you start with R, and the next letter is L, then you have a pair.
# If you start with R, and next letter is R, then keep track of how many R's you have.
# If the next letter is L, then the previous R's have to match the number of L's to be a match. If it changes to R and there is no equal match, then do not count that pair


# Return the sum of teh tracked pairs

# Code:


def balance_R_and_L(str_R_L):
    tracked_pairs = []

    R, L = 0, 0

    # Edge case:
    if str_R_L == "":
        return 0

    for index, letter in enumerate(str_R_L):

        if letter == "R":
            R += 1
            if R == L:
                tracked_pairs.append(1)
                R, L = 0, 0

        if letter == "L":
            L += 1
            if R == L:
                tracked_pairs.append(1)
                R, L = 0, 0

    return sum(tracked_pairs)

    # Below is a unfinshed detailed DRY alternative way that wasn't quite there...

    # if letter == "R":
    #     R += 1
    #     if str_R_L[index + 1] == "L":
    #         L += 1
    #         if (R == L): #if next letter is "L"       #Might throw out of index error....
    #             tracked_pairs.append(1)
    #             R,L = 0 , 0
    #     elif letter == "R":
    #         R += 1
    #         if R == L:
    #             tracked_pairs.append(1)
    #             R,L = 0,0
    # elif letter == "L":
    #     L += 1
    #     if str_R_L[index + 1] == "R":
    #         R += 1
    #         if (R == L):
    #             tracked_pairs.append(1)
    #             R,L = 0,0

    #     elif letter == "L":
    #         L += 1
    #         if R == L:
    #             tracked_pairs.append(1)
    #             R,L = 0,0

    # return sum(tracked_pairs)


print(balance_R_and_L("RLRRLLRLRL"))

print(balance_R_and_L("RLLLLRRRLR"))

print(balance_R_and_L("LLLLRRRR"))

print(balance_R_and_L("RLRRRLLRLL"))

print(balance_R_and_L(""))

# Runtime: 40 ms, faster than 16.04% of Python3 online submissions for Split a String in Balanced Strings.
# Memory Usage: 14.2 MB, less than 44.86% of Python3 online submissions for Split a String in Balanced Strings.


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        n = 0
        for i in s:
            if i == "R":
                count += 1
            elif i == "L":
                count -= 1
            if count == 0:
                n += 1
        return n


# Runtime: 36 ms, faster than 21.42% of Python3 online submissions for Split a String in Balanced Strings.
# Memory Usage: 14.2 MB, less than 44.86% of Python3 online submissions for Split a String in Balanced Strings.
