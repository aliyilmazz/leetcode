package com.mybasepackage.medium.arrayandstrings;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class MissingRanges {

    List<String> missingRanges;

    public MissingRanges() {
        this.missingRanges = new ArrayList<>();
    }

    public void registerInterval(int lowerBound, int upperBound) {
        String intervalRepresentation;
        if (lowerBound == upperBound) {
            intervalRepresentation = Integer.toString(lowerBound);
        }
        else {
            intervalRepresentation = String.format("%s->%s", lowerBound, upperBound);
        }
        this.missingRanges.add(intervalRepresentation);
    }


    public void identifyMissingRanges(int[] nums, int lower, int upper) {
        if (nums.length == 0) { registerInterval(lower, upper); return; }

        if (nums[0] > lower) {
            registerInterval(lower, nums[0]-1);
        }

        for (int i=0; i<nums.length-1; i++) { // this loop wont work for single-element lists.
            if (nums[i]+1 != nums[i+1]) {
                // there is an incontinuity. lets generate missing interval
                registerInterval(nums[i]+1, nums[i+1]-1);
            }
        }

        if (upper > nums[nums.length-1]) {
            registerInterval(nums[nums.length-1]+1, upper);
        }

    }


    public List<String> findMissingRanges(int[] nums, int lower, int upper) {
        this.identifyMissingRanges(nums, lower, upper);
        return this.missingRanges;
    }


//    public List<String> findMissingRanges(int[] nums, int lower, int upper) {
//
//        HashSet<Integer> registeredNums = new HashSet<>();
//        for (int num: nums) {
//            registeredNums.add(num);
//        }
//
//
//        int lowerBound = 0, upperBound = 0;
//        boolean lowerBoundSet = false;
//
//
//
//        for (int i=lower; i<=upper; i++) {
//
//
//            if (registeredNums.contains(i)) {
//                if (lowerBoundSet) {
//                    // number is present in list, AND lower bound set.
//                    // action: terminate interval
//                    registerInterval(lowerBound, upperBound);
//                    lowerBoundSet = false;
//                }
//                else {
//                    // number is present in list, AND lower bound NOT set,
//                    // action: no action. just continue iterating.
//                    continue;
//                }
//            }
//            else {
//                // number is NOT present in list...
//                if (lowerBoundSet) {
//                    // ... AND lower bound set.
//                    // action: increase upperbound.
//                    upperBound++;
//                }
//                else {
//                    // ... AND lower bound NOT set
//                    // action: SET lower bound, start interval
//                    lowerBound = i;
//                    upperBound = i;
//                    lowerBoundSet = true;
//                }
//            }
//        }
//
//        if (lowerBoundSet) {
//            registerInterval(lowerBound, upper);
//        }
//        return this.missingRanges;
//    }


    public static void main(String[] args) {
        MissingRanges missingRangesCls = new MissingRanges();
        int[] nums = new int[]{0, 1, 3, 50, 75};
        int lowerRangeBound = 0;
        int upperRangeBound = 99;
        System.out.println("Nums: " + Arrays.toString(nums) + " Range: " + String.format("[%s,%s]", lowerRangeBound, upperRangeBound));
        List<String> missingRanges = missingRangesCls.findMissingRanges(nums, lowerRangeBound, upperRangeBound);
        System.out.println("Missing Ranges: " + missingRanges.toString());
    }
}
