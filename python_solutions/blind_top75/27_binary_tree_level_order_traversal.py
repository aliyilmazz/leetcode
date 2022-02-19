from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        stack, root = [], p
        p_inorder = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            node = stack.pop()
            p_inorder.append(node.val)
            root = node.right

        queue = deque([q])
        q_inorder = []
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                q_inorder.append(node.val if node else None)
                if node:
                    queue.append(node.left)
                    queue.append(node.right)

        queue = deque([p])
        p_inorder = []
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                p_inorder.append(node.val if node else None)
                if node:
                    queue.append(node.left)
                    queue.append(node.right)


        #print("p inorder: %s" % p_inorder)
        #print("q inorder: %s" % q_inorder)
        return p_inorder == q_inorder





if __name__ == '__main__':

    p = TreeNode(1, TreeNode(2), TreeNode(3))
    q = TreeNode(1, TreeNode(2), TreeNode(3))
    output = Solution().isSameTree(p, q)
    print("output: %s" % output)