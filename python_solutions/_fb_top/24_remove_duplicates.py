# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        levels = defaultdict(lambda: defaultdict(list))

        def traverse(node, row, col):
            if not node:
                return

            levels[col][row].append(node.val)
            traverse(node.left, row + 1, col - 1)
            traverse(node.right, row + 1, col + 1)

        traverse(root, 0, 0)

        results = []
        for col_level in sorted(levels.keys()):
            column_data = []

            rows = levels[col_level]
            for row in sorted(rows.keys()):
                column_data.extend(sorted(rows[row]))

            results.append(column_data)

        return results
