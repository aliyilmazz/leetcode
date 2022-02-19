# Definition for singly-linked list.
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        stack = []  # we need stack to go backwards (for tail)
        stack_traverser = head

        while stack_traverser:
            stack.append(stack_traverser)
            stack_traverser = stack_traverser.next

        start, tail = head, stack.pop()
        for _ in range((len(stack) // 2) - 1):
            #do adjustment
            '''
            1 -> 2 -> 3 -> 4 -> 5
            1 2 3 4 5
            1 5 2 3 4
            1 5 2 4 3            
            '''

            temp = start.next  # keep rest of list (to tie to tail->next)
            start.next = tail  # make start point to end
            tail.next = temp   # initially tail.next should be None

            start = temp
            tail = stack.pop()
        return


if __name__ == '__main__':
    list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    Solution().reorderList(list)
    print("debug here")