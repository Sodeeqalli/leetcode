# 1470. Shuffle the Array
# Solved
# Easy

# Topics
# Companies

# Hint
# Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

# Return the array in the form [x1,y1,x2,y2,...,xn,yn].

 

# Example 1:

# Input: nums = [2,5,1,3,4,7], n = 3
# Output: [2,3,5,4,1,7] 
# Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].
# Example 2:

# Input: nums = [1,2,3,4,4,3,2,1], n = 4
# Output: [1,4,2,3,3,2,4,1]
# Example 3:

# Input: nums = [1,1,2,2], n = 2
# Output: [1,2,1,2]

#solution
class Solution(object):
    def shuffle(self, nums, n):
        i ,j = 0, n #initialize first pointer to zero and second to n(middle)
        shuffled = [] #create an array to store the shuffled
        while i < n: #while i < the middle number
            shuffled.append(nums[i]) #add the number at first pointer
            shuffled.append(nums[j]) #add the number at second pointer
            i+=1 #increase first pointer by one
            j+=1 #increase second pointer by one
        return shuffled #return the shuffled array