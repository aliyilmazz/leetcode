# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0

        def traverse(root):
            nonlocal max_diameter

            if not root:
                return 0

            left = traverse(root.left)
            right = traverse(root.right)
            max_diameter = max(max_diameter, left + right)
            return 1 + max(left, right)

        traverse(root)
        return max_diameter