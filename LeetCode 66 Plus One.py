# 66. Plus One
# Solved
# Easy

# Topics
# Companies
# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

 

# Example 1:

# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].
# Example 2:

# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].
# Example 3:

# Input: digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].
 

# Constraints:

# 1 <= digits.length <= 100
# 0 <= digits[i] <= 9
# digits does not contain any leading 0's.

#solution
class Solution(object):
    def plusOne(self, digits):
        stringlist = [str(num) for num in digits] #convert the digits to string so we'll be able to concatenate them
        stringConvert = ''.join(stringlist) #join the strings in the list
        added = int(stringConvert) + 1 #convert to integer, then add one
        backstring = list(str(added)) #then convert back to string , then list cause we cant convert to list directly
        original = [int(letter) for letter in backstring] #convert each element back to an integer
        return original #return
    
#test
if __name__ == "__main__":
    solution = Solution()
    print(solution.plusOne([4,3,2,1]))