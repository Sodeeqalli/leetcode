# 20. Valid Parentheses
# Solved
# Easy
# Topics
# Companies
# Hint
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 
# Example 1:
# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false
 

# Constraints:
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

#Thought process
        #If stack is empty and we encounter a closing bracket, just return false, if not in map, we append
        #if its not empty, we append if its not in map or its in map but doesnt match top of stack, else pop 
         
        # we can think of the algorithm as :
        # If the parenthesis in my map, move forward if not just append
        # if the stack is not empty, move forward if not return False
        # if the map value of the parenthesis is equal to the top of the stack. POP
        # if it is not equal to the top of the stack. APPEND
        
        
#DATA STRUCTURE : MAP , ARRAY
class Solution(object):
    def isValid(self, s):
        myMap = {
            ')' : '(',
            '}' : '{',
            ']' : '['       
                 }
        stack = []
        
        for i in range(len(s)):
            if s[i] in myMap:
                if stack:
                    if stack[-1] == myMap[s[i]]:
                        stack.pop()
                    else:
                        stack.append(s[i])
                else:
                    return False
            else:
                stack.append(s[i])       
        return not stack
                    
                    
            
            
        
        
        
if __name__ == "__main__":
    solution = Solution()
    
    #Testing with parenthesis
    print(solution.isValid('{([])}'))



