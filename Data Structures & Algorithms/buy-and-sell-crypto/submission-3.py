class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_idx = 0
        max_profit = 0

        for idx, sell_price in enumerate(prices):
            if sell_price < prices[buy_idx]:
                buy_idx = idx
            else:
                curr_profit = sell_price - prices[buy_idx]
                max_profit = max(max_profit, curr_profit)
        
        return max_profit

    #verify[10,1,5,6,7,1]
    #10<10 no so cp = 10-10=0, mp=0
    #1<10 so buy idx = 1
    #5, cp = 5-1=4, mp=4
    #6, mp=5
    #7 mp =6
    #1, mp =6
    #
                

        