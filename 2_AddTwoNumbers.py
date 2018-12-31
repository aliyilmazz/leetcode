from itertools import combinations

def print_linkedlist(ll):
    result_array = []
    while ll:
        result_array.append(ll.val)
        ll = ll.next
    print(" -> ".join([str(x) for x in result_array]))

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = None
        extra_digit = False
        while (l1 is not None or l2 is not None) or extra_digit is True:
            # print_linkedlist(l1)
            # print_linkedlist(l2)
            digit_sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + extra_digit*1
            # print("l1:%s, l2:%s, ds:%d" % (str(l1.val) if l1 else "nope", str(l2.val) if l2 else "nope", digit_sum))
            extra_digit = False
            digit_sum_copy = digit_sum
            digit_sum %= 10

            if result == None:
                # print("new node first digit: " + str(digit_sum))
                result = ListNode(digit_sum)
            else:
                tail = result
                while tail.next:
                    tail = tail.next
                tail.next = ListNode(digit_sum)

            if digit_sum_copy >= 10:
                extra_digit = True
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        return result







first_number = ListNode(1)
first_number.next = ListNode(8)
# first_number.next.next = ListNode(3)

second_number = ListNode(0)
# second_number.next = ListNode(6)
# second_number.next.next = ListNode(4)

sol = Solution()
third_number = sol.addTwoNumbers(first_number, second_number)
print_linkedlist(third_number)
