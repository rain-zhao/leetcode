import org.junit.jupiter.api.Test;

public class Task123 {

    Task188 task188 = new Task188();

//    public int maxProfit(int[] prices) {
//        return task188.maxProfit(2,prices);
//    }


//    public int maxProfit(int[] prices) {
//
//        if(prices.length < 2){
//            return 0;
//        }
//
//        int l = prices.length;
//        int[][][] mp = new int[l][3][2];
//
//        //init
//        mp[0][0][1] = mp[0][1][1] = mp[0][2][1] = -prices[0];
//
//        for (int i = 1; i < l; i++) {
//            mp[i][0][1] = Math.max(mp[i-1][0][1],-prices[i]);
//
//            mp[i][1][0] = Math.max(mp[i-1][1][0],mp[i-1][0][1]+prices[i]);
//            mp[i][1][1] = Math.max(mp[i-1][1][1],mp[i-1][1][0]-prices[i]);
//
//            mp[i][2][0] = Math.max(mp[i-1][2][0],mp[i-1][1][1]+prices[i]);
//
//        }
//
//        return Math.max(mp[l-1][1][0],mp[l-1][2][0]);
//
//    }

    public int maxProfit(int[] prices) {

        if (prices.length < 2) {
            return 0;
        }

        int l = prices.length;

        //init
        int relese1 = 0, release2 = 0, hold1 = -prices[0], hold2 = -prices[0];

        for (int i = 1; i < l; i++) {
            release2 = Math.max(release2, hold2 + prices[i]);
            hold2 = Math.max(hold2, relese1 - prices[i]);
            relese1 = Math.max(relese1, hold1+prices[i]);
            hold1 = Math.max(hold1, -prices[i]);

        }

        return release2;

    }


    @Test
    void test(){
        int[] prices = new int[]{7,1,5,3,6,4};

        System.out.println(maxProfit(prices));
    }
}
