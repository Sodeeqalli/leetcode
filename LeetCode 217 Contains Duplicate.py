# 217. Contains Duplicate
# Solved
# Easy

# Topics
# Companies
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

# Example 1:

# Input: nums = [1,2,3,1]

# Output: true

# Explanation:

# The element 1 occurs at the indices 0 and 3.

# Example 2:

# Input: nums = [1,2,3,4]

# Output: false

# Explanation:

# All elements are distinct.

# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]

# Output: true

 

# Constraints:

# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109

#solution
class Solution(object):
    def containsDuplicate(self, nums):
        converted = set(nums) #convert the list of numbers to a set
        #it is converted to a set cause it will eliminate duplicates
        #if it eliminates duplicates, the length of the set is no longer equal to the original list
        #so our logic is, if the length is not the same, it contains duplicates
        return not len(converted) == len(nums)  #return true if they have same lenght, else false
    
#test 
if __name__ =="__main__":
    solution = Solution()
    print(solution.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))