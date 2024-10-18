# 27. Remove Element
# Solved
# Easy

# Topics
# Companies

# Hint
# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
# Return k.


class Solution(object):
    def removeElement(self, nums, val):
        position = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[position] =nums[i]
                position +=1
        return position
        
if __name__ == "__main__":
    solution = Solution()
    print(solution.removeElement([3,2,2,3], 3))