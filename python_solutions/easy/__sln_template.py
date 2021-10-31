from typing import List


class Solution:
    def foo(self, input: List[int]) -> bool:
        return True


def verbose_assert(_list):
    output = Solution().foo(_list)
    print("Input:  %s\nOutput: %s" % (_list, output))


if __name__ == '__main__':
    input = [1, 2, 3]
    verbose_assert(input)
