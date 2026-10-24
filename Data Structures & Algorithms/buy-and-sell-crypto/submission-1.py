class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        max_profit = 0

        #sell on right 
        for right in range(1, len(prices)):
            if prices[right] < prices[left]:
                # cheaper to buy here
                left = right
            else:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)

        return max_profit