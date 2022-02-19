class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1] * n for _ in range(m)]

        dp[m-1][n-1] = 0  # base
        dp[m-1][n-2] = 1  # base case
        dp[m-2][n-1] = 1  # base case

        def f(i, j):
            if i >= m or j >= n:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            dp[i][j] = f(i+1, j) + f(i, j+1)
            return dp[i][j]

        return f(0, 0)


if __name__ == '__main__':
    m, n = 3, 7
    output = Solution().uniquePaths(m, n)
    print("M: %s, N: %s, Output: %s" % (m, n, output))