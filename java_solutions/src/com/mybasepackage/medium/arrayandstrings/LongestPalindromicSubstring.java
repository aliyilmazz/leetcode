package com.mybasepackage.medium.arrayandstrings;

public class LongestPalindromicSubstring {

    public boolean isPalindrome(String s) {
        int leftIndex = 0;
        int rightIndex = s.length()-1;
        while (leftIndex<rightIndex) {
            if (s.charAt(leftIndex) != s.charAt(rightIndex)) return false;
            else {
                leftIndex++;
                rightIndex--;
                if (leftIndex == rightIndex) break;
             }
        }
        return true;
    }

    public String longestPalindrome(String s) {
        String longestString = "";
        int longestLength = 0;
        for (int i=0; i<s.length(); i++) {
            for (int j=i+1; j<=s.length(); j++) {
                int candidateStringLength = j-i;
                if (candidateStringLength <= longestLength) continue;
                String candidateString = s.substring(i, j);
                if (isPalindrome(candidateString)) {
                    longestLength = candidateStringLength;
                    longestString = candidateString;
                }
            }
        }
        return longestString;
    }

    public static void main(String[] args) {
        String testString = "testString";
        System.out.println(testString.substring(0, 1));
        System.out.println(testString.substring(1, 3));
        System.out.println(testString.substring(1, 4));
        System.out.println(testString.substring(2, 5));
        LongestPalindromicSubstring longestPalindromicStringCls = new LongestPalindromicSubstring();
        String exampleInputString = "a";
        String longestPalindrome = longestPalindromicStringCls.longestPalindrome(exampleInputString);
        System.out.println("Example string: " + exampleInputString);
        System.out.println("Longest substring: " + longestPalindrome);
    }
}
