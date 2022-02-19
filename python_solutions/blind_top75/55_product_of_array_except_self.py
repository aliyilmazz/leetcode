# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def lowestCommonAncestor_recursive(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def recurse_tree(root):
            if not root:
                return False

            left = recurse_tree(root.left)
            right = recurse_tree(root.right)
            mid = root == p or root == q

            if mid + left + right >= 2:
                self.lca = root

            return mid or left or right

        recurse_tree(root)
        return self.lca

    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return

        stack = [root]

        #  parent pointers
        parent = {root: None}

        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)

        p_parents = []
        p_traverser = p
        while p_traverser:
            p_parents.append(p_traverser)
            p_traverser = parent[p_traverser]

        q_traverser = q
        while q_traverser:
            if q_traverser in p_parents:
                return q_traverser
            q_traverser = parent[q_traverser]





