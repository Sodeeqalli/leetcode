# 242. Valid Anagram
# Solved
# Easy

# Topics
# Companies
# Given two strings s and t, return true if t is an 
# anagram
#  of s, and false otherwise.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false

 

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.

#solution
class Solution(object):
    def isAnagram(self, s, t):
        tlist = list(t) #convert T to a list so we can mutate it in our operation
        for i in range(len(s)): #for every letter in s
            if s[i] in tlist: #if the letter exists in T
                tlist.remove(s[i]) #remove it
            else:  #else
                return False    #return false, cause its automatically not an anagram
        return not tlist #return false if the list still contains letter after removing everything

#test
if __name__ == "__main__":
    solution = Solution()
    print(solution.isAnagram("anagram", "nagaram"))

 