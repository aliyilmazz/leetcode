# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.stack = []

    def _yield(self):
        while self.stack or self.root:
            while self.root:
                self.stack.append(self.root)
                self.root = self.root.left
            node = self.stack.pop()
            if node.right:
                self.root = node.right
            yield node.val

    def next(self):
        return next(self._yield())

    def hasNext(self) -> bool:
        return self.stack or self.root

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()