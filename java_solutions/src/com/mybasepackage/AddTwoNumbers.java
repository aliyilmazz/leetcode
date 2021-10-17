package com.mybasepackage;

import java.util.ArrayList;
import java.util.Arrays;
import com.mybasepackage.helpers.ListNode;

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */


class AddTwoNumbers {


    public long deserialize(ListNode listNode) {
        // todo
        long sum = 0;
        long multiplier = 1;
        int base = 10;
        ListNode traverserNode = listNode;
        while (traverserNode != null) {
            sum += multiplier * traverserNode.val;
            traverserNode = traverserNode.next;
            multiplier *= base;
        }

        return sum;
    }

    /*
    public long findBiggestMultiplier(long number) {
        long biggestMultiplier = 1;
        while (biggestMultiplier*10 <= number) {
            biggestMultiplier *= 10;
        }
        return biggestMultiplier;
    }

    public int[] convertSumToSumDigits(long sum) {
        long biggestMultiplier = findBiggestMultiplier(sum);
        long sumTraverser = sum;
        ArrayList<Integer> digitList = new ArrayList<>();
        long multiplier = biggestMultiplier;
        while (true) {
            int newDigit = (int)((float)sumTraverser/(float)multiplier);
            if (newDigit==10) newDigit=9;
            sumTraverser -= newDigit * multiplier;
            digitList.add(newDigit);
            if (multiplier == 1) break;
            else multiplier /= 10;
        }
        return digitList.stream().mapToInt(i -> i).toArray();
    }

    public ListNode convertListToLL(int[] sumDigits) {
        int traverserIndex = sumDigits.length - 1;
        ListNode sumLL = new ListNode(sumDigits[traverserIndex--]);  // head of linked list
        ListNode traverserSumLL = sumLL;
        while (traverserIndex>=0) {
            traverserSumLL.next = new ListNode(sumDigits[traverserIndex--]);
            traverserSumLL = traverserSumLL.next;
            if (traverserIndex<0) break;
        }
        return sumLL;
    }

    public ListNode serialize(long sum) {
        int[] sumDigits = convertSumToSumDigits(sum);
        ListNode sumLL = convertListToLL(sumDigits);
        return sumLL;
    }
    */

    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode firstNumberRunner = l1;
        ListNode secondNumberRunner = l2;
        int sumVal = firstNumberRunner.val + secondNumberRunner.val;
        boolean remainderExists = false;
        if (sumVal>=10) {
            sumVal-=10;
            remainderExists = true;
        }
        ListNode sumLL = new ListNode(sumVal);
        ListNode traverserLL = sumLL;
        firstNumberRunner = firstNumberRunner.next;
        secondNumberRunner = secondNumberRunner.next;
        while (firstNumberRunner != null || secondNumberRunner != null || remainderExists) {
            sumVal = (remainderExists?1:0) +
                    ((firstNumberRunner!=null)? firstNumberRunner.val : 0) +
                    ((secondNumberRunner!=null)? secondNumberRunner.val : 0);
            if (sumVal>=10) {
                sumVal -= 10;
                remainderExists = true;
            }
            else {
                remainderExists = false;
            }
            traverserLL.next = new ListNode(sumVal);
            firstNumberRunner = (firstNumberRunner!=null)?firstNumberRunner.next:null;
            secondNumberRunner = (secondNumberRunner!=null)?secondNumberRunner.next:null;
            traverserLL = traverserLL.next;
        }
        return sumLL;
    }


    public ListNode convertInputToLL(int[] numDigits) {
        if (numDigits.length == 0) return new ListNode(0);
        // todo
        int traverserIndex = 0;
        ListNode newLL = new ListNode(numDigits[traverserIndex++]);
        ListNode traverserLL = newLL;
        while (traverserIndex < numDigits.length) {
            traverserLL.next = new ListNode(numDigits[traverserIndex++]);
            traverserLL = traverserLL.next;
        }
        return newLL;
    }

    public static void main(String[] args) {
        AddTwoNumbers addTwoNumbersCls = new AddTwoNumbers();
        int[] num1 = new int[]{9,9,9,9,9,9,9,9,9,9};
        int[] num2 = new int[]{0};
        ListNode inputNumberOne = addTwoNumbersCls.convertInputToLL(num1);
        ListNode inputNumberTwo = addTwoNumbersCls.convertInputToLL(num2);
        System.out.printf("Numbers are: %s %s%n", addTwoNumbersCls.deserialize(inputNumberOne), addTwoNumbersCls.deserialize(inputNumberTwo));
        ListNode sumLL = addTwoNumbersCls.addTwoNumbers(inputNumberOne, inputNumberTwo);
        System.out.printf("New number is: %s%n", addTwoNumbersCls.deserialize(sumLL));
    }
}