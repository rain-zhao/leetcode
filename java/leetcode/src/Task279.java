import org.junit.jupiter.api.Test;

public class Task279 {
    public int numSquares(int n) {
        if (n < 4) {
            return n;
        }

        int[] dp = new int[n + 1];

        for (int i = 1; i <= n; i++) {
            dp[i] =i;

            for (int j = 1; i-j*j >= 0 ; j++) {
                dp[i] = Math.min(dp[i],dp[i-j*j]+1);
            }

        }

        return dp[n];
    }


    @Test
    void test(){
        int n = 13;
        System.out.println(numSquares(n));
    }
}
