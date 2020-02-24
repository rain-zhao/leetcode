public class Task122 {
    public static int maxProfit(int[] prices) {
        int profit = 0;
        if(prices.length < 2){
            return profit;
        }
        for (int i = 1; i < prices.length; i++) {
            if(prices[i] > prices[i-1]){
                profit +=prices[i]-prices[i-1];
            }
        }
        return profit;
    }

    public static void main(String[] args) {
        int[] prices = new int[]{1,2,3,4,5};

        System.out.println(maxProfit(prices));
    }
}
