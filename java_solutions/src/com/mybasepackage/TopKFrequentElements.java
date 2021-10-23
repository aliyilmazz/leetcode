package com.mybasepackage;

import java.util.*;
import java.util.stream.IntStream;


class FixedSizePriorityQueue<E> extends TreeSet<E> {
    final int _capacity;

    public FixedSizePriorityQueue(final int capacity) {
        this._capacity = capacity;
    }

    public FixedSizePriorityQueue(final int capacity, final Comparator<? super E> comparator) {
        super(comparator);
        this._capacity = capacity;
    }

    @Override
    public boolean add(final E e) {
        if (this._capacity <= 0) { return false; }

        if (size() < this._capacity) { super.add(e); }
        else {
            if (comparator() != null && comparator().compare(this.last(), e) < 0) {
                pollLast();
                return super.add(e);
            }
        }
        return false;
    }
}


public class TopKFrequentElements {

    Map<Integer, Integer> occurrencesMap;
    Map<Integer, Integer> leadingOccurrencesMap;
    Integer lowestKey;
    Integer lowestValue;
    Integer leaderboardElementCount;

    public TopKFrequentElements() {
        occurrencesMap = new HashMap<>();
        leadingOccurrencesMap = new HashMap<>();
        leaderboardElementCount = 0;

    }

    public int[] _topKFrequent(int[] nums, int k) {

        for (Integer num: nums) {
            int newOccurance = occurrencesMap.getOrDefault(num, 0)+1;
            occurrencesMap.put(num, newOccurance);

            if (leadingOccurrencesMap.containsKey(num)) {
                // if the number is already in leaderboard, increment the occurrence
                leadingOccurrencesMap.put(num, newOccurance);
                if (leaderboardElementCount == k && lowestValue.equals(newOccurance-1)) {
                    if (num.equals(lowestKey)) {
                        replaceLowestKey: {
                            for (Map.Entry<Integer, Integer> entry: leadingOccurrencesMap.entrySet()) {
                                if (entry.getValue().equals(lowestValue)) {
                                    lowestKey = entry.getKey();
                                    break replaceLowestKey;
                                }
                            }
                            // if you can't find any lower key
                            // [1] leave lowestKey assignments as is
                            // [2] assign lowestValue as newOccurrence
                            lowestValue = newOccurance;
                        }
                    }
                }
            }
            else {
                // if number is not in leaderboard, check if it's worthy

                if (leaderboardElementCount < k) {
                    // [Phase A] if there's not enough numbers in leaderboard, then just put it.
                    leadingOccurrencesMap.put(num, newOccurance);
                    leaderboardElementCount++;
                    if (leaderboardElementCount == k) {
                        // [Phase A1] now board is filled fully with K elements.
                        // action: iterate list, determine lowestKey and lowestValue for [Phase B].
                        this.lowestValue = Integer.MAX_VALUE;
                        for (Map.Entry<Integer, Integer> entry: leadingOccurrencesMap.entrySet()) {
                            if (entry.getValue() < lowestValue) {
                                lowestValue = entry.getValue();
                                lowestKey = entry.getKey();
                            }
                        }
                    }
                }
                else {
                    // [Phase B] if it's filled, check the lowestValue and see if a replacement is needed.
                    if (newOccurance > lowestValue) {
                        leadingOccurrencesMap.put(num, newOccurance);
                        leadingOccurrencesMap.remove(lowestKey);
                        findSameLowest: {
                            for (Map.Entry<Integer, Integer> entry: leadingOccurrencesMap.entrySet()) {
                                if (entry.getValue() < newOccurance) {
                                    lowestValue = entry.getValue();
                                    lowestKey = entry.getKey();
                                    break findSameLowest;
                                }
                            }
                            lowestValue = newOccurance;
                            lowestKey = num;
                        }
                    }
                }
            }
        }
        return leadingOccurrencesMap.keySet().stream().mapToInt(i->i).toArray();
    }

    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> occurrencesMap = new HashMap<>();
        for (Integer num: nums) {
            occurrencesMap.put(num, occurrencesMap.getOrDefault(num,0)+1);
        }

        Queue<Integer> occurrenceListings = new PriorityQueue<>((num1, num2) -> (occurrencesMap.get(num2) - occurrencesMap.get(num1)));
        occurrencesMap.forEach((_k,_v) -> occurrenceListings.add(_k));

        List<Integer> topOccurrences = new ArrayList<>();
        IntStream.range(0, k).forEach(i->topOccurrences.add(occurrenceListings.poll()));

        return topOccurrences.stream().mapToInt(i->i).toArray();
    }

    public static void main(String[] args) {
//        TopKFrequentElements cls = new TopKFrequentElements();
//        int[] nums = {1,2};
//        int k = 2;
//        int[] outputNums = cls.topKFrequent(nums, k);
//        System.out.println("Output is: " + Arrays.toString(outputNums));



//        HashMap<Integer, Integer> occurrenceMap = new HashMap<>();
//        occurrenceMap.put(1, 55);
//        occurrenceMap.put(2, 10);
//        occurrenceMap.put(3, 15);
//        occurrenceMap.put(4, 20);
//        occurrenceMap.put(5, 25);
//        occurrenceMap.put(6, 44);
//        occurrenceMap.put(7, 77);
//        occurrenceMap.put(8, 75);
//        occurrenceMap.put(9, 110);

//        TreeSet<Integer> testTreeSet = new TreeSet<>((n1,n2) -> (occurrenceMap.get(n2)-occurrenceMap.get(n1)));
//
//        occurrenceMap.forEach((k,v) -> testTreeSet.add(k));
//        System.out.println("test treeset: " + testTreeSet.first());
//
//        List<Integer> returnedList = new ArrayList<>();
//        IntStream.range(0, 3).forEach(i -> returnedList.add(testTreeSet.pollFirst()));
//        System.out.println("returned list: " + returnedList.toString());


//        Queue<Integer> occurrencePriorityQueue = new PriorityQueue<>(
//                (n1, n2) -> occurrenceMap.get(n2) - occurrenceMap.get(n1)
//        );
//
//        for (Map.Entry<Integer, Integer> entry: occurrenceMap.entrySet()) {
//            occurrencePriorityQueue.add(entry.getKey());
//        }


//        FixedSizePriorityQueue<Integer> _fixedSizePQ = new FixedSizePriorityQueue<>(3, Collections.reverseOrder());
//        occurrenceMap.forEach((k,v) -> _fixedSizePQ.add(k));
//        System.out.println("PriorityQueue members: " + Arrays.toString(_fixedSizePQ.toArray()));

    }
}

