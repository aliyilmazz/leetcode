"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':

        p_parents = []
        p_traverser = p
        while p_traverser:
            p_parents.append(p_traverser)
            p_traverser = p_traverser.parent

        q_parents = []
        q_traverser = q
        while q_traverser:
            q_parents.append(q_traverser)
            q_traverser = q_traverser.parent


        p_parent_pointer = len(p_parents)-1
        q_parent_pointer = len(q_parents)-1

        assert p_parents[p_parent_pointer] == q_parents[q_parent_pointer]
        while True:
            new_p_pointer = p_parent_pointer - 1
            new_q_pointer = q_parent_pointer - 1
            if (
               new_p_pointer >= 0 and new_q_pointer >= 0 and p_parents[new_p_pointer] == q_parents[new_q_pointer]
            ):
                p_parent_pointer = new_p_pointer
                q_parent_pointer = new_q_pointer
            else:
                break  # our LCA is what either of our pointer points to

        return p_parents[p_parent_pointer]



# if __name__ == '__main__':
#     Solution().lowestCommonAncestor()
