# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList_iterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return

        stack = []
        element = head
        while element:
            stack.append(element)
            element = element.next

        new_head = stack.pop()
        traverser = new_head
        while stack:
            traverser.next = stack.pop()
            traverser = traverser.next

        traverser.next = None
        return new_head

    @staticmethod
    def _getNextNode(node):
        '''
        if not node:
            return 

        next_node = Solution._getNextNode(node.next)
        if next_node:
            next_node.next = node

        return next_node
        '''
        if not node or not node.next:
            return node

        else:
            head_node = Solution._getNextNode(node.next)
            node.next.next = node
            node.next = None
            return head_node

    def reverseList(self, head):
        return Solution._getNextNode(head)

    def reverseList_iterative_o1space(self, head):
        ''' o(1) space '''
        new_head = None
        while head:
            temp = head.next  # keep rest of LL
            head.next = new_head  # point to backwards
            new_head = head  # prepare for next loop: set something to point to
            head = temp  # go to next loop
        return new_head



