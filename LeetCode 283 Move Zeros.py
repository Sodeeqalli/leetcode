# 283. Move Zeroes
# Solved
# Easy

# Topics
# Companies

# Hint
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

 

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]
 

# Constraints:

# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1
 

# Follow up: Could you minimize the total number of operations done?

#solution
class Solution(object):
    def moveZeroes(self, nums):
        indices = [] #to keep track of the indices where we find zero
        for i in range(len(nums)): #for every number in our array
            if nums[i] == 0: #if the number equal zero
                indices.append(i) #keep track of the index
        for i in range(len(indices)): #for every index we have kept track of
            nums.append(0) #append zero to the original array
            nums.pop(indices[i]-i) #remove zero from the index stored minus the iteration count
            #we remove iteration count cause as we are popping from the front, the array moves one side to the left
        return nums
    
    #test
if __name__ == "__main__":
    solution = Solution()
    print(solution.moveZeroes([0,1,0,3,12]))    ``