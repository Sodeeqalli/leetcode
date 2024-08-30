# Given an integer x, return true if x is a 
# palindrome
# , and false otherwise.

 

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

# Constraints:

# -231 <= x <= 231 - 1

#Thought Process
#Palindrome basically means a sequence of characters is the same as the sequence reversed
#so we basically do that check
#All we have to do is convert the integer to a string and then do the check

class Solution(object):
    def isPalindrome(self, x): 
        palindrome = str(x) == str(x)[::-1] #simply check if the string version of x is equal to the inverted string version of x and store in a variable
        return palindrome #return the variable lol 
    
    
#Test
if __name__ == "__main__":
    solution = Solution()
    print(solution.isPalindrome(121))
    
    
    

 