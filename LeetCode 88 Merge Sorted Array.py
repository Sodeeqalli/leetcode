# 88. Merge Sorted Array
# Solved
# Easy

# Topics
# Companies

# Hint
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
# Example 1:

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
# Example 2:

# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].
# Example 3:

# Input: nums1 = [0], m = 0, nums2 = [1], n = 1
# Output: [1]
# Explanation: The arrays we are merging are [] and [1].
# The result of the merge is [1].
# Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
 

# Constraints:

# nums1.length == m + n
# nums2.length == n
# 0 <= m, n <= 200
# 1 <= m + n <= 200
# -109 <= nums1[i], nums2[j] <= 109

#Thought Process
#Two arrays sorted, to merge them, space has been left for us in the first array. first array has a size of m(the actual array) + n(space to accomodate merging)
#The strategy will be to start from the last index of the first array that has space for merging
#Then we compare the last elements from the first and second arrays, the largest will be added to last index
#then we continue this process until the second array is empty
# if there is leftover in the second array, that tells us that all the elements are smaller than the smallest number in A so they should fill the positions

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        #The last index where we would input bigger value
        lastIndex = m + n - 1
        
        # the index to manage the first array
        i = m - 1
        
        #index to manage the second array
        j = n -1
        
        #now the logic for the movement, while both arrays are not empty, do your comparisons
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[lastIndex] = nums1[i]
                i -= 1
            else:
                nums1[lastIndex] = nums2[j]
                j -= 1
            lastIndex -= 1
        #if there are leftovers in the second array
        while j >= 0:
            nums1[lastIndex] = nums2[j]
            j -=1
            lastIndex -= 1
        
        return nums1
    
    #test
if __name__ == "__main__":
    solution = Solution()
    
    print( solution.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,9,12], n = 3))
            