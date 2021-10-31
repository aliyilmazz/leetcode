from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        runner = 0
        inverse_runner = len(s)-1
        while runner < inverse_runner:
            temp = s[runner]
            s[runner] = s[inverse_runner]
            s[inverse_runner] = temp
            runner += 1
            inverse_runner -= 1


def verbose_assert(_str):
    print("Str(before): %s" % _str)
    Solution().reverseString(_str)
    print("Str(after) : %s" % _str)


if __name__ == '__main__':
    input = list("Hannah")
    verbose_assert(input)
