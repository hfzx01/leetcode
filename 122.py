class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        count = 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                count += prices[i+1]-prices[i]
        return count