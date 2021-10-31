package com.mybasepackage.misc;


import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;
import java.util.Stack;

public class Calculator {



    static String separator = " ";
    static Set<String> signSet = new HashSet<String>(Arrays.asList("+", "-", "/", "*"));


    public static boolean isSign(String member) {
        return signSet.contains(member);
    }

    public static double applyOperator(double leftElement, double rightElement, String operatorChar) {
        // note to reader: this one feels like a code repetition, but I'm running out of time :D
        // more elegant solutions are possible (eg mapping operatorchar to an operator etc)
        switch (operatorChar) {
            case "-": {
                return leftElement-rightElement;
            }
            case "+": {
                return leftElement+rightElement;
            }
            case "*": {
                return leftElement*rightElement;
            }
            case "/": {
                return leftElement/rightElement;
            }
        }

        // since no invalid operations will be fed, I assume this section is unreachable.
        return 0;
    }


    public double evaluate(String expr) {

        if (expr.equals("")) return 0; // handle edge case

        String[] members = expr.split(separator);

        Stack<Double> iteratedMemberStack = new Stack<Double>();

        for (String member: members) {
            if (isSign(member)) {
                // if stack has two elements, load them and apply operation
                if (iteratedMemberStack.size() >= 2) {
                    double rightElement = iteratedMemberStack.pop();
                    double leftElement = iteratedMemberStack.pop();
                    iteratedMemberStack.push(applyOperator(leftElement, rightElement, member));
                }
                // else, I assume we just discard the sign and keep on adding?
            }
            else {
                iteratedMemberStack.push(Double.parseDouble(member));
            }
        }

        if (iteratedMemberStack.size() == 0) return 0;
        return iteratedMemberStack.peek();
    }

    public static void main(String[] args) {

        Calculator cls = new Calculator();
        System.out.println(cls.evaluate("1 3 +"));
    }
}


