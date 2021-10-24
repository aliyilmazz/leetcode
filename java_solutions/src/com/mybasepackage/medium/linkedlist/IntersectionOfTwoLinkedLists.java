package com.mybasepackage.medium.linkedlist;
import com.mybasepackage.helpers.ListNode;


public class IntersectionOfTwoLinkedLists {

    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        //boundary check
        if(headA == null || headB == null) return null;

        ListNode a = headA;
        ListNode b = headB;

        //if a & b have different len, then we will stop the loop after second iteration
        while( a != b){
            //for the end of first iteration, we just reset the pointer to the head of another linkedlist
            a = a == null? headB : a.next;
            b = b == null? headA : b.next;
        }

        return a;
    }

    public static void main(String[] args) {
        IntersectionOfTwoLinkedLists cls = new IntersectionOfTwoLinkedLists();
        ListNode iNode = new ListNode(1, new ListNode(8));
        ListNode listA = new ListNode(13, new ListNode(11, new ListNode(19, new ListNode(2, new ListNode(9, iNode)))));
        ListNode listB = new ListNode(30, new ListNode(4, new ListNode(3, iNode)));
        ListNode intersectionNode = cls.getIntersectionNode(listA, listB);
        if (intersectionNode == null) {
            System.out.println("Intersection node IS NULL!");
        } else {
            System.out.println("Intersection node val: " + intersectionNode.val);
        }
    }
}
