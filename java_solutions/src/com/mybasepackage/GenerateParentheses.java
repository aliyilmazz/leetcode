package com.mybasepackage;

import java.util.ArrayList;
import java.util.List;

public class GenerateParentheses {


    List<String> parenthesesList;
    int n;

    public GenerateParentheses() {
        this.parenthesesList = new ArrayList<>();
    }


    public void _generateParentheses(StringBuilder substring, int completeParenthesesCount, int incompleteParenthesesCount) {
        if (completeParenthesesCount == this.n) {
            this.parenthesesList.add(substring.toString());
            return;
        }

        if (incompleteParenthesesCount == 0) {
            // no chance to append closure parentheses. only append opening parentheses and return.
            _generateParentheses(new StringBuilder(substring.append('(').toString()), completeParenthesesCount, 1);
            return;
        }

        else if ((completeParenthesesCount+incompleteParenthesesCount) == this.n) {
            // no chance to append opening parentheses. only append closure parentheses and return.
            _generateParentheses(new StringBuilder(substring.append(')').toString()), completeParenthesesCount+1, incompleteParenthesesCount-1);
            return;
        }

        StringBuilder cloneSubstring = new StringBuilder(substring.toString());
        _generateParentheses(new StringBuilder(cloneSubstring.append('(').toString()), completeParenthesesCount, incompleteParenthesesCount+1);
        if (incompleteParenthesesCount > 0) {
            _generateParentheses(new StringBuilder(substring.append(')').toString()), completeParenthesesCount+1, incompleteParenthesesCount-1);
        }

    }

    public List<String> generateParenthesis(int n) {
        this.n = n;
        _generateParentheses(new StringBuilder(), 0, 0);
        return this.parenthesesList;
    }

    public static void main(String[] args) {
        GenerateParentheses cls = new GenerateParentheses();
        List<String> parentheses = cls.generateParenthesis(8);
        System.out.println("Generated parentheses: " + parentheses.toString());
    }
}
