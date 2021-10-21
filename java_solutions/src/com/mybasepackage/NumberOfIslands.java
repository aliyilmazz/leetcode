package com.mybasepackage;

public class NumberOfIslands {


    public void purgeIsland(char[][] grid, int i, int j) {
        grid[i][j] = '0';
        if (i < grid.length-1) { // bottom side
            if (grid[i+1][j] == '1') {
                purgeIsland(grid, i+1, j);
            }
        }

        if (i > 0) { // top side
            if (grid[i-1][j] == '1') {
                purgeIsland(grid, i-1, j);
            }
        }

        if (j < grid[0].length-1) { // right side
            if (grid[i][j+1] == '1') {
                purgeIsland(grid, i, j+1);
            }
        }

        if (j > 0) { // left side
            if (grid[i][j-1] == '1') {
                purgeIsland(grid, i, j-1);
            }
        }
    }


    public int numIslands(char[][] grid) {
        if (grid==null) return 0;

        int numIslands = 0;


        for (int i=0; i<grid.length; i++) {
            for (int j=0; j<grid[i].length; j++) {
                if (grid[i][j] == '1') {
                    purgeIsland(grid, i, j);
                    numIslands++;
                }
            }
        }

        return numIslands;
    }

    public static void main(String[] args) {
        NumberOfIslands cls = new NumberOfIslands();
        char[][] grid =
        {
                {'1', '1', '1', '1', '0'},
                {'1', '1', '1', '1', '0'},
                {'1', '1', '1', '1', '0'},
                {'1', '1', '1', '1', '0'},
        };
        System.out.println("Number of islands: " + cls.numIslands(grid));
    }
}
