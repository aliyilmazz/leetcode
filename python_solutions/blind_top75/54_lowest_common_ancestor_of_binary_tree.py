# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if p.val > root and q.val > root:
            self.lowestCommonAncestor(root.right, p, q)
        elif p.val < root and q.val < root:
            self.lowestCommonancestor(root.left, p, q)
        else:
            return root
