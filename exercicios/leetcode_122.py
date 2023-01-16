# 122. Best Time to Buy and Sell Stock II

class Solution:
    def get_max_value(
        self, max_value: int, idx: int, prices:list[int], size: int
    ) -> tuple[int, int]:
        while idx < size and max_value < prices[idx]:
            max_value = prices[idx]
            idx += 1

        return max_value, idx

    def maxProfit(self, prices: list[int]) -> int:
        idx = 0
        max_value = -10 
        min_value = prices[0]
        profit = 0
        size = len(prices)

        while idx < size:

            if min_value > prices[idx]:
                min_value = prices[idx]

            max_value, idx = self.get_max_value(max_value, idx, prices, size)
            
            profit += (max_value - min_value)

            if idx < size:
                min_value = prices[idx]

            idx += 1
            max_value = -10
        
        return profit
                
