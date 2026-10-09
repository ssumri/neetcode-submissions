class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mprofit = 0
        for i in range(len(prices)):
            if max(prices[i:]) - prices[i] > mprofit:
                mprofit = max(prices[i:]) - prices[i]
        return mprofit
        