package com.mybasepackage.easy;

import java.util.ArrayList;
import java.util.Arrays;

public class Intersect {

    public void sort(int arr[])
    {
        int n = arr.length;

        // Build heap (rearrange array)
        for (int i = n / 2 - 1; i >= 0; i--)
            heapify(arr, n, i);

        // One by one extract an element from heap
        for (int i = n - 1; i > 0; i--) {
            // Move current root to end
            int temp = arr[0];
            arr[0] = arr[i];
            arr[i] = temp;

            // call max heapify on the reduced heap
            heapify(arr, i, 0);
        }
    }

    // To heapify a subtree rooted with node i which is
    // an index in arr[]. n is size of heap
    void heapify(int arr[], int n, int i)
    {
        int largest = i; // Initialize largest as root
        int l = 2 * i + 1; // left = 2*i + 1
        int r = 2 * i + 2; // right = 2*i + 2

        // If left child is larger than root
        if (l < n && arr[l] > arr[largest])
            largest = l;

        // If right child is larger than largest so far
        if (r < n && arr[r] > arr[largest])
            largest = r;

        // If largest is not root
        if (largest != i) {
            int swap = arr[i];
            arr[i] = arr[largest];
            arr[largest] = swap;

            // Recursively heapify the affected sub-tree
            heapify(arr, n, largest);
        }
    }

    public int[] findIntersects(int[] shortArray, int[] longArray) {

        int slowRunnerIndex = 0;
        int currentFastNumber = 0;

        ArrayList<Integer> intersect = new ArrayList<>();
        for (int fastRunnerIndex = 0; fastRunnerIndex < longArray.length; fastRunnerIndex++)
        {
            currentFastNumber = longArray[fastRunnerIndex];

            if (currentFastNumber>shortArray[slowRunnerIndex]) {
                while (shortArray[slowRunnerIndex] < currentFastNumber) {
                    slowRunnerIndex++;
                    if (slowRunnerIndex >= shortArray.length) break;
                }
            }

            if (slowRunnerIndex >= shortArray.length) break;

            if (shortArray[slowRunnerIndex] == currentFastNumber) {
                intersect.add(currentFastNumber);
                slowRunnerIndex++;
                if (slowRunnerIndex >= shortArray.length) break;
            }
        }
        return intersect.stream().mapToInt(i -> i).toArray();
    }

    public int[] intersect(int[] nums1, int[] nums2) {
        System.out.println("Sorting the arrays...");
        sort(nums1);
        sort(nums2);
        System.out.println("Sorting complete! Detecting intersects...");

        if (nums1.length > nums2.length) {
            return findIntersects(nums2, nums1);
        }
        else {
            return findIntersects(nums1, nums2);
        }
    }

    public static void main(String[] args) {

        int[] nums1 = Arrays.asList(1, 2, 3, 4).stream().mapToInt(i -> i).toArray();
        int[] nums2 = new int[]{1, 1};
        Intersect singleNumberCls = new Intersect();
        int[] intersectArr = singleNumberCls.intersect(nums1, nums2);
        System.out.println(String.format("IntersectArray: %s", Arrays.toString(intersectArr)));
    }
}
