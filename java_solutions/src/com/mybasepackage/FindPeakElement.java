package com.mybasepackage;

import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.TreeSet;
import java.util.stream.IntStream;

public class FindPeakElement {

    public int findPeakElement(int[] nums) {
        TreeSet<Integer> peakSet = new TreeSet<>(Collections.reverseOrder());
        HashMap<Integer, Integer> indexMap = new HashMap<>();




//        for (int i=0; i<nums.length; i++) {
//            peakSet.add(nums[i]);
//            indexMap.put(nums[i], i);
//        }


        IntStream.range(0, nums.length).forEach(i -> {
            peakSet.add(nums[i]);
            indexMap.put(nums[i], i);
            }
        );

        return indexMap.get(peakSet.pollFirst());
    }

    public static void main(String[] args) {
        FindPeakElement cls = new FindPeakElement();
        int[] nums = {1,2,3,2,3,1};
        int peakElement = cls.findPeakElement(nums);
        System.out.println("Peak element: " + peakElement);
    }
}
