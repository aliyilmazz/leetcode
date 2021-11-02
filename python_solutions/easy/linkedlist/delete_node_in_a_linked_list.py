from typing import List
from ...utils import ListNode


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # mock next node and skip it. :D
        node.val = node.next.val
        node.next = node.next.next


def verbose_assert(*args):
    output = Solution().deleteNode(*args)
    print("Input:  %s\nOutput: %s" % (args, output))


if __name__ == '__main__':
    args = ([1,2,3])
    verbose_assert(*args)
