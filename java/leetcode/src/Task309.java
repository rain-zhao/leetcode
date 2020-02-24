import org.junit.jupiter.api.Test;

public class Task309 {
//    public int maxProfit(int[] prices) {
//
//        if (prices.length < 2) {
//            return 0;
//        }
//
//        int l = prices.length;
//
//        //int[i][j]
//        //i: i st day max profit
//        //j: i st day's status:0-no stock,1-has stock,2-cool down
//        int[][] mp = new int[l][3];
//
//        //init
//        mp[0][1] = -prices[0];
//
//        for (int i = 1; i < l; i++) {
//            mp[i][0] = Math.max(mp[i - 1][0], mp[i - 1][2]);
//            mp[i][1] = Math.max(mp[i - 1][1], mp[i - 1][0] - prices[i]);
//            mp[i][2] = mp[i - 1][1] + prices[i];
//        }
//
//        return Math.max(mp[l - 1][0], mp[l - 1][2]);
//    }

    public int maxProfit(int[] prices) {

        if (prices.length < 2) {
            return 0;
        }

        int l = prices.length;

        //init
        int noStock = 0,hasStock= -prices[0],coolDown = 0;

        for (int i = 1; i < l; i++) {
            int tempCoolDown = coolDown;
            coolDown = hasStock + prices[i];
            hasStock = Math.max(hasStock, noStock - prices[i]);
            noStock = Math.max(noStock, tempCoolDown);

        }

        return Math.max(noStock, coolDown);
    }
    @Test
    void test() {
        int[] prices = new int[]{1,2,3,0,2};

        System.out.println(maxProfit(prices));
    }
}
