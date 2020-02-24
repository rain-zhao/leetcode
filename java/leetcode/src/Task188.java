import org.junit.jupiter.api.Test;

import java.util.Arrays;

public class Task188 {
    public int maxProfit(int k, int[] prices) {
        if(prices.length == 0){
            return 0;
        }
        int l = prices.length;

        //greedy
        if(k >= l/2){
            int profit = 0;

            for (int i = 1; i < l; i++) {
                if(prices[i] > prices[i-1]){
                    profit +=prices[i]-prices[i-1];
                }
            }
            return profit;
        }

        int[][][] mp = new int[l][k+1][2];

        //init
        for (int i = 0; i < k+1; i++) {
            mp[0][i][1] = -prices[0];
        }

        for (int i = 1; i < l ; i++) {
            for (int j = 0; j < k+1 ; j++) {
                if(j>0){
                    mp[i][j][0]=Math.max(mp[i-1][j][0],mp[i-1][j-1][1]+prices[i]);
                }
                mp[i][j][1]=Math.max(mp[i-1][j][1],mp[i-1][j][0]-prices[i]);
            }
        }

        int max = mp[l-1][0][0];
        for (int i = 1; i < k+1; i++) {
            max = Math.max(max,mp[l-1][i][0]);
        }

        return max;
    }

    @Test
    void test(){
        int[] prices = new int[]{3,2,6,5,0,3};
        int k = 2;
        System.out.println(maxProfit(k,prices));
    }
}
