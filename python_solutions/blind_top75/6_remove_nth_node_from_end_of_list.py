class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        repr = ''
        traverser = self
        while traverser:
            repr += str(traverser.val)
            if traverser.next:
                repr += ' -> '
            traverser = traverser.next
        return repr



class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        ''' 

        5 nodes
        n=2
        len=5


        5-2 = 3rd node from beginning.

        if target=0 return head.next

        start traversing from head, traverse 2 times (n-1 times)
            just jump to next node (traverser = traverser.next)

        now you are at prev node
        record where you are, as prev
        assign prev.next = prev.next.next 

        return head





        first go: determine length, and determine order from beginning (0-indexed)

        '''

        # [1] determine length
        ll_len = 0
        length_traverser = head
        while length_traverser:
            ll_len += 1
            length_traverser = length_traverser.next

        # [2] determine order from front
        to_be_removed_node_order = ll_len - n

        # [3] handle edge case where user wants to remove head
        if to_be_removed_node_order == 0:
            return head.next if head else ListNode()

        # [4] start traversing from head, to reach prev node
        traverse_count = to_be_removed_node_order - 1

        traverser = head
        for _ in range(traverse_count):
            traverser = traverser.next

        prev = traverser

        # [5] apply delete operation
        prev.next = prev.next.next

        # [6] return head
        return head




if __name__ == '__main__':
    ll = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print("Input LL: %s" % ll)
    returned_ll = Solution().removeNthFromEnd(ll, 2)
    print("Output LL: %s" % returned_ll)