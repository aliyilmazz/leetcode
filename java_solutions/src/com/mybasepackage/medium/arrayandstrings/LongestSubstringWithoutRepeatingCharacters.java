package com.mybasepackage.medium.arrayandstrings;

import java.util.HashSet;
import java.util.stream.Collectors;

public class LongestSubstringWithoutRepeatingCharacters {

    public StringBuilder truncateWord(StringBuilder stringBuilder, Character letter) {
        // todo
        int charIndex = stringBuilder.indexOf(letter.toString());

        // if (charIndex == stringBuilder.length()-1) return new StringBuilder(letter.toString());

        return new StringBuilder(stringBuilder.substring(charIndex+1, stringBuilder.length()));
    }


    public int lengthOfLongestSubstring(String s) {

        int longestStreakCount = 0;
        int localStreakCount = 0;

        StringBuilder longestString = new StringBuilder();
        HashSet<Character> chars = new HashSet<>();
        for (int i=0; i<s.length(); i++) {
            Character currentChar = s.charAt(i);
            longestString.append(currentChar);
            if (chars.contains(currentChar)) {
                // todo
                longestStreakCount = Math.max(localStreakCount, longestStreakCount);
                longestString = truncateWord(longestString, currentChar);
                chars = longestString.toString().chars().mapToObj(x->(char)x).collect(Collectors.toCollection(HashSet::new));
                localStreakCount = longestString.length();
            }
            else {
                localStreakCount++;
                chars.add(currentChar);
            }
        }
        return Math.max(longestStreakCount, localStreakCount);
    }


    public static void main(String[] args) {

        LongestSubstringWithoutRepeatingCharacters longestSubstringCls = new LongestSubstringWithoutRepeatingCharacters();
        int length = longestSubstringCls.lengthOfLongestSubstring("dvdf");
        System.out.println("Length: " + length);
    }
}
