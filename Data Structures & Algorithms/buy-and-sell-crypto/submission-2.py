class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max_profit = 0
        # if len(prices)==1:
        #     return max_profit
        
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         curr_profit = prices[j] - prices[i]
        #         max_profit = max(curr_profit, max_profit)
        # return max_profit
        i=0
        min_buy = prices[i]
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_buy:
                min_buy = prices[i]
            else:
                curr_profit = prices[i] -  min_buy
                max_profit = max(curr_profit, max_profit)
        
        return max_profit
        