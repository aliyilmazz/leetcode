class Solution:
    def countBits_intuitive(self, n: int) -> List[int]:

        bits = []

        for num in range(n + 1):
            total_bits = 0
            for pow in range(32):
                total_bits += ((num >> pow) & 1)
            bits.append(total_bits)

        return bits

    def countBits_hammingWeight(self, n):

        bits = []
        for num in range(n + 1):
            count = 0
            while num != 0:  #  max: log(n) loops where n=2^n-1
                num = num & num - 1
                count += 1
            bits.append(count)

        # overall: nlogn

        return bits

    def countBits_LSB(self, n):
        if n == 0:
            return [0]

        dp = [0] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            dp[i] = dp[i // 2] + i % 2

        return dp[:n + 1]

    def countBits(self, n):
        dp = [0] * (n + 1)
        x = 0
        b = 1

        # [0, b] is calculated
        while b <= n:
            while x < b and x + b <= n:
                dp[x + b] = dp[x] + 1
                x += 1
            x = 0
            b <<= 1  #  b = 2b

        return dp