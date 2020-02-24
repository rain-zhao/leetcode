import org.junit.jupiter.api.Test;

public class Task292 {
    public boolean canWinNim(int n) {
        if (n < 4) {
            return true;
        } else {
            return canWinNim(n - 1) || canWinNim(n - 2) || canWinNim(n - 3);
        }
    }

    //dp
    public boolean canWinNim2(int n) {
        if (n < 4) {
            return true;
        }

        boolean[] dp = new boolean[n + 1];
        dp[0] = dp[1] = dp[2] = dp[3] = true;

        for (int i = 4; i <= n; i++) {
            dp[i] = !(dp[i - 1] && dp[i - 2] && dp[i - 3]);
        }
        return dp[n];
    }

    @Test
    void test(){
        int n = 1348820612;
        System.out.println(canWinNim2(n));
    }
}
