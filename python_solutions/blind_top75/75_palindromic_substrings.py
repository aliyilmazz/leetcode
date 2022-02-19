# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isIdenticalTree(self, root1, root2):
        if not root1 and not root2:
            return True

        if not root1 or not root2:
            return False

        if root1.val == root2.val:
            return self.isIdenticalTree(root1.left, root2.left) and self.isIdenticalTree(root1.right, root2.right)

        return False

    def isSubtree_ost(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True

        if not root or not subRoot:
            return False

        if self.isIdenticalTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)



    def isSubtree(self, root, subRoot):
        def merkle(node):
            if not node:
                return '#'
            m_left = merkle(node.left)
            m_right = merkle(node.right)
            node.merkle = m_left + str(node.val) + m_right
            return node.merkle

        merkle(root)
        merkle(subRoot)

        def dfs(node):
            if not node:
                return False
            return (node.merkle == subRoot.merkle or dfs(node.left) or dfs(node.right))

        return dfs(root)