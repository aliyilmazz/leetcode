package com.mybasepackage;

import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class LetterCombinationsPhoneNumber {

    Map<Character, List<Character>> letters;
    List<Integer> combinationIndexList;
    List<List<Character>> targetedLetterCombinations;

    public LetterCombinationsPhoneNumber() {
        this.letters = new HashMap<>();
        this.letters.put('2', new ArrayList<>(Stream.of('a', 'b', 'c').map(i->(char)i).collect(Collectors.toList())));
        this.letters.put('3', new ArrayList<>(Stream.of('d', 'e', 'f').map(i->(char)i).collect(Collectors.toList())));
        this.letters.put('4', new ArrayList<>(Stream.of('g', 'h', 'i').map(i->(char)i).collect(Collectors.toList())));
        this.letters.put('5', new ArrayList<>(Stream.of('j', 'k', 'l').map(i->(char)i).collect(Collectors.toList())));
        this.letters.put('6', new ArrayList<>(Stream.of('m', 'n', 'o').map(i->(char)i).collect(Collectors.toList())));
        this.letters.put('7', new ArrayList<>(Stream.of('p', 'q', 'r', 's').map(i->(char)i).collect(Collectors.toList())));
        this.letters.put('8', new ArrayList<>(Stream.of('t', 'u', 'v').map(i->(char)i).collect(Collectors.toList())));
        this.letters.put('9', new ArrayList<>(Stream.of('w', 'x', 'y', 'z').map(i->(char)i).collect(Collectors.toList())));
        combinationIndexList = new ArrayList<>();
        targetedLetterCombinations = new ArrayList<>();
    }

    public String extractString() {
        StringBuilder newString = new StringBuilder();
        for (int i=0; i<this.combinationIndexList.size(); i++) {
            int index = this.combinationIndexList.get(i);
            newString.append(this.targetedLetterCombinations.get(i).get(index));
        }
        return newString.toString();
    }

    public boolean incrementIndexList() {
        int index = this.combinationIndexList.size()-1;
        boolean overflow = true;
        while (overflow) {
            int lastDigitIndex = this.combinationIndexList.get(index);
            lastDigitIndex++;
            if (lastDigitIndex == this.targetedLetterCombinations.get(index).size()) {
                this.combinationIndexList.set(index, 0);
                index--;
                if (index < 0) { // all digits are reset, so we traversed all possible options
                    return false;  // terminate outer flow
                }
            }
            else {
                this.combinationIndexList.set(index, lastDigitIndex);
                overflow = false;
            }
        }
        return true;
    }

    public List<String> letterCombinations(String digits) {

        if (digits.equals("")) return new ArrayList<>();

        List<String> letterCombinations = new ArrayList<>();

        for (int i=0; i<digits.length(); i++) {
            char digit = digits.charAt(i);
            this.targetedLetterCombinations.add(this.letters.get(digit));
        }

        for (List<Character> targetedLetterCombination: this.targetedLetterCombinations) {
            this.combinationIndexList.add(0);
        }

        boolean incrementSucceeded = true;
        while (incrementSucceeded) {
            String newString = extractString();
            incrementSucceeded = incrementIndexList();
            letterCombinations.add(newString);
        }

        return letterCombinations;
    }

    public static void main(String[] args) {
        LetterCombinationsPhoneNumber cls = new LetterCombinationsPhoneNumber();
        List<String> letterCombinations = cls.letterCombinations("29");
        System.out.println("Letter combinations: " + letterCombinations.toString());
    }
}
