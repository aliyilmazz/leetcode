package com.mybasepackage;

import java.util.Arrays;

public class RotateArray {

    public void rotateArray(int[] nums, int k) {
        // todo

        if (nums.length == 0 || nums.length == 1) {
            return;
        }

        if (k>=nums.length) {
            k %= nums.length;
        }

        int rightShifterIndex = nums.length - (k+1);

        int[] tempArrayForLeftShift = new int[k];
        int tempLeftShiftFillerIndex = rightShifterIndex+1;
        int tempLeftShiftFilterCounter = 0;
        while (tempLeftShiftFilterCounter<k) {
            tempArrayForLeftShift[tempLeftShiftFilterCounter] = nums[tempLeftShiftFillerIndex];
            tempLeftShiftFillerIndex++;
            tempLeftShiftFilterCounter++;
        }
        int rightShiftedNumber = nums[rightShifterIndex];

        int tempRightShifterIndex = rightShifterIndex;
        while (tempRightShifterIndex>=0) {
            nums[tempRightShifterIndex+k] = nums[tempRightShifterIndex];
            tempRightShifterIndex--;
        }

        int tempLeftShifterIndex = 0;
        while (tempLeftShifterIndex<k) {
            nums[tempLeftShifterIndex] = tempArrayForLeftShift[tempLeftShifterIndex];
            tempLeftShifterIndex++;
        }
    }

    public static void main(String[] args) {
        int[] nums = new int[]{1,2,3,4,5,6,7};
        int k = 3;
        RotateArrayO1Space rotateArrayCls = new RotateArrayO1Space();
        System.out.println(String.format("Nums before rotation: %s, Rotating by k:%s", Arrays.toString(nums), k));
        rotateArrayCls.rotateArray(nums, k);
        System.out.println(String.format("Nums after rotation: %s", Arrays.toString(nums)));
    }
}
