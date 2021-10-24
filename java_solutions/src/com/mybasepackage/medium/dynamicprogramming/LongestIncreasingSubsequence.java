package com.mybasepackage.medium.dynamicprogramming;

import java.util.HashMap;
import java.util.HashSet;

public class LongestIncreasingSubsequence {

    int[] nums;
    HashMap<Integer, Integer> solutionMap;
    int LIS = 1;


    public int _lengthOfLIS(int index) {
        if (solutionMap.containsKey(index)) {return solutionMap.get(index);}

        int currentNumber = nums[index];
        int tempIterator = index+1;
        int LIS = 1;
        while (tempIterator < nums.length) {
            if (nums[tempIterator] > currentNumber) {
                LIS = Math.max(LIS, 1 + _lengthOfLIS(tempIterator));
            }
            tempIterator++;
        }

        this.LIS = Math.max(this.LIS, LIS);
        solutionMap.put(index, LIS);
        return LIS;
    }


    public int lengthOfLIS(int[] nums) {
        this.nums = nums;
        solutionMap = new HashMap<>();

        int currentIndex = nums.length-1;
        solutionMap.put(nums.length-1, 1);

        int arrayReverseIterator = nums.length-1;
        while(arrayReverseIterator>=0) {
            _lengthOfLIS(arrayReverseIterator);
            arrayReverseIterator--;
        }
        return this.LIS;
    }

    public static void main(String[] args) {
        LongestIncreasingSubsequence cls = new LongestIncreasingSubsequence();
//        assert cls.lengthOfLIS(new int[]{10,9,2,5,3,7,101,18}) == 4;
//        assert cls.lengthOfLIS(new int[]{0,1,0,3,2,3}) == 4;
//        assert cls.lengthOfLIS(new int[]{7,7,7,7,7,7,7,7}) == 1;
        int[] nums = {0,1,0,3,2,3};
        System.out.println("LIS: " + cls.lengthOfLIS(nums));
//        int[] nums2 = {0};
//        System.out.println("LIS: " + cls.lengthOfLIS(nums2));
    }
}
