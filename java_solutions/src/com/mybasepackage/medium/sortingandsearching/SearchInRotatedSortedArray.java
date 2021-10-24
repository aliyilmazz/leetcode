package com.mybasepackage.medium.sortingandsearching;

import java.util.HashSet;

public class SearchInRotatedSortedArray {

    public int applyBinarySearchInSortedArray(int target, int[] nums, int startIndex, int endIndex) {
        HashSet<Integer> visitedIndices = new HashSet<>();

        int startIndexTraverser = startIndex;
        int endIndexTraverser = endIndex;

        int middleIndex;

        while (startIndexTraverser <= endIndexTraverser) {

            if (endIndexTraverser-startIndexTraverser<=1) {
                // terminating condition: array is small enough to manually look up
                if (nums[startIndexTraverser] == target) return startIndexTraverser;
                if (nums[endIndexTraverser] == target) return endIndexTraverser;
                else return -1;
            }

            middleIndex = (startIndexTraverser+endIndexTraverser) / 2;
            if (nums[middleIndex] == target) return middleIndex;

            else if (nums[middleIndex] > target) {
                endIndexTraverser = middleIndex;
            }
            else if (nums[middleIndex] < target) {
                startIndexTraverser = middleIndex;
            }
        }
        return -1;
    }

    public int search(int[] nums, int target) {
        if (nums.length == 0) return -1;

        int firstIndex = 0;
        int lastIndex = nums.length-1;
        int middleIndex;

        while (true) {
            if (lastIndex == firstIndex) {
                if (nums[firstIndex] == target) return firstIndex;
                else return -1;
            }
            if (lastIndex - firstIndex == 1) {
                if (nums[firstIndex] == target) return firstIndex;
                else if (nums[lastIndex] == target) return lastIndex;
                else return -1;
            }

            // keeping breaking down interval into a smaller interval.
            if (nums[firstIndex] > nums[lastIndex]) {
                // our array is unsorted. our number might be in between.
                // divide array into two pieces.
                middleIndex = (firstIndex + lastIndex) / 2 ;
                if (nums[middleIndex] < nums[lastIndex]) {
                    // rightside is properly sorted. then left side is rotated.

                    // check sorted interval
                    if (nums[middleIndex] <= target && target <= nums[lastIndex]) {
                        // target lies inside sorted array. apply binary search
                        return applyBinarySearchInSortedArray(target, nums, middleIndex, lastIndex);
                    }
                    else {
                        // target may or may not lie in rotated left part. examine left part in next iteration
                        lastIndex = middleIndex;
                    }
                }
                else {
                    // leftside is properly sorted. (logically if array is unsorted, one half is sorted)
                    if (nums[firstIndex] <= target && target <= nums[middleIndex]) {
                        return applyBinarySearchInSortedArray(target, nums, firstIndex, middleIndex);
                    }
                    else {
                        // target may or may not lie in rotated right part. examine left part in next iteration
                        firstIndex = middleIndex;
                    }
                }
            }
            else {
                // array is sorted. apply binary search.
                return applyBinarySearchInSortedArray(target, nums, firstIndex, lastIndex);
            }
        }
    }

    public static void main(String[] args) {
        SearchInRotatedSortedArray cls = new SearchInRotatedSortedArray();
        int[] rotatedSortedArray = {3,5,1};
        int target = 3;
        int indexOfTarget = cls.search(rotatedSortedArray, target);
        System.out.println("Index of target: " + indexOfTarget);
    }
}
