# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle_withset(self, head: Optional[ListNode]) -> bool:

        ''' 



        '''

        traverser = head
        visited = set()

        while traverser:
            if traverser in visited:
                return True
            visited.add(traverser)
            traverser = traverser.next

        return False

    def hasCycle(self, head):

        slow = head
        fast = head.next

        while slow != fast:

            if not slow or not fast:
                return False


            slow = slow.next
            fast = fast.next.next

        return True


if __name__ == '__main__':
    node = ListNode(-1)
    output = Solution().hasCycle(node)
    print("output: %s" % output)