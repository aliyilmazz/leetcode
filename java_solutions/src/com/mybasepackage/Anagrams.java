package com.mybasepackage;

import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Anagrams {

    HashMap<String, Integer> orderedWordToWordPoolMap;
    List<List<String>> wordPool;

    public Anagrams() {
        this.wordPool = new ArrayList<>();
        this.orderedWordToWordPoolMap = new HashMap<>();
    }

    public void groupAnagrams(String[] strs) {
        //List<HashSet<Character>> characterPoolList = new ArrayList<>();

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
//        HashMap<List<Character>, Integer> characterPoolToWordPoolIndexMap = new HashMap<>();
//        characterPoolToWordPoolIndexMap.put(
//                new ArrayList<>(Arrays.asList('a', 'b', 'c')),
//                2
//        );
//        characterPoolToWordPoolIndexMap.put(
//                new ArrayList<>(Arrays.asList('a', 'b', 'c', 'd')),
//                2
//        );
//        System.out.println(characterPoolToWordPoolIndexMap.keySet());
//        Set<Character> collect = "test".chars().mapToObj(i -> (char) i).collect(Collectors.toSet());

        Set<Character> firstCharSet = new HashSet<>(Arrays.asList('a', 'b', 'c'));
        Set<Character> secondCharSet = new HashSet<>(Arrays.asList('c', 'b', 'a'));
        System.out.println(firstCharSet.equals(secondCharSet));

        List<String> someList = new ArrayList<>(Arrays.asList("asd", "qwe"));
        someList.add(0, "zxc");
        System.out.println(someList.toString());

        Anagrams anagramsCls = new Anagrams();
        anagramsCls.groupAnagrams(
                Stream.of("eat", "tea", "tan", "ate", "nat", "bat").toArray(String[]::new)
        );
        System.out.println(anagramsCls.wordPool);
    }
}
