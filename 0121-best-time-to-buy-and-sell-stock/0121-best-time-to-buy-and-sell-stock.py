class Solution(object):
    def maxProfit(self, prices):
        min_prices = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            curr_profit = prices[i] - min_prices
            if curr_profit > profit:
                profit = curr_profit

            min_prices= min(min_prices, prices[i])

        return profit        


       
        