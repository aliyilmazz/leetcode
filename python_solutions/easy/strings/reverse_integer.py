from typing import List


class Solution:
    def reverse(self, x: int) -> int:

        strint = str(x) if x>=0 else str(x)[1:]

        result = int(''.join(reversed(strint)))
        SIGNED_INT_MAX = 2**31 - 1
        SIGNED_INT_MIN = -1 * (2**31)

        result = result * -1 if x<0 else result
        return result if SIGNED_INT_MIN < result < SIGNED_INT_MAX else 0

def verbose_assert(input_integer):
    output = Solution().reverse(input_integer)
    print("Input:  %s\nOutput: %s" % (input_integer, output))


if __name__ == '__main__':
    input = -123
    verbose_assert(input)
