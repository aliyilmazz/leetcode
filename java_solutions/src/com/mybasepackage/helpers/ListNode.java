package com.mybasepackage.helpers;

import java.util.ArrayList;
import java.util.List;

public class ListNode {
    public int val;
    public ListNode next;
    public ListNode() {}
    public ListNode(int val) {this.val = val;}
    public ListNode(int val, ListNode next) { this.val=val; this.next=next;}

    public void printListNode() {
        ListNode headTraverser = this;
        List<Integer> valueList = new ArrayList<>();
        while (headTraverser != null) {
            valueList.add(headTraverser.val);
            headTraverser = headTraverser.next;
        }
        System.out.println("LinkedList: " + valueList);
    }
}
