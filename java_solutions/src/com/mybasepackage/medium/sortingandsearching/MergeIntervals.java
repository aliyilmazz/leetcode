package com.mybasepackage.medium.sortingandsearching;

import java.util.*;

public class MergeIntervals {

    public int[][] merge(int[][] intervals) {

        int[][] mergedIntervals = new int[][]{{}};
        mergedIntervals[0] = intervals[0];

        List<int[]> registeredIntervalList = new ArrayList<>();


        Queue<int[]> intervalInputs = new PriorityQueue<>((a, b) -> (a[0] - b[0]));
        Collections.addAll(intervalInputs, intervals);
        registeredIntervalList.add(intervalInputs.poll());

        while (!intervalInputs.isEmpty()) {
            int[] currentInterval = intervalInputs.poll();

            int[] lastRegisteredInterval = registeredIntervalList.get(registeredIntervalList.size() - 1);

            // since the inputs are sorted w.r.t first elements,
            // we know that currentInterval[0]>=lastRegisteredInterval[0]

            // check if input interval's lower bound...
            if (lastRegisteredInterval[0] <= currentInterval[0] && lastRegisteredInterval[1] >= currentInterval[0]) {
                // [1] ... remains in last interval's range. if current's interval's upper bound...
                if (lastRegisteredInterval[1] >= currentInterval[1]) {
                    // [1A] ... falls into last interval's range
                    //  action: no action.
                } else {
                    // [1B] ... falls outside last interval's range.
                    //  action: extend last interval's range.
                    lastRegisteredInterval[1] = currentInterval[1];
                }
            } else {
                // [2] ... does not remain within last interval's range.
                // action: register it as a separate interval.
                registeredIntervalList.add(currentInterval);
            }
        }

        return registeredIntervalList.toArray(int[][]::new);
    }


    public static void main(String[] args) {
        MergeIntervals cls = new MergeIntervals();
        int[][] intervals = {{1,4}, {4,6}, {5, 9}, {11, 15}, {2, 3}, {2, 4}};
        int[][] mergedIntervals = cls.merge(intervals);
        System.out.println("Merged intervals: " + Arrays.deepToString(mergedIntervals));

        Queue<int[]> intervalQueue = new PriorityQueue<>((a, b) -> (a[0] - b[0]));
        intervalQueue.add(new int[]{100, 150});
        intervalQueue.add(new int[]{8, 10});
        intervalQueue.add(new int[]{10, 60});
        intervalQueue.add(new int[]{1, 6});

        Iterator<int[]> it = intervalQueue.iterator();
        while (it.hasNext()) {
            int[] currentArray = it.next();
            System.out.println("TestQueue: " + Arrays.toString(currentArray));
            System.out.println("Next item is present: " + it.hasNext());
        }

    }
}
