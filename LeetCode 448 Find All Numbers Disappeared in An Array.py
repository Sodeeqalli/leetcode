# 448. Find All Numbers Disappeared in an Array
# Solved
# Easy

# Topics
# Companies

# Hint
# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

# Example 1:

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]
# Example 2:

# Input: nums = [1,1]
# Output: [2]
 

# Constraints:

# n == nums.length
# 1 <= n <= 105
# 1 <= nums[i] <= n
 

#Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space

#solution
class Solution(object):
    def findDisappearedNumbers(self, nums):
        disappeared = [] #an array to keep track of numbers
        setnums = set(nums) #reduce size of numbers to iterate over to increase efficiency
        for i in range(len(nums)): #for every number in the original list
            if i+1 not in setnums: #if it is not in the reduced list
                disappeared.append(i+1) #add it to the "disappeared" array
        return disappeared #return the array

#test
if __name__ == "__main__":
    solution = Solution()
    print(solution.findDisappearedNumbers([4,3,2,7,8,2,3,1]))
    
