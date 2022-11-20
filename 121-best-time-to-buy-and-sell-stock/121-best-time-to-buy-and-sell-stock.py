class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = prices[0]
        maxP = 0

        for price in prices:
            min_price = min(price, min_price)
            compare_profit = price - min_price
            maxP = max(compare_profit, maxP)

        return maxP