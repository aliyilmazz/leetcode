package com.mybasepackage.medium.backtracking;

import java.util.*;
import java.util.stream.Collectors;

public class Subsets {



    List<List<Integer>> subsetOutput;

    public Subsets() {
        this.subsetOutput = new ArrayList<>();
    }


    public void _registerSubset(List<Integer> currentSubset, List<Integer> superSet) {
        this.subsetOutput.add(currentSubset);

        for (int i=0; i<superSet.size(); i++) {
            int newInteger = superSet.get(i);
            List<Integer> supersetClone = new ArrayList<>(superSet.subList(i+1, superSet.size()));
            List<Integer> newSubsetList = new ArrayList<>(currentSubset);
            newSubsetList.add(newInteger);
            _registerSubset(newSubsetList, supersetClone);
        }

    }

    public List<List<Integer>> subsets(int[] nums) {
        List<Integer> superSet = Arrays.stream(nums).boxed().collect(Collectors.toList());
        _registerSubset(new ArrayList<>(), superSet);
        return this.subsetOutput;
    }

    public static void main(String[] args) {
        Subsets cls = new Subsets();
        int[] nums = new int[]{1,2,3};
        List<List<Integer>> output = cls.subsets(nums);
        System.out.println("Subsets start");
        for (List<Integer> o: output) {
            System.out.println(o.toString());
        }
        System.out.println("Subsets end");
    }
}
