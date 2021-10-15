package com.mybasepackage;

import java.util.*;
import java.util.stream.Stream;

public class Anagrams {

    HashMap<String, Integer> orderedWordToWordPoolMap;
    List<List<String>> wordPool;

    public Anagrams() {
        this.wordPool = new ArrayList<>();
        this.orderedWordToWordPoolMap = new HashMap<>();
    }

    public void groupAnagrams(String[] strs) {

        for (int j=strs.length-1; j>=0; j--) {
            String currentWord = strs[j];
            char[] charArray = currentWord.toCharArray();
            Arrays.sort(charArray);
            String orderedWord = new String(charArray);

            enrichOrRegisterPool: {
                for (String orderedWordInHash: this.orderedWordToWordPoolMap.keySet())
                    if (orderedWord.equals(orderedWordInHash)) {
                        int index = this.orderedWordToWordPoolMap.get(orderedWordInHash);
                        wordPool.get(index).add(currentWord);
                        break enrichOrRegisterPool;
                    }
                wordPool.add(new ArrayList<>(List.of(currentWord)));
                this.orderedWordToWordPoolMap.put(
                        orderedWord,
                        wordPool.size()-1
                );
            }
        }
    }

    public static void main(String[] args) {
        Anagrams anagramsCls = new Anagrams();
        anagramsCls.groupAnagrams(
                Stream.of("eat", "tea", "tan", "ate", "nat", "bat").toArray(String[]::new)
        );
        System.out.println(anagramsCls.wordPool);
    }
}
