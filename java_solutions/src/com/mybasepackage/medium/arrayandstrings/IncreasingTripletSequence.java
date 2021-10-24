package com.mybasepackage.medium.arrayandstrings;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;




class HashMapWithDefaultList extends HashMap<Integer, List<Integer> > {
    public void putValue(Integer key, Integer val) {
        if (containsKey(key)) {
            super.get(key).add(val);
        }
        else {
            super.put(key, new ArrayList<>(List.of(val)));
        }
    }
}

public class IncreasingTripletSequence {


    public boolean increasingTriplet(int[] nums) {

       HashMapWithDefaultList numberSet = new HashMapWithDefaultList();

       for (int i=0; i<nums.length; i++) {
           numberSet.putValue(nums[i], i);
       }

       if (numberSet.keySet().size() < 3) return false;

        for (int i=0; i<nums.length; i++) {
            for (int j=i+1; j<nums.length; j++) {
                if (nums[i] >= nums[j]) continue;
                for (int k=j+1; k<nums.length; k++) {
                    if (nums[k] > nums[j]) return true;
                }
            }
        }
        return false;
    }

    public static void main(String[] args) {}
}
