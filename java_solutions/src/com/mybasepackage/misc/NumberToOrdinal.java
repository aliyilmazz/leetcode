package com.mybasepackage.misc;


import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class NumberToOrdinal {


    static String PREFIX_ST = "st";
    static String PREFIX_ND = "nd";
    static String PREFIX_RD = "rd";
    static String PREFIX_TH = "th";

    static Set<Integer> exceptionalTeenNumbers = new HashSet<Integer>(Arrays.asList(11,12,13));

    public static boolean isTeenNumber(Integer number) {
        int lastTwoDigitsOfGivenNumber = number % 100;
        return exceptionalTeenNumbers.contains(lastTwoDigitsOfGivenNumber);
    }

    public static String yieldPrefix(Integer number) {
        int lastDigit = number % 10;
        switch (lastDigit) {
            case 1: {
                return PREFIX_ST;
            }
            case 2: {
                return PREFIX_ND;
            }
            case 3: {
                return PREFIX_RD;
            }
            default: {
                return PREFIX_TH;
            }
        }
    }

    public static String numberToOrdinal( Integer number ) {

        // handle edge case #1
        if (number == 0) return "0";

        StringBuilder stringifiedNumber = new StringBuilder(number.toString());

        // handle edge case #2
        if (isTeenNumber(number)) return stringifiedNumber.append(PREFIX_TH).toString();

        String prefix = yieldPrefix(number);

        return stringifiedNumber.append(prefix).toString();


    }

    public static void main(String[] args) {
        System.out.println(numberToOrdinal(0));
        System.out.println(numberToOrdinal(1));
        System.out.println(numberToOrdinal(100));
        System.out.println(numberToOrdinal(1000));
        System.out.println(numberToOrdinal(1013));
        System.out.println(numberToOrdinal(2));
        System.out.println(numberToOrdinal(3));
        System.out.println(numberToOrdinal(3000));
    }
}


