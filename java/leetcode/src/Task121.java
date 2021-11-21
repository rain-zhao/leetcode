import org.junit.jupiter.api.Test;

public class Task121 {
//    public int maxProfit(int[] prices) {
//
//        if(prices.length < 2){
//            return 0;
//        }
//
//        int res = 0;
//        int min = prices[0];
//        for (int i = 1; i < prices.length; i++) {
//            int price = prices[i];
//
//            if(price > min){
//                int profit = price-min;
//                res = profit > res ? profit : res;
//            }else{
//                min = price;
//            }
//
//        }
//
//        return res;
//    }

    //dp
    public int maxProfit(int[] prices) {

        if(prices.length < 2){
            return 0;
        }

        int l = prices.length;
        int[][] mp = new int[l][2];

        //init
        mp[0][1]= - prices[0];

        for (int i = 1; i < l; i++) {
            mp[i][0] = Math.max(mp[i-1][0],mp[i-1][1]+prices[i]);
            mp[i][1] = Math.max(mp[i-1][1],-prices[i]);
        }

        return mp[l-1][0];
    }

    @Test
    void test(){
        int[] prices = new int[]{7,1,5,3,6,4};

        System.out.println(maxProfit(prices));
    }

}
