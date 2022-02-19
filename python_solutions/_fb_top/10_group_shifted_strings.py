from collections import deque


class Solution:
    def rightSideView_bfs(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return

        rightside = []

        queue = deque([root])
        while queue:
            rightmost_node = None
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                rightmost_node = node

            rightside.append(rightmost_node.val)

        return rightside

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return

        rightside = []

        def dfs(node, level):
            completed_levels = len(rightside) - 1
            if level > completed_levels:
                rightside.append(node.val)

            if node.right:
                dfs(node.right, level + 1)

            if node.left:
                dfs(node.left, level + 1)

        dfs(root, 0)
        return rightside
