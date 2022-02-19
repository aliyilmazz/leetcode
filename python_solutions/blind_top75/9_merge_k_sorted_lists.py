# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def mergeTwoLists_iterative(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        '''


        timewise o(n+m) iterations
        space complexity o(1). no extra space needed

        '''
        merged_list = ListNode(0)  # dummy head node

        merged_list_head = merged_list

        '''
            two pointers, p_list1 p_list2
            increment, populate merged_list until p_list1 == None nad p_list2 == None
            return merged_list
        '''

        p_list1 = list1
        p_list2 = list2

        while p_list1 or p_list2:
            if not p_list1:
                merged_list.next = p_list2
                merged_list = merged_list.next
                p_list2 = p_list2.next
                continue

            if not p_list2:
                merged_list.next = p_list1
                merged_list = merged_list.next
                p_list1 = p_list1.next
                continue

            if p_list1.val <= p_list2.val:
                merged_list.next = p_list1
                merged_list = merged_list.next
                p_list1 = p_list1.next
            else:
                merged_list.next = p_list2
                merged_list = merged_list.next
                p_list2 = p_list2.next

        return merged_list_head.next  # skip dummy val

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        '''


        recursive
        function call for each member of l1, l2
        time complexity: o(n+m)
        space complexity: o(n+m)

        '''
        if list1 is None and list2 is None:
            return None
        elif list1 is None:
            return list2
        elif list2 is None:
            return list1
        elif list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2







if __name__ == '__main__':
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    merged_list = Solution().mergeTwoLists(list1, list2)
    print("debug here and see merged list")