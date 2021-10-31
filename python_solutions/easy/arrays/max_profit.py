class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        i = 0
        max_profit = 0
        while i < len(prices) - 1:
            current_price = prices[i]
            future_price = prices[i + 1]

            if current_price < future_price:
                max_profit += (future_price - current_price)
            i += 1

        return max_profit


prices = [1, 2, 3, 4, 5]
max_profit = Solution().maxProfit(prices)
print("max profit: %s" % max_profit)
