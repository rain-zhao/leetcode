import org.junit.jupiter.api.Test;

public class Task44 {
    public boolean isMatch(String s, String p) {

        int m = s.length();
        int n = p.length();

        boolean[][] dp = new boolean[m + 1][n + 1];

        //init
        dp[0][0] = true;
        for (int i = 1; i <= n; i++) {
            dp[0][i] = dp[0][i - 1] && p.charAt(i - 1) == '*';
        }

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                char c2 = p.charAt(j - 1);
                if (c2 == '*') {
                    dp[i][j] = dp[i - 1][j] || dp[i][j - 1];
                } else if (c2 == '?') {
                    dp[i][j] = dp[i - 1][j - 1];
                } else {
                    char c1 = s.charAt(i - 1);
                    if (c1 == c2) {
                        dp[i][j] = dp[i - 1][j - 1];
                    }
                }
            }
        }

        return dp[m][n];
    }

    @Test
    void test() {
        String s = "cb", p = "?a";
        System.out.println(isMatch(s, p));
    }
}
