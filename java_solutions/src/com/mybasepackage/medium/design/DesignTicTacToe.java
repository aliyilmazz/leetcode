package com.mybasepackage.medium.design;


import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.stream.IntStream;


class GameOverException extends RuntimeException {
    int winnerPlayer;
    public GameOverException(int winnerPlayer) { this.winnerPlayer=winnerPlayer; }
}

class TicTacToeO1 {
    //int[][] grid;
    int n;
    int[] solutionArray;

    public TicTacToeO1(int n) {
        this.n = n;
        //this.grid = new int[n][n];


        // [0,n-1] -> rows
        // [n, 2n-1] -> cols
        // [2n] -> diagonal from upperLeft to lowerRight
        // [2n+1] -> diagonal form lowerLeft to upperRight
        solutionArray = new int[2*n+2];
        Arrays.fill(solutionArray, 0);
    }

    List<Integer> _generateSolutionArrayIndices(int row, int col) {
        List<Integer> indices = new ArrayList<>();

        // identify row (guaranteed to exist)
        indices.add(row);

        // identify col (guaranteed to exist)
        indices.add(n + col);

        // bonus: identify diagonal (if exists)
        if (row==col) indices.add(2*n);
        if (row+col == n-1) indices.add(2*n+1);

        return indices;
    }

    public int move(int row, int col, int player) {
        List<Integer> indices = _generateSolutionArrayIndices(row, col);

        int number = (player==1?1:-1);


        solutionArray[row] += number;
        if (solutionArray[row]==n*number) return player;

        solutionArray[n+col] += number;
        if (solutionArray[n+col]==n*number) return player;


        if (row==col) {
            solutionArray[2*n] += number;
            if (solutionArray[2*n]==n*number) return player;
        }
        if (row+col == n-1) {
            solutionArray[2*n+1] += number;
            if (solutionArray[2*n+1]==n*number) return player;
        }

        return 0;

//        try {
//            indices.forEach(i-> {
//                solutionArray[i] += (player==1?1:-1);  // store negative sum (-1) for P2, positive sum (1) for P1
//                if (solutionArray[i] == n) throw new GameOverException(1);
//                if (solutionArray[i] == (n*-1)) throw new GameOverException(2);
//            });
//        }
//        catch (GameOverException gee) {
//            return gee.winnerPlayer;
//        }
//        return 0;  // code survived try-catch block, so no winners yet
    }
}



class TicTacToe {

    int[][] grid;
    int n;

    public TicTacToe(int n) {
        this.n = n;
        this.grid = new int[n][n];
    }


    public int move(int row, int col, int player) {
        grid[row][col] = player;
        return _checkGameProgress();
    }

    int _checkGameProgress() {
        // check horizontal match
        for (int i=0; i<n; i++) {
            int rowStarter = grid[i][0];
            if (rowStarter==0) continue;
            rowChecker: {
                for (int j=1; j<n; j++) {
                    if (grid[i][j] != rowStarter) break rowChecker;
                }
                return rowStarter;
            }
        }

        // check vertical match
        for (int i=0; i<n; i++) {
            int colStarter = grid[0][i];
            if (colStarter==0) continue;
            colChecker: {
                for (int j=1; j<n; j++) {
                    if (grid[j][i] != colStarter) break colChecker;
                }
                return colStarter;
            }
        }

        // check 1st diagonal match
        firstDiagonalMatch: {
            int diagonalValue = grid[0][0];
            if (diagonalValue==0) break firstDiagonalMatch;
            for (int i=0; i<n; i++) {
                if (grid[i][i] != diagonalValue) break firstDiagonalMatch;
            }
            return diagonalValue;
        }

        // check 2nd diagonal match
        secondDiagonalMatch: {
            int secondDiagonalValue = grid[0][n-1];
            if (secondDiagonalValue==0) break secondDiagonalMatch;
            for (int i=1; i<n; i++) {
                if (grid[i][n-(i+1)] != secondDiagonalValue) break secondDiagonalMatch;
            }
            return secondDiagonalValue;
        }

        return 0;
    }
}



public class DesignTicTacToe {
    public static void main(String[] args) {
        int n = 3;
        TicTacToeO1 cls = new TicTacToeO1(n);
        System.out.println(cls.move(0, 0, 1));
        System.out.println(cls.move(0, 2, 2));
        System.out.println(cls.move(2, 2, 1));
        System.out.println(cls.move(1, 1, 2));
        System.out.println(cls.move(2, 0, 1));
        System.out.println(cls.move(1, 0, 2));
        System.out.println(cls.move(2, 1, 1));
//        System.out.println(cls.move(1, 0, 1));
//        System.out.println(cls.move(1, 1, 1));
//        System.out.println(cls.move(1, 2, 1));

    }
}
