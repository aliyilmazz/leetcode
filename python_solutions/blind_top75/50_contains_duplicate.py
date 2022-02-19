from typing import List


class Solution:

    def _rob(self, nums: List[int]) -> int:
        ''' regular rob function '''
        n = len(nums)

        if n == 1:
            return nums[0]

        dp = [-1] * n

        # dp[i] = maximum revenue from list, up to index i (inclusive)
        # we need dp[n-1]

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        def _dp(x):
            if dp[x] != -1:
                return dp[x]

            dp[x] = max(_dp(x - 2) + nums[x], _dp(x - 1))
            return dp[x]

        return _dp(n - 1)

    def rob(self, nums):

        if len(nums) == 1:
            return nums[0]

        return max(self._rob(nums[1:]), self._rob(nums[:-1]))


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    output = Solution().rob(nums)
    print("output: %s" % output)