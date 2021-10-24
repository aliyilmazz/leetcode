package com.mybasepackage.medium.sortingandsearching;

public class Search2DMatrixII {

    public boolean searchMatrix(int[][] matrix, int target) {

        int rowIterator = 0;
        int colIterator = 0;

        while(rowIterator<matrix[0].length) {
            // accumulate row boundary
            int currentRowValue = matrix[0][rowIterator];
            if (currentRowValue == target) return true;
            if (currentRowValue < target) rowIterator++;
            else break;
        }

        while(colIterator<matrix.length) {
            // accumulate column boundary
            int currentColValue = matrix[colIterator][0];
            if (currentColValue == target) return true;
            if (currentColValue < target) colIterator++;
            else break;
        }

        for (int i=1; i<colIterator; i++) {
            for (int j=1; j<rowIterator; j++) {
                if (matrix[i][j] == target) return true;
            }
        }

        return false;
    }

    public static void main(String[] args) {
        Search2DMatrixII cls = new Search2DMatrixII();
        int[][] matrix = {{1,4,7,11,15},{2,5,8,12,19},{3,6,9,16,22},{10,13,14,17,24},{18,21,23,26,30}};
        boolean result = cls.searchMatrix(matrix, 20);
        System.out.println("Search result: " + result);
    }
}
