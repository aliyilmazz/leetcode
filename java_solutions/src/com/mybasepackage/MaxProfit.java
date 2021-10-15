package com.mybasepackage;

class MaxProfit {
    public int maxProfit(int[] prices) {
        int maxProfit = 0;
        int i = 0;
        while (i<prices.length-1) {
            int current_price = prices[i];
            int future_price = prices[i+1];
            if (current_price < future_price) {
                maxProfit += (future_price - current_price);
            }
            i++;
        }
        return maxProfit;
    }

    public static void main(String[] args) {
        MaxProfit solution = new MaxProfit();
        int[] prices = new int[]{1,2,3,4,5};
        int maxProfit = solution.maxProfit(prices);
        System.out.println(String.format("Max profit: %s", maxProfit));
    }
}
