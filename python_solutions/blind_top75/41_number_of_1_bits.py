from typing import List


class Solution:
    def reverseBits(self, n: int) -> int:
        reversed_num = 0
        power = 31

        while n:
            reversed_num += (n & 1) << power
            n >>= 1
            power -= 1


if __name__ == '__main__':
    output = Solution().reverseBits([3,4,5,1,2])
    print("output: %s" % output)