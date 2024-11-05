""" 
DIFFICULTY:  Easy
PROBLEM:     0121. Best Time to Buy and Sell Stock
             https://leetcode.com/problems/best-time-to-buy-and-sell-stock 
PATTERN:     Greedy Algorithms
"""

class Solution:

    """
    https://www.hello-algo.com/en/chapter_greedy/greedy_algorithm/
    https://www.hackerearth.com/practice/algorithms/greedy/basics-of-greedy-algorithms/tutorial/
    """

    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)

        profit = 0
        i = 0
        while i < n:

            j = i + 1
            while j < n and prices[j] > prices[i]:
                diff = prices[j] - prices[i]

                if diff > profit:
                    profit = diff

                j += 1
            i += 1

        return profit