# 1. Two Sum
# Solved
# Easy

# Topics
# Companies

# Hint
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
 

# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

#Thought Process
#Basically finding which two numbers add up to a number
#An optimal approach to achieve this is by:
#checking a number, calculating its complement from the target. Then storing the number if we have not come accross it's complement
#if we have we just return the number and the complement's index

class Solution(object):
    def twoSum(self, nums, target):
        seen = {} #keep track of the numbers we have seen and their index
        
        for i in range(len(nums)): #for every number in the list
            complement = target - nums[i] #we calculate the complement from the target
            if complement in seen: #if we have reorded the number in seen
                return [seen[complement], i] #return the index of that number and the one of the current number

            seen[nums[i]] = i  #record the number if we have not found the solution

#test
if __name__ == "__main__" :
    solution = Solution()
    
    print(solution.twoSum([3,2,4], 6))