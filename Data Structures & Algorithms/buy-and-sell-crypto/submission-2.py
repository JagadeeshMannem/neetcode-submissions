class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        ##track left and right index of the sliding window
        left, right = 0, 1

        while right < len(prices):
            #if difference between left and right index is better than current profit, update the profit
            if prices[right] > prices[left]:
                diff = prices[right] - prices[left]
                profit = max(diff, profit)

            else: 
                left = right

        #always iterate ther right index
            right += 1
        
        return profit

        #?when to move the left index