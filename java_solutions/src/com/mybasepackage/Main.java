package com.mybasepackage;

import java.util.Arrays;

public class Main {

    public static int removeDuplicates(int[] nums) {
        if (nums.length == 0) return 0;

        int i = 0;
        for (int j=1; j<nums.length; j++) {
            if (nums[j] != nums[i]) {
                i++;
                nums[i] = nums[j];
            }
        }
        return i+1;
    }


    public static void main(String[] args) {
	// write your code here
        int[] nums = new int[]{1, 1, 2};
        System.out.println(String.format("Nums before execution: %s", Arrays.toString(nums)));
        int k = removeDuplicates(nums);
        System.out.println(String.format("Nums after execution: %s", Arrays.toString(nums)));
    }
}