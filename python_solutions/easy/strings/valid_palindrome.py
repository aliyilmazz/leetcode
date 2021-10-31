from typing import List


class Solution:
    def isPalindrome(self, s: str) -> bool:
        parsed_text = ''.join([x.lower() for x in s if x.isalnum()])
        return ''.join(reversed(parsed_text)) == parsed_text

def verbose_assert(*args):
    output = Solution().isPalindrome(*args)
    print("Input:  %s\nOutput: %s" % (*args, output))


if __name__ == '__main__':
    args = "A man, a plan, a canal: Panama"
    verbose_assert(args)
