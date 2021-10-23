package com.mybasepackage;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Permutations {


    List<List<Integer>> permutationsList;
    Set<Integer> numSet;

    public Permutations() {
        this.permutationsList = new ArrayList<>();
        numSet = new HashSet<>();
    }


    public void _permute(List<Integer> permutationList, Set<Integer> numSet) {
        if (numSet.isEmpty()) {
            this.permutationsList.add(permutationList);
            return;
        }

        for (Integer num: numSet) {
            Set<Integer> newSet = new HashSet<>(numSet);
            newSet.remove(num);
            List<Integer> newPermutationsList = new ArrayList<>(permutationList);
            newPermutationsList.add(num);
            _permute(newPermutationsList, newSet);
        }
    }

    public List<List<Integer>> permute(int[] nums) {
        for (Integer num: nums) {
            numSet.add(num);
        }
        _permute(new ArrayList<>(), numSet);
        return this.permutationsList;
    }

    public static void main(String[] args) {
        Permutations cls = new Permutations();
        int[] nums = new int[]{1};
        List<List<Integer>> result = cls.permute(nums);

        System.out.println("Permutations start");
        for (List<Integer> integerList: result) {
            System.out.println(integerList);
        }
        System.out.println("Permutations end");
    }
}
