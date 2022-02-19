from typing import List


class Solution:
    def maxSubArray_dp(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        max_sum = -9999999

        for i in range(n):
            dp[i][i] = nums[i]
            max_sum = max(max_sum, nums[i])

        for i in range(n):
            for j in range(i - 1, -1, -1):
                dp[i][j] = dp[i - 1][j] + nums[i]
                max_sum = max(max_sum, dp[i][j])

        for row in dp:
            print(row)

        return max_sum

    def maxSubArray(self, nums):


        current_subarray_value = 0
        max_subarray_value = -99999

        for num in nums:
            current_subarray_value += num
            max_subarray_value = max(max_subarray_value, current_subarray_value)
            current_subarray_value = max(0, current_subarray_value)

        return max_subarray_value



if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    output = Solution().maxSubArray(nums)
    print("nums:%s\noutput:%s\n\n" % (nums, output))

    nums = [-2]
    output = Solution().maxSubArray(nums)
    print("nums:%s\noutput:%s\n\n" % (nums, output))

    nums = [-2, -1]
    output = Solution().maxSubArray(nums)
    print("nums:%s\noutput:%s\n\n" % (nums, output))

    nums = [-2, 1]
    output = Solution().maxSubArray(nums)
    print("nums:%s\noutput:%s\n\n" % (nums, output))


