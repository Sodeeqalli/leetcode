# 1768. Merge Strings Alternately
# Solved
# Easy

# Topics
# Companies

# Hint
# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.

 

# Example 1:

# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r
# Example 2:

# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.
# word1:  a   b 
# word2:    p   q   r   s
# merged: a p b q   r   s
# Example 3:

# Input: word1 = "abcd", word2 = "pq"
# Output: "apbqcd"
# Explanation: Notice that as word1 is longer, "cd" is appended to the end.
# word1:  a   b   c   d
# word2:    p   q 
# merged: a p b q c   d
 

# Constraints:

# 1 <= word1.length, word2.length <= 100
# word1 and word2 consist of lowercase English letters.


#Thought process, to merge two string alternatively. It simply means I add a letter from one string, then a letter at that same index of another string, 
#Like that till, one of the strings is exhausted, then you just add the rest of the remaining string
#lets put to practice
class Solution(object):
    def mergeAlternately(self, word1, word2):
        limit1 = len(word1) -1  #defining the number of times we can iterate over the first word
        limit2 = len(word2) -1 #same for the second
        word = "" #the word variable
        i = 0 #pointer for the first string
        j = 0 #pointer for the second string
        while i <= limit1 and j<= limit2:  #while both strings have content
            word += word1[i]  #add the letter at the current index  of word1 to our word variable
            word += word2[j] #add the letter at the current index of word2 to our word variable
            i+=1 #increment pointer for word 1
            j+=1 #increment pointer for word 2
        
        #when a word is exhausted we just add the remaining content of the second
        #since we cant say for sure which word it will be, we check both words
        
        #check for word 1
        while i <= limit1:  #if and while word1 has content
            word += word1[i] #add the letter at current index to word 1
            i +=1 #increase pointer
        
        #check for word 2
        while j <= limit2:
            word += word2[j]
            j +=1
        
        return word


