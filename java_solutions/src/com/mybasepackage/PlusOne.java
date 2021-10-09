package com.mybasepackage;

import java.util.ArrayList;
import java.util.Arrays;

public class PlusOne {

    public int[] plusOne(int[] digits) {
        //int lastDigit = digits[digits.length-1];
        return new int[]{};
    }


    public static void main(String[] args) {
        int[] nums = Arrays.asList(9,8,7,6,5,4,3,2,1,0).stream().mapToInt(i -> i).toArray();
        PlusOne plusOneCls = new PlusOne();
        System.out.println(String.format("Input array: %s", Arrays.toString(nums)));
        int[] plusOneArr = plusOneCls.plusOne(nums);
        System.out.println(String.format("Resulted Array: %s", Arrays.toString(plusOneArr)));
    }
}
