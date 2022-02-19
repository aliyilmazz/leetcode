class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[-1] * n for _ in range(n)]

        # initially n palindromic substrings
        for i in range(n):
            dp[i][i] = 1

        '''
        for each row in matrix, dp[i][i] and onwards is legit. 
        dp[i][j]
        i -> in range(0, n)
        j -> in range(i+1, n) (dp[i][i] is already set)
        '''
        for right in range(1, n):
            for left in range(right):
                if right == left + 1 or right == left + 2:
                    # 2 or 3 letter-long strings
                    if s[right] == s[left]:
                        dp[left][right] = 1
                    else:
                        dp[left][right] = 0
                else:
                    # bigger strings: inherit
                    if dp[left + 1][right - 1] == 1 and s[left] == s[right]:
                        dp[left][right] = 1
                    else:
                        dp[left][right] = 0

        return sum([row.count(1) for row in dp])



if __name__ == '__main__':
    s = "aaaaa"
    output = Solution().countSubstrings(s)
    print("output: %s" % output)