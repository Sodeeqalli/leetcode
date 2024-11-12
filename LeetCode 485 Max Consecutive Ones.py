# 485. Max Consecutive Ones
# Solved
# Easy

# Topics
# Companies

# Hint
# Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

# Example 1:

# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
# Example 2:

# Input: nums = [1,0,1,1,0,1]
# Output: 2
 

# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.


#solution
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        maximum = 0 #variable to keep track of the longest sequence
        current = 0 #variable to keep track of the current sequence
        for i in range(len(nums)): #for every number
            if nums[i] == 1: #if it is one
                current +=1 #add to current sequence
            else: #if it is not one
                if current > maximum: #check if the current sequence is longer than the current longest squence
                    maximum, current = current, 0 #if it is, the max sequence becomes the current and current is reinitialised to zero
                else: #if the current sequence is not longer than the current longest sequence
                    current = 0 #the current sequence is just restarted
        return current if current > maximum else maximum #we return the current if its longer than the maximum, else we return maximum
    
    
#test
if __name__ == "__main__":
    solution = Solution()
    print(solution.findMaxConsecutiveOnes([1,1,0,1,1,1]))