# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers_dfs(self, root: Optional[TreeNode]) -> int:

        '''

        time: o(n)
        space: o(n)
        '''
        total = 0

        def traverse(node, strnum):
            nonlocal total

            strnum += str(node.val)

            if not node.left and not node.right:
                total += int(strnum)
                return

            if node.left:
                traverse(node.left, strnum)

            if node.right:
                traverse(node.right, strnum)

        traverse(root, '')
        return total

    def sumNumbers_iterative(self, root: Optional[TreeNode]) -> int:
        '''
        time = o(N), n=number of nodes
        space= up to o(H) max (stack extends and squeezes) in worst case it gets o(H)
        '''
        total = 0

        stack = [(root, 0)]
        while stack:
            root, curr_number = stack.pop()

            curr_number = curr_number * 10 + root.val
            if root.left is None and root.right is None:
                total += curr_number
            else:
                if root.left:
                    stack.append((root.left, curr_number))

                if root.right:
                    stack.append((root.right, curr_number))

        return total



