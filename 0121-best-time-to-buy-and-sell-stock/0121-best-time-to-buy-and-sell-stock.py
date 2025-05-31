class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currMax = 0
        l, r = 0, 1
        while r < len(prices):
            if prices[r] > prices[l]:
                currMax = max(currMax, prices[r] - prices[l])
            else:
                l = r
            r += 1
        return currMax