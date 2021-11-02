from typing import Optional, List

class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """

        iterate each one, get int list out of them
        merge int lists
        sort int list
        create new linkedlist out of this intlist


        """

        if lists == []:
            return None

        runner_list = {}

        head_runner = ListNode(2 ** 32)
        smallest_index = -1

        head_runner_overridden = False
        for _index, _list in enumerate(lists):
            if not _list:
                continue
            runner_list[_index] = _list
            if head_runner.val > _list.val:
                head_runner = _list
                smallest_index = _index
                head_runner_overridden = True

        if not head_runner_overridden:
            return None

        head = head_runner
        runner_list[smallest_index] = head_runner.next

        while any(runner_list.values()):  # until they all reach None
            to_be_deleted_runner_indices = []
            next_node = None
            available_min_value_for_next_node = 2 ** 32
            next_node_runner_index = -1
            for k, v in runner_list.items():
                if not v:  # this runner reached end of itself
                    # to_be_deleted_runner_indices.append(k)
                    continue

                if v.val < available_min_value_for_next_node:
                    available_min_value_for_next_node = v.val
                    next_node = v
                    next_node_runner_index = k

            if next_node:
                #print("new minimum found. adding. curval:%s, minval:%s" % (head_runner.val, next_node.val))
                head_runner.next = next_node
                runner_list[next_node_runner_index] = next_node.next
                head_runner = head_runner.next

            # for k in to_be_deleted_runner_indices:
            #     del runner_list[k]

        return head



if __name__ == '__main__':
    lists = [
        ListNode(1, ListNode(4, ListNode(5))),
        ListNode(1, ListNode(3, ListNode(4))),
        ListNode(2, ListNode(6))
    ]
    head_runner = Solution().mergeKLists(lists)
    while head_runner:
        print("%s ->" % head_runner.val)
        head_runner = head_runner.next












