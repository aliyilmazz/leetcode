package com.mybasepackage.medium.dynamicprogramming;

import java.util.Arrays;
import java.util.HashMap;

public class CoinChange {


    HashMap<Integer, Integer> solutionMap;
    int[] coins;

    public CoinChange() { solutionMap = new HashMap<>(); }


    public int _coinChange(int amount) {
        if (solutionMap.containsKey(amount)) return solutionMap.get(amount);


        if (coins[0] > amount) { // even minimum coin is bigger than amount. return -1
            solutionMap.put(amount, -1);
            return -1;
        }

        int coinIndex = 0;
        while (coinIndex < coins.length-1) {
            if (coins[coinIndex+1] < amount) coinIndex++;
            else break;
        }

        int minAmount = Integer.MAX_VALUE;

        while (coinIndex>=0) {
            int coinCountForRemainingAmount = _coinChange(amount-coins[coinIndex]);
            if (coinCountForRemainingAmount == -1) {
                // do nothing. pass
            }
            else {
                int coinAmountWithCurrentCoin = 1 + coinCountForRemainingAmount;
                minAmount = Math.min(minAmount, coinAmountWithCurrentCoin);
            }
            coinIndex--;
        }

        if (minAmount != Integer.MAX_VALUE) {
            solutionMap.put(amount, minAmount);
            return minAmount;
        }
        else {
            solutionMap.put(amount, -1);
            return -1;
        }
    }

    public int coinChange(int[] coins, int amount) {

        this.coins = coins;
        Arrays.sort(this.coins);
        Arrays.stream(coins).forEach(i -> solutionMap.put(i, 1));
        solutionMap.put(0, 0);
        //IntStream.range(0, this.coins[0]).forEach(i -> solutionMap.put(i, -1));
        int coinCount = _coinChange(amount);
        return coinCount;
    }

    public static void main(String[] args) {
        CoinChange cls = new CoinChange();
        int[] coins = {1,2,5};
        int amount = 11;
        //int[] coins = {1,4,5};
        //int amount = 8;
        int coinCount = cls.coinChange(coins, amount);
        System.out.println("Total number of coins: " + coinCount);
    }
}