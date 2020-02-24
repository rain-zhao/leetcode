import org.junit.jupiter.api.Test;

public class Task714 {
    public int maxProfit(int[] prices, int fee) {
        if (prices.length < 2) {
            return 0;
        }

        int l = prices.length;

        //init
        int release = 0,hold = -prices[0];

        for (int i = 1; i < l; i++) {
            int tempRelease = release;
            release=Math.max(release,hold+prices[i]-fee);
            hold=Math.max(hold,tempRelease-prices[i]);
        }

        return release;
    }

    @Test
    void test() {
        int[] prices = new int[]{1, 3, 2, 8, 4, 9};
        int fee = 2;

        System.out.println(maxProfit(prices,fee));
    }
}
