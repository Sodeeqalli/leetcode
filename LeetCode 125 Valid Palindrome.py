# 125. Valid Palindrome
# Solved
# Easy

# Topics
# Companies
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
 

# Constraints:

# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.

#solution
class Solution(object):
    def isPalindrome(self, s):
        converted = s.strip().lower() #we remove all whitespaces and set all characters to their lowercase
        listchar = [char for char in converted if char.isalnum()] #we create a list that take alls the characters in converted that are alphanumeric
        return listchar == listchar[::-1] #we return a boolean comparing if the list is the same in reverse which is the definition of the palindrome

#test
if __name__ == "__main__":
    solution = Solution()
    print( solution.isPalindrome("A man, a plan, a canal: Panama"))
   