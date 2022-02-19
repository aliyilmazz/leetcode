
from typing import List

from functools import lru_cache


class Solution:
    def rob_dpmemo(self, nums: List[int]) -> int:
        '''

        2 7 9 3 1

        2 + rob[931]
        rob[7931]
        '''

        n = len(nums)
        dp = [-1] * (n + 1)
        dp[n] = 0
        dp[n - 1] = nums[-1]

        # @lru_cache
        def rob(start_index):
            if start_index > n:
                return 0

            if dp[start_index] != -1:
                return dp[start_index]

            cand1 = nums[start_index] + rob(start_index + 2)
            cand2 = rob(start_index + 1)
            result = max(cand1, cand2)
            dp[start_index] = result
            return result

        result = rob(0)
        return result

    def rob_dp_bottom_to_top(self, nums):
        n = len(nums)

        if n == 1:
            return nums[0]

        dp = [-1] * (n + 1)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

        return dp[n - 1]

    def rob(self, nums):

        n = len(nums)
        if n == 1:
            return nums[0]

        two_prev = nums[0]
        prev = max(nums[0], nums[1])
        max_value = prev

        for i in range(2, n):
            max_value = max(nums[i] + two_prev, prev)
            two_prev = prev
            prev = max_value

        return max_value

if __name__ == '__main__':
    output = Solution().rob([1,2,3,1])
    print("output: %s" % output)