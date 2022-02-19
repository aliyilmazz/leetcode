class Solution:
    def climbStairs_recursion_with_memo(self, n: int) -> int:
        ''' basically DP with top-down approach '''
        memo = [-1] * (n+1)

        def climb(target):

            if target < 0:
                return 0

            if target == 0:
                return 1

            if memo[target] != -1:
                return memo[target]

            memo[target] = climb(target-1) + climb(target-2)
            return memo[target]

        return climb(n)

    def climbStairs(self, n: int) -> int:
        ''' dp with bottomup approach '''
        dp = [-1] * (n+1)  # dp[n] = number of ways to climb height N
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]


if __name__ == '__main__':
    n = 3
    output = Solution().climbStairs(n)
    print("N: %s, Output: %s" % (n, output))
