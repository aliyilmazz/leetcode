from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def _isValidBST(self, root, lesser_parents, greater_parents):
        if not root:
            return True

        for lesser_parent in lesser_parents:
            if root.val <= lesser_parent:
                return False

        for greater_parent in greater_parents:
            if root.val >= greater_parent:
                return False

        lesser_parents_with_root = lesser_parents.copy()
        lesser_parents_with_root.add(root.val)
        greater_parents_with_root = greater_parents.copy()
        greater_parents_with_root.add(root.val)

        left_valid = self._isValidBST(root.left, lesser_parents, greater_parents_with_root)
        right_valid = self._isValidBST(root.right, lesser_parents_with_root, greater_parents)

        return left_valid and right_valid

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self._isValidBST(root, set(), set())




if __name__ == '__main__':
    root = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
    output = Solution().isValidBST(root)
    print("output: %s" % output)



