package com.mybasepackage.medium.sortingandsearching;
import java.util.*;
import java.util.stream.IntStream;


public class KthLargestElement {

    public int findKthLargest(int[] nums, int k) {
        Queue<Integer> largestNums = new PriorityQueue<>(Collections.reverseOrder());
        for (Integer num: nums) {
            largestNums.add(num);
        }
        //Arrays.stream(nums).forEach(largestNums::add);
        IntStream.range(0, k-1).forEach(i->largestNums.poll());
        return largestNums.poll();
    }

    public static void main(String[] args) {
        KthLargestElement cls = new KthLargestElement();
        int[] nums = {3,2,3,1,2,4,5,5,6};
        int kthLargest = cls.findKthLargest(nums, 4);
        System.out.println("Kth largest: " + kthLargest);
    }
}
