package com.mybasepackage.medium.linkedlist;
import com.mybasepackage.helpers.ListNode;

/**
 Definition for singly-linked list.
 *
 **/


public class OddEvenLinkedList {
    public ListNode oddEvenList(ListNode head) {

        if (head == null || head.next == null || head.next.next == null) {
            return head;  // lists with n={1,2} are not processed.
        }

        ListNode tailTraverser = head;
        int nodeCount = 1;
        while (tailTraverser.next != null) {
            nodeCount++;
            tailTraverser = tailTraverser.next;
        }



        ListNode headTraverser = head;


        int iterationCount = 0;
        if (nodeCount % 2 == 1) {
            iterationCount = (nodeCount-1) / 2;
        }
        else {
            iterationCount = nodeCount / 2;
        }
        int iterationCounter = 0;
        while (iterationCounter++ < iterationCount) {
            tailTraverser.next = headTraverser.next;
            headTraverser.next = tailTraverser.next.next;
            tailTraverser = tailTraverser.next;
            tailTraverser.next = null;
            headTraverser = headTraverser.next;
        }

        return head;
    }
    public static void main(String[] args) {
        OddEvenLinkedList oddEvenLinkedListCls = new OddEvenLinkedList();
        ListNode head = new ListNode(
                1, new ListNode(
                        2, new ListNode(
                                3, new ListNode(
                                        4, new ListNode(
                                                5)
        )
        )
        )
        );
        head.printListNode();
        oddEvenLinkedListCls.oddEvenList(head);
        head.printListNode();
    }
}

