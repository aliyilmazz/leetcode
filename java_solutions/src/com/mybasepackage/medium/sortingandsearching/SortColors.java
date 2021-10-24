package com.mybasepackage.medium.sortingandsearching;

import java.util.Arrays;

class SortColors {
    public void sortColors(int[] nums) {

        int zeroOffset = 0;
        int oneOffset = 0;

        for (int currentIndex=0; currentIndex<nums.length; currentIndex++) {
            int currentNumber = nums[currentIndex];
            if (currentNumber != 2) {
                if (currentNumber == 0) {
                    if (currentIndex > zeroOffset) {
                        nums[currentIndex] = nums[zeroOffset];
                        nums[zeroOffset] = 0;
                        zeroOffset++;
                        oneOffset++;
                        if (nums[currentIndex] == 1) {
                            // zero replacement messed up 1s.
                            // action: replace 1 aswell.
                            nums[currentIndex] = nums[oneOffset - 1];
                            nums[oneOffset - 1] = 1;
                        }
                    }
                    else {
                        zeroOffset++;
                        oneOffset++;
                    }
                }
                else if (currentNumber == 1) {
                    if (currentIndex > oneOffset) {
                        nums[currentIndex] = nums[oneOffset];
                        nums[oneOffset] = 1;
                        oneOffset++;
                    }
                    else {
                        oneOffset++;
                    }
                }
            }
        }
    }


    public static void main(String[] args) {
        SortColors cls = new SortColors();
        int[] nums = new int[]{0,1};
        System.out.println("Unsorted nums: " + Arrays.toString(nums));
        cls.sortColors(nums);
        System.out.println("Sorted nums: " + Arrays.toString(nums));
    }
}
