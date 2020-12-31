#Q1: Monotonic Array (896)

# An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

# Return true if and only if the given array A is monotonic.

# Test Cases:

# Input: [1,2,2,3]
# Output: true
# Example 2:

# Input: [6,5,4,4]
# Output: true
# Example 3:

# Input: [1,3,2]
# Output: false
# Example 4:

# Input: [1,2,4,5]
# Output: true
# Example 5:

# Input: [1,1,1]
# Output: true


#Thoughts:
#Has to be in order, sorted 
#Check if the list is ordered 
#Check if i <= j, then continue
#Check if i >= j, then continue

#Special cases:
#I: []
#O: false

#I: [0]
#O: false 

#Pseudocode:

#Iterate through the list
    #If i[0] <= i[0+1], continue



    #else, return false

#Iterate through the list
    #If i[0] >= i[0+1], continue

    #else, return false


#return true

#Code:

class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        

        if A[0] <= A[1]:
            for i in range(len(A) - 1):
                if A[i] <= A[i+1] 
                    
                    continue
                    
                else:
                    return False

        if A[0] >= A[1]:
            for i in range(len(A) - 1):          
                if A[i] >= A[i+1] 
                    
                    continue
         
                else:
                    return False


#======================
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        

        return (all(A[i] <= A[i+1] for i in range(len(A) - 1)) or
                all(A[i] >= A[i+1] for i in range(len(A) - 1)))


# Input: [1,3,2]
# Output: false
# Example 4:

# Input: [1,2,4,5]
# Output: true
# Example 5:

# Input: [1,1,1]
# Output: true

