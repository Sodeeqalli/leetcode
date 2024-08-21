# 70. Climbing Stairs
# Solved
# Easy

# Topics
# Companies

# Hint
#You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# Example 1:


# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:


# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
 
# Constraints:
# 1 <= n <= 45

#Thought Process
#If its one stair, theres only a way. just one step
#If its two, there are two ways. two steps at a time or one twice
#If its three, there are three ways. two then one, one then two, one three times
#if its four, there are five. The idea is this follows a sequence. that the number of ways is the addition of the two previous number of ways
#This is generally known as the Fibonnacci sequence and we can implement this with dynamic programming

#Algorithm
#for the first two, we know, we return n
#to keep track of the rest, we create a dp array of size n+1, then set the dp[current index] to the previous one plus the one before that
#then we return dp[n]

class Solution(object):
    def climbStairs(self, n): 
        if n < 3: return n

        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2
        
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]
    
if __name__ == "__main__":
    solution = Solution()
    
    print(solution.climbStairs(5))