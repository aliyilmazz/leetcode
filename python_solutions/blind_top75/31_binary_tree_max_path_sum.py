from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        lowest_buy = float('inf')
        profit = float('-inf')

        for price in prices:
            if price < lowest_buy:
                lowest_buy = price
            else:
                profit = max(profit, price - lowest_buy)

        return profit if profit != float('-inf') else 0



if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    max_profit = Solution().maxProfit(prices)
    print("profit: %s" % max_profit)