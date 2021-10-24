package com.mybasepackage.medium.dynamicprogramming;

public class UniquePaths {



    int[][] grid;


    public int _findUniquePaths(int x, int y) {
        if (grid[x][y] != 0) return grid[x][y];
        grid[x][y] = _findUniquePaths(x, y+1) + _findUniquePaths(x+1, y);
        return grid[x][y];
    }

    public int uniquePaths(int m, int n) {
        this.grid = new int[m][n];

        for(int i=0; i<n; i++) {
            grid[m-1][i] = 1;
        }

        for (int i=0; i<m; i++) {
            grid[i][n-1] = 1;
        }

        return _findUniquePaths(0,0);
    }


    public static void main(String[] args) {
        UniquePaths cls = new UniquePaths();
        int m=1, n=1;
        int uniquePathCount = cls.uniquePaths(m,n);
        System.out.println("Unique Paths: " +  uniquePathCount);
    }
}
