"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList_iterative(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        new_head = new_head_traverser = Node(0, None, None)  # dummy node
        head_traverser = head
        node_map = dict()
        while head_traverser:
            new_node = Node(head_traverser.val, None, None)
            new_head_traverser.next = new_node
            new_head_traverser = new_node
            node_map[head_traverser] = new_node
            head_traverser = head_traverser.next

        new_head_traverser = new_head.next  # skip dummy node
        head_traverser = head
        while head_traverser:
            new_head_traverser.random = node_map[head_traverser.random] if head_traverser.random else None
            new_head_traverser = new_head_traverser.next
            head_traverser = head_traverser.next

        return new_head.next








