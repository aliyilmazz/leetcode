# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def _rangeSumBST(self, root, low, high):

        if not root:
            return

        if low <= root.val <= high:
            self.sum += root.val
            self._rangeSumBST(root.left, low, high)
            self._rangeSumBST(root.right, low, high)
        elif root.val < low:
            # left tree is guaranteed to not contain any node in range
            # try right tree
            self._rangeSumBST(root.right, low, high)
        elif root.val > high:
            self._rangeSumBST(root.left, low, high)
        else:
            assert False, "Unreachable"

    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """

        # create list
        #  invoke recursive function
        # return list

        self.sum = 0

        if root:
            self._rangeSumBST(root, low, high)

        return self.sumSlac


if __name__ == '__main__':
    root = TreeNode(10, left=TreeNode(5, left=TreeNode(3), right=TreeNode(7)), right=TreeNode(15, right=TreeNode(18)))
    left = 7
    right = 15
    output = Solution().rangeSumBST(root, left, right)
    print("Input: %s\nOutput: %s" % ('%s-%s' % (left, right), output))
