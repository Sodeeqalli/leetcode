# 41. First Missing Positive
# Solved
# Hard

# Topics
# Companies

# Hint
# Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

# You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

# Example 1:

# Input: nums = [1,2,0]
# Output: 3
# Explanation: The numbers in the range [1,2] are all in the array.
# Example 2:

# Input: nums = [3,4,-1,1]
# Output: 2
# Explanation: 1 is in the array but 2 is missing.
# Example 3:

# Input: nums = [7,8,9,11,12]
# Output: 1
# Explanation: The smallest positive integer 1 is missing.
 

# Constraints:

# 1 <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1

#Thought Process, we'll [3, 4, -1, 1] to think
#The first thing to do is to replace the ones not in range with any figure we are not using. so we find the highest possible number and the negative ones.
#using our example array: -1 is negative and the highest possible number is 4 cause there are 4 spaces. so we'll use 5 as our placeholder number 
# - to replace negative numbers and numbers bigger that 4
# now our array is [3, 4, 5, 1]
# now for every number here, we'll mark their position when we come accross them by negating the numbers in their supposed position
# for this step its important to check if the value has been negated before, or else double negation is positive
#and absolute values should be used to perform the marking
# so now we'll have [-3, 4, -5, -1]
#4 wont be negated because its where 2 is supposed and there's no 2 in the array
# so we'll return 2 which is the index of the only number not negated + 1

#now lets put into practice
class Solution(object):
    def firstMissingPositive(self, nums):
        n = len(nums) #not a fore-thought, you will find out we will use it a lot 
        
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1
            
        for i in range(n):
            num = abs(nums[i])
            
            if num <= n:
                if nums[num -1] > 0:
                    nums[num -1 ] = -(nums[num -1])
                    
        
        for i in range(n):
            if nums[i] > 0:
                return i + 1
            
        return n + 1
    
    #test
if __name__ =="__main__":
    solution = Solution()
    
    print(solution.firstMissingPositive([1,2,0]))
    
        
        
        
