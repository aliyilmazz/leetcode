# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _maxDepth(self, node):
        if not node:
            return 0

        return 1 + max(self._maxDepth(node.left), self.maxDepth(node.right))

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self._maxDepth(root)