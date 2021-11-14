package com.mybasepackage.misc;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class MinimumKnightMoves  {

        //5,5,1,4
//    int[][] solutionMap = {
//        {4, 1, 2, 1, 4},
//        {1, 2, 3, 2, 1},
//        {2, 3, 0, 3, 2},
//        {1, 2, 3, 2, 1},
//        {4, 1, 2, 1, 4}
//    };

    Map<Integer, Integer> moveCache = new HashMap<>();

    public int minKnightMoves(int x, int y) {
        int hashCode = Arrays.hashCode(new int[]{x, y});
        if (x==0 && y==0) return 0;
        if (moveCache.containsKey(hashCode)) {
            System.out.println("Cache hit for x: " + x + " y: " + y + "! Result: " + moveCache.get(hashCode));
            return moveCache.get(hashCode);
        }

        System.out.println("Current xy: " + x + " -- " + y);
//        if ((Math.abs(x) > 2 || Math.abs(y) > 2)) {

            int result;
            if (x>=0 && y>=0) {
                result = 1 + Math.min(minKnightMoves(x-1, y-2), minKnightMoves(x-2, y-1));
                moveCache.put(hashCode, result);
                return result;
            }
            else if (x>=0 && y<=0) {
                result = 1 + Math.min(minKnightMoves(x-1, y+2), minKnightMoves(x-2, y+1));
                moveCache.put(hashCode, result);
                return result;
            }
            else if (x<=0 && y<=0) {
                result = 1 + Math.min(minKnightMoves(x+1, y+2), minKnightMoves(x+2, y+1));
                moveCache.put(hashCode, result);
                return result;
            }
            else /* if (x<0 && y>0) */ {
                result = 1 + Math.min(minKnightMoves(x+1, y-2), minKnightMoves(x+2, y-1));
                moveCache.put(hashCode, result);
                return result;
            }
//        } else {
//            int rowIndex, colIndex;
//            rowIndex = (y>0)?(2-y):(2+(-1*y));
//            colIndex = x+2;
//            return this.solutionMap[rowIndex][colIndex];
//        }
    }
    public static void main(String[] args) {
        MinimumKnightMoves cls = new MinimumKnightMoves();
        System.out.println("Result: " + cls.minKnightMoves(2, 112));
    }
}


