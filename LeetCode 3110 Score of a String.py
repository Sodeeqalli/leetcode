# 3110. Score of a String
# Solved
# Easy

# Topics
# Companies

# Hint
# You are given a string s. The score of a string is defined as the sum of the absolute difference between the ASCII values of adjacent characters.

# Return the score of s.

 

# Example 1:

# Input: s = "hello"

# Output: 13

# Explanation:

# The ASCII values of the characters in s are: 'h' = 104, 'e' = 101, 'l' = 108, 'o' = 111. So, the score of s would be |104 - 101| + |101 - 108| + |108 - 108| + |108 - 111| = 3 + 7 + 0 + 3 = 13.

# Example 2:

# Input: s = "zaz"

# Output: 50

# Explanation:

# The ASCII values of the characters in s are: 'z' = 122, 'a' = 97. So, the score of s would be |122 - 97| + |97 - 122| = 25 + 25 = 50.

 

# Constraints:

# 2 <= s.length <= 100
# s consists only of lowercase English letters.

#very straight forward
#so iterate over every letter in the string, get the abs difference of the ascii value of it and the nect letter and add to result
#put a condition so that it doesnt go out of range cause i+1 will eventually be i+ last letter which is out of range


#solution

class Solution(object):
    def scoreOfString(self, s):
        result = 0 #result variable
        for i in range(len(s)): #for every letter
            if i + 1 < len(s): #and the letter index + 1 is still in range
                result += abs(ord(s[i]) - ord(s[i+1])) #add the absolute difference of the letter and next ascii values to result
        return result #return result
 
 #test   
if __name__ == "__main__" :
    solution = Solution()

    print(solution.scoreOfString('brother'))
       

