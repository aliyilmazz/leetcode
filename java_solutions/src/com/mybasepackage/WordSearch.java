package com.mybasepackage;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class WordSearch {

    boolean wordExists;

    public WordSearch() {
        this.wordExists = false;
    }


    public void _exist(char[][] board, int mIndex, int nIndex, String word, List<List<Integer>> usedLetters) {

        if (this.wordExists) return;

        if (word.equals("")) {
            this.wordExists = true;
            return;
        }

        char currentCharacter = word.charAt(0);


        boolean upAvailable = true;
        boolean downAvailable = true;
        boolean rightAvailable = true;
        boolean leftAvailable = true;

        for(List<Integer> usedLetterCoordinates: usedLetters) {
            Integer x = usedLetterCoordinates.get(0);
            Integer y = usedLetterCoordinates.get(1);
            if (x == mIndex-1 && y == nIndex) upAvailable = false;
            else if (x == mIndex && y == nIndex-1) leftAvailable = false;
            else if (x == mIndex && y == nIndex+1) rightAvailable = false;
            else if (x == mIndex+1 && y == nIndex) downAvailable = false;
        }

        if (upAvailable) {
            if (mIndex > 0) {
                if (board[mIndex - 1][nIndex] == currentCharacter) {
                    List<List<Integer>> lettersForMovingUp = new ArrayList<>(usedLetters);
                    lettersForMovingUp.add(new ArrayList<>(Arrays.asList(mIndex - 1, nIndex)));
                    _exist(board, mIndex - 1, nIndex, word.substring(1), lettersForMovingUp);
                }
            }
        }

        if (downAvailable) {
            if (mIndex < board.length-1) {
                if (board[mIndex+1][nIndex] == currentCharacter) {
                    //char[][] newBoard = Arrays.stream(board).map(char[]::clone).toArray(char[][]::new);
                    List<List<Integer>> lettersForMovingDown = new ArrayList<>(usedLetters);
                    lettersForMovingDown.add(new ArrayList<>(Arrays.asList(mIndex+1, nIndex)));
                    _exist(board, mIndex+1, nIndex, word.substring(1), lettersForMovingDown);
                }
            }
        }

        if (leftAvailable) {
            if (nIndex > 0) {
                if (board[mIndex][nIndex-1] == currentCharacter) {
                    //char[][] newBoard = Arrays.stream(board).map(char[]::clone).toArray(char[][]::new);
                    List<List<Integer>> lettersForMovingLeft = new ArrayList<>(usedLetters);
                    lettersForMovingLeft.add(new ArrayList<>(Arrays.asList(mIndex, nIndex-1)));
                    _exist(board, mIndex, nIndex-1, word.substring(1), lettersForMovingLeft);
                }
            }
        }

        if (rightAvailable) {
            if (nIndex < board[mIndex].length-1) {
                if (board[mIndex][nIndex+1] == currentCharacter) {
                    //char[][] newBoard = Arrays.stream(board).map(char[]::clone).toArray(char[][]::new);
                    List<List<Integer>> lettersForMovingRight = new ArrayList<>(usedLetters);
                    lettersForMovingRight.add(new ArrayList<>(Arrays.asList(mIndex, nIndex+1)));
                    _exist(board, mIndex, nIndex+1, word.substring(1), lettersForMovingRight);
                }
            }
        }
    }

    public boolean exist(char[][] board, String word) {
        if (word.equals("")) return true;


        char firstLetter = word.charAt(0);
        for (int i=0; i<board.length; i++) { // 0 -> m
            for (int j=0; j<board[i].length; j++) { // 0 -> n
                if (board[i][j] == firstLetter) {
                    //char[][] newBoard = Arrays.stream(board).map(char[]::clone).toArray(char[][]::new);

                    List<List<Integer>> usedLetters = new ArrayList<>();
                    usedLetters.add(new ArrayList<>(Arrays.asList(i, j)));
                    _exist(board, i, j, word.substring(1), usedLetters);
                }
            }
        }
        return this.wordExists;
    }

    public static void main(String[] args) {
        WordSearch cls = new WordSearch();
        char[][] board = {{'A', 'B', 'C', 'E'}, {'S', 'F', 'C', 'S'},{'A', 'D', 'E', 'E'}};
        String word = "ABCCED";
        boolean wordExists = cls.exist(board, word);
        System.out.println("Word '" + word + "' exists: " + wordExists);
    }
}
