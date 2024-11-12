# 350. Intersection of Two Arrays II
# Solved
# Easy

# Topics
# Companies
# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

 

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.
 

# Constraints:

# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000
 
class Solution(object):
    def intersect(self, nums1, nums2):
        common = []  #to keep track of the common numbers
        for i in range(len(nums1)): #for every number in num one 
            if nums1[i] in nums2: #if it is num 2
                common.append(nums1[i]) #add it to common
                nums2.remove(nums1[i]) #remove from num2 so we dont count twice
        return common #return common
#test
if __name__ == "__main__":
    solution = Solution()
    print(solution.intersect([1,2,2,1], [2,2]))