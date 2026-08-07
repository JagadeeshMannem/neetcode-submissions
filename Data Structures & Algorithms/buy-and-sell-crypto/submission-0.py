class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        first = 0
        last = 1
        best = 0
        
        while last < len(prices):
            if prices[first] < prices[last]:
                profit = prices[last] - prices[first]
                best = max(best, profit)
            else:
                first = last
            last += 1
        
        return best