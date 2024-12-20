# 121. Best Time to Buy and Sell Stock
# Solved
# Easy

# Topics
# Companies
# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
 

# Constraints:

# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104

#solution
class Solution(object):
    def maxProfit(self, prices):
        minimum_price = prices[0] #the lowest price you can buy
        profit = 0 #the highest profit recorded

        for i in range(1, len(prices)): #for everyday after the first day
            if prices[i] < minimum_price: #if stocks available for cheaper
                minimum_price = prices[i] #we hold as the current stock
            elif prices[i] - minimum_price > profit: #if the difference between current price and the current stock i hold is greater than the highest profit i have recorded
                profit = prices[i] - minimum_price #i record as the highest profit
        return profit #return

#test
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProfit([7,1,5,3,6,4]))
