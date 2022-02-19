# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def traverse(self, node, p, q):
        if self.lca:
            return

        if not node:
            return False, False

        p_found, q_found = False, False

        if node == p:
            p_found = True
        if node == q:
            q_found = True

        p_found_in_left, q_found_in_left = self.traverse(node.left, p, q)
        p_found_in_right, q_found_in_right = self.traverse(node.right, p, q)

        p_found |= (p_found_in_left or p_found_in_right)
        q_found |= (q_found_in_left or q_found_in_right)

        if p_found and q_found:
            self.lca = node
            return

        else:
            return p_found, q_found

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.lca = None

        '''
            * set lca_found key
            * traverse(node, p, q)
                * if lca_found: return
                * if node is null, return


                p_found_in_left, q_found_in_left = traverse(node.left, p, q)
                p_found_in_right, q_found_in_right = traverse(node.right, p, q)

                p_found = (p_found_in_left or p_found_in_right)
                q_found = (q_found_in_left or q_found_in_right)

                if p_found and q_found: 
                    self.lca = node
                    self.lca_found = True
                    return

                else:
                    return p_found, q_found

        '''

        self.traverse(root, p, q)
        return self.lca


if __name__ == '__main__':
    p = TreeNode(2)
    q = TreeNode(3)
    root = TreeNode(1)
    root.left, root.right = p, q
    output = Solution().lowestCommonAncestor(root, p, q)
    print("Output: %s" % output.val)