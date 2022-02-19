"""
# Definition for a Node.
"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':

        if not root:
            return None

        stack = []

        leftmost, rightmost = None, None
        prev = None
        while stack or root:
            while root:
                # prioritize left
                stack.append(root)
                root = root.left

            node = stack.pop()
            print("current val: %s" % node.val)

            if not leftmost:
                leftmost = node
            rightmost = node

            if prev:
                prev.right = node
                node.left = prev

            prev = node

            # queue right
            if node.right:
                root = node.right

        leftmost.left = rightmost
        rightmost.right = leftmost

        return leftmost

    def treeToDoublyList_dfs(self, root: 'Optional[Node]') -> 'Optional[Node]':

        def dfs(node):

            if not node:
                return None, None

            ll, lr, rl, rr = node, node, node, node

            if node.left:
                ll, lr = dfs(node.left)
            if node.right:
                rl, rr = dfs(node.right)

            if node.left:
                node.left = lr
                lr.right = node

            if node.right:
                node.right = rl
                rl.left = node

            rr.right = ll
            ll.left = rr

            return ll, rr

        left, right = dfs(root)
        return left



if __name__ == '__main__':
    tree = Node(2, left=Node(1))
    Solution().treeToDoublyList(tree)
