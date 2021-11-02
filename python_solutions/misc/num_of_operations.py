from typing import List


class Solution:
    def foo(self, input: List[int]) -> bool:
        return True


def verbose_assert(*args):
    output = Solution().foo(*args)
    print("Input:  %s\nOutput: %s" % (args, output))


if __name__ == '__main__':
    args = ([1,2,3])
    verbose_assert(*args)
