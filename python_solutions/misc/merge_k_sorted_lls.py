from typing import List, Optional
from ..utils.ListNode import ListNode


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """

        iterate each one, get int list out of them
        merge int lists
        sort int list
        create new linkedlist out of this intlist


        """
        int_list = []
        for _ll in lists:
            ll = _ll
            while ll:
                print("adding val: %s" % ll.val)
                int_list.append(ll.val)
                ll = ll.next

        if len(int_list) == 0:
            return None

        print("intlist:%s" % int_list)
        int_list.sort()
        print("intlist:%s" % int_list)

        new_ll = ListNode(int_list[0])
        head = new_ll
        int_list_traverser = 1
        while int_list_traverser < len(int_list):
            new_ll.next = ListNode(int_list[int_list_traverser])
            int_list_traverser += 1
            new_ll = new_ll.next
        return head
