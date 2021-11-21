import org.junit.jupiter.api.Test;

import java.util.Arrays;

public class Task322 {
    public int coinChange(int[] coins, int amount) {
        if(amount == 0){
            return 0;
        }
        if(coins.length == 0){
            return -1;
        }

        int MAX = amount+1;
        int[] dp = new int[MAX];
        Arrays.fill(dp,MAX);
        dp[0] = 0;


        for (int i = 1; i <= amount; i++) {
            for(int coin:coins){
                if(i >= coin){
                    dp[i] = Math.min(dp[i],dp[i-coin]+1);
                }
            }
        }

        return dp[amount] > amount ? -1:dp[amount];
    }

    @Test
    void test(){
        int[] coins = new int[]{1, 2, 5};
        int amount = 11;
        System.out.println(coinChange(coins,amount));
    }

}
