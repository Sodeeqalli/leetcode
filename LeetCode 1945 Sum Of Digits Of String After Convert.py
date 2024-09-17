# 1945. Sum of Digits of String After Convert
# Solved
# Easy

# Topics
# Companies

# Hint
# You are given a string s consisting of lowercase English letters, and an integer k.

# First, convert s into an integer by replacing each letter with its position in the alphabet (i.e., replace 'a' with 1, 'b' with 2, ..., 'z' with 26). Then, transform the integer by replacing it with the sum of its digits. Repeat the transform operation k times in total.

# For example, if s = "zbax" and k = 2, then the resulting integer would be 8 by the following operations:

# Convert: "zbax" ➝ "(26)(2)(1)(24)" ➝ "262124" ➝ 262124
# Transform #1: 262124 ➝ 2 + 6 + 2 + 1 + 2 + 4 ➝ 17
# Transform #2: 17 ➝ 1 + 7 ➝ 8
# Return the resulting integer after performing the operations described above.

 

# Example 1:

# Input: s = "iiii", k = 1
# Output: 36
# Explanation: The operations are as follows:
# - Convert: "iiii" ➝ "(9)(9)(9)(9)" ➝ "9999" ➝ 9999
# - Transform #1: 9999 ➝ 9 + 9 + 9 + 9 ➝ 36
# Thus the resulting integer is 36.
# Example 2:

# Input: s = "leetcode", k = 2
# Output: 6
# Explanation: The operations are as follows:
# - Convert: "leetcode" ➝ "(12)(5)(5)(20)(3)(15)(4)(5)" ➝ "12552031545" ➝ 12552031545
# - Transform #1: 12552031545 ➝ 1 + 2 + 5 + 5 + 2 + 0 + 3 + 1 + 5 + 4 + 5 ➝ 33
# - Transform #2: 33 ➝ 3 + 3 ➝ 6
# Thus the resulting integer is 6.
# Example 3:

# Input: s = "zbax", k = 2
# Output: 8
 

# Constraints:

# 1 <= s.length <= 100
# 1 <= k <= 10
# s consists of lowercase English letters.

#Thought Process
#Question as StraightForward As Possible,
#First, Convert string s to number
#We first find the positions of letters in string A in the alphabet with their ascii value.
#the values are also incremented based on positions in the alphabet, hence we can use this approach
#for instance if the ascii value of 'a' is 97, 'b' will be 98 and so on
#so when we get positions of each, we put in a string

#now we transform
#so we say, for the number of times we are asked to transform
#we create a placeoholder to calculate the value
#add individual numbers in the current converted string together
#assign the value to convert
#now the new convert will be operated on


class Solution(object):
    def getLucky(self, s, k):
       #convert
        converted = ""
        for i in range(len(s)):
            converted += str((ord(s[i]) - ord('a')) + 1)
        
        for i in range(k):
            value = 0
            for j in range(len(converted)):
                value += int(converted[j])
            
            converted = str(value)
        
        return value


if __name__ == "__main__":
    solution = Solution()
    print(solution.getLucky('iiii', 1))