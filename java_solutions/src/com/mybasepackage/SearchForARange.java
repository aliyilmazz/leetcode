package com.mybasepackage;

import java.util.Arrays;
import java.util.HashSet;

public class SearchForARange {

    public int[] searchRange(int[] nums, int target) {
        if (nums.length == 0) return new int[]{-1,-1};
        if (nums[0] > target || nums[nums.length-1] < target) return new int[]{-1,-1};

        HashSet<Integer> visitedIndices = new HashSet<>();

        int stepSize = (nums.length-1)/2;
        if (stepSize < 1) stepSize = 1;
        int index = 0;
        while (true) {
            int currentNumber = nums[index];
            if (currentNumber == target) {
                // number found. action: detect and return range
                int rangeTraverser = index;
                while (rangeTraverser > 0 && nums[rangeTraverser-1] == target) {
                    rangeTraverser--;
                }
                int lowerBound = rangeTraverser;
                rangeTraverser = index;
                while (rangeTraverser < nums.length-1 && nums[rangeTraverser+1] == target) {
                    rangeTraverser++;
                }
                int upperBound = rangeTraverser;
                return new int[]{lowerBound, upperBound};
            }
            else if (currentNumber < target) {
                index+=stepSize;
            }
            else if (currentNumber > target) {
                index-=stepSize;
            }

            if (index < 0 || index > nums.length-1) return new int[]{-1,-1};
            stepSize/=2;
            if (stepSize < 1) stepSize = 1;

            if (visitedIndices.contains(index)) {
                // detect circularity
                return new int[]{-1, -1};
            } else { visitedIndices.add(index); }
        }
    }

    public static void main(String[] args) {
        SearchForARange cls = new SearchForARange();

        int[] nums = {5,7,7,8,8,10};
        int target = 6;
        int[] range = cls.searchRange(nums, target);
        System.out.println("Range: " + Arrays.toString(range));
    }
}
