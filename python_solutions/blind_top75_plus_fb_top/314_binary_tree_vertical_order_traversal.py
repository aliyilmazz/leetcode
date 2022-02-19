# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import defaultdict, deque


class Solution(object):

    # def _verticalOrder(self, root, level):
    #     if not root:
    #         return
    #
    #     self.vertical_level_map[level].append(root.val)
    #     self._verticalOrder(root.left, level - 1)
    #     self._verticalOrder(root.right, level + 1)

    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        ''' 
            naive approach (presumed to take place in o-nlogn time, o-n space)


            *** store a vertical_level->node map.
            *** starting from root, set vertical_level=0
            *** for left and right subtrees, reinvoke function, adjusting level accordingly
            *** let all functions use a class-level map.
        '''

        self.vertical_level_map = defaultdict(list)

        # self._verticalOrder(root, 0) # populate map

        fifo_queue = deque()

        if root:
            fifo_queue.append((0, root))

        while fifo_queue:
            level, node = fifo_queue.popleft()
            self.vertical_level_map[level].append(node.val)
            if node.left:
                fifo_queue.append((level-1, node.left))
            if node.right:
                fifo_queue.append((level+1, node.right))





        vertical_levels = list(self.vertical_level_map.keys())
        vertical_levels.sort()

        levels_listing = []
        for level in vertical_levels:
            levels_listing.append([level_member for level_member in self.vertical_level_map[level]])

        return levels_listing




if __name__ == '__main__':
