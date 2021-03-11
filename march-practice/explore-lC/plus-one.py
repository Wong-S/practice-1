# Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.

# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

# You may assume the integer does not contain any leading zero, except the number 0 itself.


# Example 1:

# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Example 2:

# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Example 3:

# Input: digits = [0]
# Output: [1]

# Constraints:

# 1 <= digits.length <= 100
# 0 <= digits[i] <= 9


def plusOne(digits):

    # First approach:
    final_arr = []
    last_digit = len(digits) - 1
    for index, num in enumerate(digits):
        if index == last_digit:
            if num == 9:
                final_arr.append(1)
                final_arr.append(0)
            else:
                final_arr.append(num + 1)
        else:
            if num == 9:
                final_arr.append(1)
                final_arr.append(0)
            else:
                final_arr.append(num)

    return final_arr

    # Discussion solution:
    j = len(digits) - 1  # 2

    while j >= 0 and digits[j] == 9:
        digits[j] = 0
        j -= 1

    if j >= 0:
        digits[j] += 1
    else:
        digits = [1] + digits
    return digits


print(plusOne([1, 2, 3]))  # [1, 2, 4]
print(plusOne([4, 3, 2, 1]))  # [4, 3, 2, 2]
print(plusOne([0]))  # [1]

print(plusOne([9]))  # [1,0]
print(plusOne([9, 9]))  # [1,0,0]

