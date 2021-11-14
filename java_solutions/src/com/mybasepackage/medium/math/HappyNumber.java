package com.mybasepackage.medium.math;

import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.Stream;

public class HappyNumber {



    public List<Integer> getDigits(int n) {
//        int multiplier = 1;
//        while (multiplier*10<=n && multiplier < Integer.MAX_VALUE/10) {
//            multiplier *= 10;
//        }
//
//        List<Integer> digits = new ArrayList<>();
//
//        while (n>0) {
//            int newDigit = n / multiplier;
//            digits.add(newDigit);
//            n -= newDigit * multiplier;
//            multiplier /= 10;
//        }

        // shorter solution
        return Integer.toString(n).chars().map(x -> x - '0').boxed().collect(Collectors.toList());
    }


    /**
     *
     * sum squares of digits, until reaching 1
     * if not reach 1, return false
     *
     * @param n
     * @return
     */
    public boolean isHappy(int n) {


        Set<Integer> visitedNumbers = new HashSet<>();
        //int MAX_ALLOWED_MEMBERS = 50;
        while (true) {
            //System.out.println("Trial #" + visitedNumbers.size());
            if (visitedNumbers.contains(n)/* || visitedNumbers.size() >= MAX_ALLOWED_MEMBERS */) {
                return false;
            }
            else {
                visitedNumbers.add(n);
            }

            List<Integer> digits = getDigits(n);
            int sumDigits = digits.stream().mapToInt(i -> i * i).sum();

            if (sumDigits == 1) {
                return true;
            }
            else {
                n = sumDigits;
            }
        }
    }



    public static void main(String[] args) {
        HappyNumber cls = new HappyNumber();
        System.out.println("IsHappy(" + 19 + "): " + cls.isHappy(19));
        System.out.println("IsHappy(" + 2 + "): " + cls.isHappy(2));
        System.out.println("IsHappy(" + 68 + "): " + cls.isHappy(68));
        System.out.println("IsHappy(" + 1999999999 + "): " + cls.isHappy(1999999999));
    }
}
