class Solution(object):
    def isValid(self, s):
        myMap = {
            ')' : '(',
            '}' : '{',
            ']' : '['       
                 }

        stack = []
        #if its not the first element
        #if its a closing bracket
        #if the bracket before it is its map corr

        for i in range(len(s)):
            if i > 0 and s[i] in myMap and stack[-1] == myMap[s[i]]:
                stack.pop()
            else:
                stack.append(s[i])
        return  not stack


