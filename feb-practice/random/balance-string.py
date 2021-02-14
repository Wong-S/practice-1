# Potential Prompt:

# Given  a list of strings, determine if it's balanced or not and return the length of the shortest balanced fragment
# Ex: "AcBZzaCb" would be balanced


# Input: ["AcBZzaCb", "zTZtsS", "yopYwO"]
# Output: 6

# Input: []
# Output: 0

# Input: ["AcBZzaCb"]
# Output: 8

# Input: ["Abc"]
# Output: 0

# Thought/Process:
# need to keep into account Upper and Lower case
# create a pair list
# Iterate over list of strings and each char
# Keep track of the pair and increment it each time. Don't forget to multiply by two
# Need to check if pair count is the same as the word count
# After this add this trackign number to a pair list

# Check the max number in that list and return the lowest number

# Code:
def balance_string(str_lst):
    pair_lst = []

    # Edge cases:
    if str_lst == []:  # Check if list is empty
        return 0

    for word in str_lst:
        check_pair = 0
        for char in word:
            if (char.upper() and char.lower()) in word:  # Checks if we have pair
                check_pair += 1
        if check_pair == len(
            word
        ):  # checks if the total pairs seen is the same len as the word itself and must be balanced
            pair_lst.append(check_pair)  # Pairs are multiples of two

    if pair_lst == []:
        return 0
    else:
        return min(pair_lst)  # Return the lowest number


print(balance_string(["AcBZzaCb", "zTZtsS", "yopYwO"]))  # 6

print(balance_string([]))  # 0

print(balance_string(["AcBZzaCb"]))  # 8

print(balance_string(["Abc"]))  # 0

