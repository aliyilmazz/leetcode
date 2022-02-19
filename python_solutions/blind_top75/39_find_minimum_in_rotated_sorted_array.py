from typing import List


class Solution:
    def maxProduct(self, nums):

        if not nums:
            return 0

        local_max = nums[0]
        local_min = nums[0]

        max_product = local_max
        n = len(nums)
        for i in range(1, n):
            num = nums[i]
            local_max = max(num, local_max * num, local_min * num)
            local_min = min(num, local_max * num, local_min * num)
            max_product = max(max_product, local_max)
        return max_product




if __name__ == '__main__':
    output = Solution().maxProduct([-4, -3, -2])
    print("output: %s" % output)