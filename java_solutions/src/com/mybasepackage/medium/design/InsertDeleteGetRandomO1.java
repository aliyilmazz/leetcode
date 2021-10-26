package com.mybasepackage.medium.design;


import java.util.*;

class RandomizedSet {

    //HashSet<Integer> integerSet;
    List<Integer> integerList;
    HashMap<Integer, Integer> integerToIndexMap;

    public RandomizedSet() {
        integerList = new ArrayList<>();
        integerToIndexMap = new HashMap<>();
    }

    public boolean insert(int val) {
        // O(1)

        if (integerToIndexMap.containsKey(val)) {
            return false;
        }

        integerList.add(val);
        int integerIndex = integerList.size()-1;
        integerToIndexMap.put(val, integerIndex);
        return true;
    }

    public boolean remove(int val) {
        // O(1)
        if (!integerToIndexMap.containsKey(val)) return false;

        if (integerToIndexMap.get(val) == integerList.size()-1) {
            integerList.remove(integerList.size()-1);
            integerToIndexMap.remove(val);
            return true;
        }

        // re-locate last element to emptied space
        int oldIndex = integerToIndexMap.get(val); // learn old index
        int newValueInOldIndex = integerList.get(integerList.size()-1);  // identify new_value in old index
        integerList.set(oldIndex, newValueInOldIndex);  // move new_value into old index
        integerList.remove(integerList.size()-1); // remove new_value from last index, since we moved it to old_index
        integerToIndexMap.remove(val);  // remove deleted element's index info
        integerToIndexMap.put(newValueInOldIndex, oldIndex);  // update new_value's index info

        return true;
    }

    public int getRandom() {
        // O(1)
        int index = new Random().nextInt(integerList.size());
        return integerList.get(index);
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */


public class InsertDeleteGetRandomO1 {

    public static void main(String[] args) {
        RandomizedSet randomizedSet = new RandomizedSet();
        System.out.println(randomizedSet.insert(1)); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
        System.out.println(randomizedSet.remove(2)); // Returns false as 2 does not exist in the set.
        System.out.println(randomizedSet.insert(2)); // Inserts 2 to the set, returns true. Set now contains [1,2].
        System.out.println(randomizedSet.getRandom()); // getRandom() should return either 1 or 2 randomly.
        System.out.println(randomizedSet.remove(1)); // Removes 1 from the set, returns true. Set now contains [2].
        System.out.println(randomizedSet.insert(2)); // 2 was already in the set, so return false.
        System.out.println(randomizedSet.getRandom()); // Since 2 is the only number in the set, getRandom() will always return 2.
    }

}