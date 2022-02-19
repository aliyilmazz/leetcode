# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional


class Solution:

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_gain = float('-inf')

        def _maxGain(root):
            '''

            base case: if no child, return self
            calculate left+self+right, test max=max(max,LSR)

            if either of child is negative, return only self
            else, return max
            child_gain = max(maxpath(left, right), 0)




            '''
            nonlocal max_gain

            if not root:
                return 0

            left_max = _maxGain(root.left)
            right_max = _maxGain(root.right)

            local_max = root.val + left_max + right_max
            max_gain = max(max_gain, local_max)  # test local loop

            child_max = max(max(left_max, right_max), 0)
            self_max = child_max + root.val  # propagate upwards

            max_gain = max(max_gain, self_max)  #  test global loop
            return self_max

        _maxGain(root)
        return max_gain


if __name__ == '__main__':
    tree = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    max_gain = Solution().maxPathSum(tree)
    print("max gain: %s" % max_gain)