# 14. Longest Common Prefix
# Solved
# Easy

# Topics
# Companies
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.


#Thought Process
#Firstly, the longest common prefix can only be as long as the shortest string. so we find the shortest string.
# that'll be the number of times we'll iterate over each string
#so basically for each iteration, we check if all letters are the same for a postion in each string
#once there is a mismatch, we return the current prefix
#If there is no mismatch, we move to the next letter

#Let us put that in practice

class Solution(object):
    def longestCommonPrefix(self, strs):
        min_len = min ([len(string) for string in strs]) #getting the length of the smallest string for iteration count

        prefix = "" #intial prefix
        for i in range(min_len): #for the length of shortest string
            character = strs[0][i] #let character be the i + 1 th letter at the first string
            for j in range(1, len(strs)): #then for the remaining strings
                if strs[j][i] != character: #if the character at that exact position is not equal to the character
                    return prefix  #return the current prefix
            prefix += character  #after the check is done for all strings, we move to the next position and repeat the process
        
        return prefix
    
#test
if __name__ == "__main__":
    solution = Solution()
    
    print(solution.longestCommonPrefix(["flower","flow","flight"]))
    