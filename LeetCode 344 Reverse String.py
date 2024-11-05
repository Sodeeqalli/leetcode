# 344. Reverse String
# Solved
# Easy

# Topics
# Companies

# Hint
# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.

 

# Example 1:

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:

# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
 

# Constraints:

# 1 <= s.length <= 105
# s[i] is a printable ascii character.

#solution
class Solution(object):
    def reverseString(self, s):
        i, j= 0, len(s)-1 #initialize two pointers at the beginning and end of the array
        while j > i: #while the j is less than i
            s[i], s[j] = s[j], s[i] #the letter at the first pointer position sshould witch places with the pointer at the second position
            i +=1 #increment i
            j -=1 #increment j
        return s #return the string array

#test
if __name__ == "__main__":
    solution = Solution()
    print(solution.reverseString(["H","a","n","n","a","h"]))