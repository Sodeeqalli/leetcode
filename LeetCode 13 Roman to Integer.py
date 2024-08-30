
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

 

# Example 1:

# Input: s = "III"
# Output: 3
# Explanation: III = 3.
# Example 2:

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 3:

# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

# Constraints:

# 1 <= s.length <= 15
# s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
# It is guaranteed that s is a valid roman numeral in the range [1, 3999].

#Though Process
#Basically when we are converting from roman numerals, we do basic addition like
#L means + 50
#V mean + 5 and so on
#So we are meant to iterate over every letter, then add their value
#Butttttttt there is an exception, a single one.
#when the next letter has a higher value than the current one.
#in that case we add the  [ value of the higher - value of current]
# then move the pointer by two places

#Let's put this in practice

class Solution(object):
    def romanToInt(self, s):
        myMap = {  #store values in a map
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
        }
        value = 0
        i = 0
        while i < len(s):
            if i + 1 < len(s) and myMap[s[i]] < myMap[s[i + 1]]:
                value += myMap[s[i+1]] - myMap[s[i]]
                i += 2
            else:
                value += myMap[s[i]]
                i+=1
            
        return value


#Test
if __name__ == "__main__":
    solution = Solution()
    
    print(solution.romanToInt("LVIII"))
    print(solution.romanToInt("MCMXCIV"))
