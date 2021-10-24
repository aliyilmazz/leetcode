package com.mybasepackage.medium.arrayandstrings;

import java.util.Arrays;

public class RotateArrayO1Space {

    public void rotateArray(int[] nums, int k) {
        // todo

        if (nums.length == 0 || nums.length == 1) {
            return;
        }

        if (k>=nums.length) {
            k = k% nums.length;
        }

        int rightShifterIndex = nums.length - (k+1);

        while (rightShifterIndex>=0) {
            //System.out.println(String.format("RightShifter Iteration Started. Current Index: %s", rightShifterIndex));
            int rightShiftedNumber = nums[rightShifterIndex];
            int tempLeftShifter = 0;
            int tempLeftBufferIndex = rightShifterIndex;
            while (tempLeftShifter<k) {
                nums[tempLeftBufferIndex] = nums[tempLeftBufferIndex+1];
                tempLeftBufferIndex++;
                tempLeftShifter++;
            }
            nums[tempLeftBufferIndex] = rightShiftedNumber;
            rightShifterIndex--;
        }
    }

    public static void main(String[] args) {
        int[] nums = new int[]{1,2};
        int k = 3;
        RotateArrayO1Space rotateArrayCls = new RotateArrayO1Space();
        System.out.println(String.format("Nums before rotation: %s, Rotating by k:%s", Arrays.toString(nums), k));
        rotateArrayCls.rotateArray(nums, k);
        System.out.println(String.format("Nums after rotation: %s", Arrays.toString(nums)));
    }
}
