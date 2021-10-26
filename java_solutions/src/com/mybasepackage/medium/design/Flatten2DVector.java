package com.mybasepackage.medium.design;


import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.stream.IntStream;

/**
 * Your Vector2D object will be instantiated and called as such:
 * Vector2D obj = new Vector2D(vec);
 * int param_1 = obj.next();
 * boolean param_2 = obj.hasNext();
 */


class Vector2D {
    int[][] vec;
    int[] flattenVec;
    int flattenVecCursor = 0;

    public Vector2D(int[][] vec) {
        this.vec = vec;

        List<Integer> flattenVecList = new ArrayList<>();
        Arrays.stream(vec)
                .forEach(i -> Collections.addAll(flattenVecList, Arrays.stream(i).boxed().toArray(Integer[]::new)));
        this.flattenVec = flattenVecList.stream().mapToInt(i -> i).toArray();
    }

    public int next() {
        return flattenVec[flattenVecCursor++];
    }

    public boolean hasNext() {
        return flattenVecCursor < flattenVec.length;
    }
}


public class Flatten2DVector {
    public static void main(String[] args) {
        Vector2D vector2D = new Vector2D(new int[][]{{1,2}, {3}, {4}});
        System.out.println(vector2D.next());    // return 1
        System.out.println(vector2D.next());    // return 2
        System.out.println(vector2D.next());    // return 3
        System.out.println(vector2D.hasNext()); // return True
        System.out.println(vector2D.hasNext()); // return True
        System.out.println(vector2D.next());    // return 4
        System.out.println(vector2D.hasNext()); // return False
    }

}
