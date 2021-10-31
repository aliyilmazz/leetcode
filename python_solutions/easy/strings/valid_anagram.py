from typing import List


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return ''.join(sorted(s)) == ''.join(sorted(t))


def verbose_assert(*args):
    output = Solution().isAnagram(*args)
    print("Input:  %s\nOutput: %s" % (args, output))


if __name__ == '__main__':
    args = "ratr", "tarr"
    verbose_assert(*args)
