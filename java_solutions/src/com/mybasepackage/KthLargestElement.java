package com.mybasepackage;


import java.util.*;

class FixedSizePQ<E> extends TreeSet<E> {
    final int _capacity;

    public FixedSizePQ(final int capacity) {
        this._capacity = capacity;
    }

    public FixedSizePQ(final int capacity, final Comparator<? super E> comparator) {
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



public class KthLargestElement {

    public int findKthLargest(int[] nums, int k) {
        FixedSizePQ<Integer> mostFrequentNums = new FixedSizePQ<>(k, Collections.reverseOrder());
        for (Integer num: nums) {
            mostFrequentNums.add(num);
        }
        //Arrays.stream(nums).forEach(mostFrequentNums::add);

        return mostFrequentNums.first();
    }

    public static void main(String[] args) {
        KthLargestElement cls = new KthLargestElement();
        int[] nums = {3,2,3,1,2,4,5,5,6};
        int kthLargest = cls.findKthLargest(nums, 4);
        System.out.println("Kth largest: " + kthLargest);
    }
}
