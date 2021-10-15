package com.mybasepackage;


import java.util.Arrays;

public class SetMatrixZeroes {

    public void setZeroes(int[][] matrix) {

        if (matrix.length == 0) return;

        int colCount = matrix[0].length;
        int rowCount = matrix.length;
        boolean[] columnMarker = new boolean[colCount];
        boolean[] rowMarker = new boolean[rowCount];
        Arrays.fill(columnMarker, false);
        Arrays.fill(rowMarker, false);
        for (int rowIndex=0; rowIndex<rowCount; rowIndex++) {
            for (int colIndex=0; colIndex<colCount; colIndex++) {
                if (matrix[rowIndex][colIndex] == 0) {
                    rowMarker[rowIndex] = true;
                    columnMarker[colIndex] = true;
                }
            }
        }

        //System.out.println("RowMarker: " + Arrays.toString(rowMarker) + " ColMarker: " + Arrays.toString(columnMarker));


        int[] currentRow;
        for (int rowIndex=0; rowIndex<rowCount; rowIndex++) {
            currentRow = matrix[rowIndex];
            if (rowMarker[rowIndex]) {
                Arrays.fill(currentRow, 0);
            }
            else {
                for (int colIndex=0; colIndex<colCount; colIndex++) {
                    if (columnMarker[colIndex]) {
                        currentRow[colIndex] = 0;
                    }
                }
            }
        }

        //System.out.println("Final matrix: " + Arrays.deepToString(matrix));
    }


    public static void main(String[] args) {
        SetMatrixZeroes sln = new SetMatrixZeroes();
        int[][] matrix = {{0,1,2,0},{3,4,5,2},{1,3,1,5}};
        sln.setZeroes(matrix);
    }
}
