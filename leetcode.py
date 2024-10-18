class Solution(object):
    def moveZeroes(self, nums):
        indices = []
        for i in range(len(nums)):
            if nums[i] == 0:
                indices.append(i)
                nums.append(0)
        print(nums, indices)
        for i in range(len(indices)):
            nums.p(indices[i])
            print(nums)
        return nums
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.moveZeroes([0,1,0,3,12]))