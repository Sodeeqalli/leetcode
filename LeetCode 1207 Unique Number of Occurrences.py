# 1207. Unique Number of Occurrences
# Solved
# Easy

# Topics
# Companies

# Hint
# Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

 

# Example 1:

# Input: arr = [1,2,2,1,1,3]
# Output: true
# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
# Example 2:

# Input: arr = [1,2]
# Output: false
# Example 3:

# Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
# Output: true
 

# Constraints:

# 1 <= arr.length <= 1000
# -1000 <= arr[i] <= 1000


#Thought Process
#Okay, its a simple thing.
#We basically take a count of every element
#After which we check if there are no two numbers with the same count
#If true, return True, else, return False

#Let's Put int Practice

class Solution(object):
    def uniqueOccurrences(self, arr):
        times_occurred = {} #Map to map the numbers with their number of occurrences

        #Loop to get the number of occurrences of each number
        for i in range(len(arr)):  #for every number in the array
            if arr[i] in times_occurred:  #if we have come accross it before
                times_occurred[arr[i]] += 1 #increase its count by 1
            else:                            #if not
                 times_occurred[arr[i]] = 1  #initialize its count to one
        
        #after we get the number of occurences of each number, we see if any two numbers are the same
        track = [] #create an array to keep track of the counts
        for i in times_occurred.values(): #for number in the counts
            if i in track: #if it has been recorded in the array
                return False #return False automatically cause that means its no longer Unique
            track.append(i)  #append if it has not been recorded

        return True  #return True if it pases the uniuue number Test


if __name__ == "__main__":
    solution = Solution()
    
    print(solution.uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))