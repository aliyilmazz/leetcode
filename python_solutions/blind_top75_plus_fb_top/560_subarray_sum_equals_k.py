class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        ''' 

            * one go, trade from space
            * reuse previous solutions
            * end: range(0, n)
            * start: range(end, -1, -1)

            * dp[start][end] = sum of subarray, both start and end inclusive.

        '''

        n = len(nums)
        dp = [['_'] * (n) for _ in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]

        for end in range(1, n):
            for start in range(end - 1, -1, -1):
                dp[start][end] = nums[end] + dp[start][end - 1]

        print("dp: %s" % dp)
        return sum([row.count(k) for row in dp])


if __name__ == '__main__':
    nums = [1, 1, 1]
    k = 2
    output = Solution().subarraySum(nums, k)
    print("Nums: %s, k: %s\nOutput: %s\n\n" % (nums, k, output))

    nums = [1, 2, 3]
    k = 3
    output = Solution().subarraySum(nums, k)
    print("Nums: %s, k: %s\nOutput: %s\n\n" % (nums, k, output))

    nums = [-1, -1, 1]
    k = 0
    output = Solution().subarraySum(nums, k)
    print("Nums: %s, k: %s\nOutput: %s\n\n" % (nums, k, output))

