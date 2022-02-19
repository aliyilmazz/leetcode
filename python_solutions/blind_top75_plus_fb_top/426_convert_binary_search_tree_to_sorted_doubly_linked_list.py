"""
# Definition for a Node.
"""


from typing import Optional

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    '''
    @staticmethod
    def convertToLinkedList(current_node: 'Optional[Node]') -> (Node, Node):

        leftmost_node_of_current_tree = current_node
        rightmost_node_of_current_tree = current_node

        if current_node.left:
            leftmost_node_of_left_tree, rightmost_node_from_left_tree = Solution.convertToLinkedList(current_node.left)
            rightmost_node_from_left_tree.right = current_node
            current_node.left = rightmost_node_from_left_tree
            leftmost_node_of_current_tree = leftmost_node_of_left_tree

        # current_node.right already points to correct successor (right node, if exists)

        if current_node.right:
            leftmost_node_from_right_tree, rightmost_node_of_right_tree = Solution.convertToLinkedList(current_node.right)
            leftmost_node_from_right_tree.left = current_node
            current_node.right = leftmost_node_from_right_tree
            rightmost_node_of_current_tree = rightmost_node_of_right_tree

        leftmost_node_of_current_tree.left = rightmost_node_of_current_tree
        rightmost_node_of_current_tree.right = leftmost_node_of_current_tree

        return leftmost_node_of_current_tree, rightmost_node_of_current_tree
    '''


    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        '''
         * instead of recursion, lets iterate tree using a stack.
            - assign left, right values.
            - add root and left nodes to stack (using curr)
            - pop from stack. process node, if right exists, curr=right.
        '''


        if not root:
            return

        first, last, curr = None, None, root.left
        stack = [root]

        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left  # populate stack until we reach leftmost node
                continue
            if stack:
                node = stack.pop()
                if not first:
                    first = node  # first iteration: assign leftmost value to `first`
                if last:
                    last.right = node
                    node.left = last
                    last = node  # all following iterations: just append `node` to tail.
                else:
                    last = node  # first iteration: assign leftmost value to `last`
                if node.right:
                    curr = node.right  # return back to re-populating the stack, before pivoting to upper tree

        last.right = first
        first.left = last
        return first



if __name__ == '__main__':
    root = Node(4, left=Node(2, left=Node(1), right=Node(3)), right=Node(5))
    Solution().treeToDoublyList(root)
    print("root: %s" % root)
