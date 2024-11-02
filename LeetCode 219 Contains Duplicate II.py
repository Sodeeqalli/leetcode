# 219. Contains Duplicate II
# Solved
# Easy

# Topics
# Companies
# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

# Example 1:

# Input: nums = [1,2,3,1], k = 3
# Output: true
# Example 2:

# Input: nums = [1,0,1,1], k = 1
# Output: true
# Example 3:

# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false
 

# Constraints:

# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109
# 0 <= k <= 105

#solution
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        seen = {} #a map to track numbers come across and their index
        for i in range(len(nums)): #for every number we come across
            if nums[i] in seen and abs(seen[nums[i]] - i) <= k: #if the number already in the map and 
                #the difference between the current index of the number and the previously recorde index less than or equal to K
                return True #return True
            else:  #else
                seen[nums[i]] = i #record the number and its current index
        return False  #return False
    
#test
if __name__ == "__main__":
    solution = Solution()
    print(solution.containsNearbyDuplicate([1,2,3,1,2,3], 2))