# 345. Reverse Vowels of a String
# Solved
# Easy

# Topics
# Companies
# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

# Example 1:

# Input: s = "hello"
# Output: "holle"
# Example 2:

# Input: s = "leetcode"
# Output: "leotcede"
 

# Constraints:

# 1 <= s.length <= 3 * 105
# s consist of printable ASCII characters.

#Thought Process 
#We are to reverse the vowels in a string
#easy way to do this is, keep track of vowels and their indices
#then we reverse the order of the indices OR vowels
#then insert the vowels with corresponding indices in their position


#Lets put to practice

class Solution(object):
    def reverseVowels(self, s):
       #mark the indices with vowels
       #keep track of the vowels
       #reverse the vowels
       #put back in indices

        vowels = 'aeiouAEIOU' #vowels
        indices = [] #indices
        track = [] #track
    
        for i in range(len(s)): #for every letter in s
            if s[i] in vowels: #if the current letter is a vowel
                indices.append(i)  #add vowel's index indices = [2, 5]
                track.append(s[i]) #add vowel  track = ['e', 'o]

        reverseIndices = indices[::-1] #reverse the indices [5, 2]
        stringList = list(s) #turn string to list ['h', 'e', 'l' , 'l', 'o']

        for i in range(len(reverseIndices)):
            stringList[reverseIndices[i]] = track[i]

        return ''.join(stringList)

#test
if __name__ == "__main__":
    solution = Solution()
    
    print( solution.reverseVowels('hello'))