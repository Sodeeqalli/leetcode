

# Code

# Testcase
# Testcase

# Test Result
# 136. Single Number
# Solved
# Easy

# Topics
# Companies

# Hint
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

 

# Example 1:

# Input: nums = [2,2,1]
# Output: 1
# Example 2:

# Input: nums = [4,1,2,1,2]
# Output: 4
# Example 3:

# Input: nums = [1]
# Output: 1
 

# Constraints:

# 1 <= nums.length <= 3 * 104
# -3 * 104 <= nums[i] <= 3 * 104
# Each element in the array appears twice except for one element which appears only once.

#solution
class Solution(object):
    def singleNumber(self, nums):
        tracker = [] #initialize an empty list to keep track of the numbers u come accross
        for i in range(len(nums)): #for every number in the list given to us
            if nums[i] in tracker: #if we have come across that letter before
                tracker.remove(nums[i]) #remove it form the tracker
            else:                       #else
                tracker.append(nums[i]) #add it to the tracker
        return tracker[0] #we return the only element in the tracker because that will be the only one that dont get removed from the list
    

#test
if __name__ == "__main__":
    solution = Solution()
    print(solution.singleNumber([4,1,2,1,2]))