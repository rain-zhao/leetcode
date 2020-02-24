import java.util.Arrays;

public class Task62 {
    //dp
    public int uniquePaths(int m, int n) {
        if (m < 2) {
            return m;
        }
        if (n < 2) {
            return n;
        }

        //define
        int[][] dp = new int[m][n];
        //init
        for (int j = 0; j < n; j++) {
            dp[0][j] = 1;
        }
        for (int i = 1; i < m; i++) {
            dp[i][0] = 1;
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                dp[i][j]=dp[i][j-1]+dp[i-1][j];
            }
        }
        return dp[m-1][n-1];
    }

    //dp2
    public int uniquePaths2(int m, int n) {
        if (m < 2) {
            return m;
        }
        if (n < 2) {
            return n;
        }

        //define
        int[]dp = new int[n];
        //init
        Arrays.fill(dp,1);

        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                dp[j]=dp[j]+dp[j-1];
            }
        }
        return dp[n-1];
    }

}
