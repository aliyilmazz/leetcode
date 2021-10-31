from typing import List

from collections import OrderedDict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        unseen_dict = OrderedDict()
        seen_set = set()
        for _index, _char in enumerate(s):
            if _char in seen_set:
                continue
            elif _char in unseen_dict:
                del unseen_dict[_char]
                seen_set.add(_char)
            else:
                unseen_dict[_char] = _index
        if len(unseen_dict) == 0:
            return -1
        return unseen_dict[next(iter(unseen_dict))]




def verbose_assert(str):
    _index = Solution().firstUniqChar(str)
    print("Input:  %s\nOutput: %s" % (str, _index))


if __name__ == '__main__':
    input = "loveleetcode"
    verbose_assert(input)
