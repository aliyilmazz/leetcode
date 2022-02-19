# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverseLinkedList(self, head, k):
        new_head = None
        ptr = head
        while k:
            next_node = ptr.next

            ptr.next = new_head
            new_head = ptr

            ptr = next_node
            k -= 1

        return new_head

    def reverseKGroup_recursive(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0
        ptr = head

        # first see if there are atleast k nodes left
        while count < k and ptr:
            ptr = ptr.next
            count += 1

        if count != k:
            return head

        # if count == k, we need sorting to do
        reversedHead = self.reverseLinkedList(head, k)
        head.next = self.reverseKGroup_recursive(ptr, k)

        return reversedHead

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ptr = head
        ktail = None

        new_head = None

        while ptr:
            count = 0
            ptr = head

            while count < k and ptr:
                ptr = ptr.next
                count += 1

            if count < k:
                break

            reversed_head = self.reverseLinkedList(head, k)
            if not new_head:
                new_head = reversed_head

            if ktail:
                ktail.next = reversed_head

            ktail = head
            head = ptr

        if ktail:
            ktail.next = head

        return new_head if new_head else head


