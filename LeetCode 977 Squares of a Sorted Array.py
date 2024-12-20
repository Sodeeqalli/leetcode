# 977. Squares of a Sorted Array
# Solved
# Easy

# Topics
# Companies
# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

# Example 1:

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
# Example 2:

# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]

#solution
class Solution(object):
    def sortedSquares(self, nums):
        return sorted([num*num for num in nums]) #return a sorted list of the square of the numbers
    
#test
if __name__ == "__main__":
    solution = Solution()
    print(solution.sortedSquares([-4,-1,0,3,10]))