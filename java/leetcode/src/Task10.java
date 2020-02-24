import org.junit.jupiter.api.Test;

public class Task10 {
    public boolean isMatch(String s, String p) {
        //condition

        //define
        int m = s.length();
        int n = p.length();

        boolean[][] dp = new boolean[m+1][n+1];

        //init
        dp[0][0] = true;
        for (int i = 2; i <= n; i++) {
            if(p.charAt(i-1) == '*' && p.charAt(i-2) != '*'){
                dp[0][i] = dp[0][i-2];
            }
        }

        //loop
        for (int i = 1; i <= m ; i++) {
            for (int j = 1; j <= n ; j++) {
                if(s.charAt(i-1) == p.charAt(j-1) || p.charAt(j-1) == '.'){
                    dp[i][j] = dp[i-1][j-1];
                }else if(p.charAt(j-1) == '*' && j-2 >= 0){
                    if(s.charAt(i-1) == p.charAt(j-2) || p.charAt(j-2) == '.'){
                        dp[i][j] = dp[i-1][j] || dp[i][j-2];
                    }else{
                        dp[i][j] = dp[i][j-2];
                    }
                }
            }
        }

        //return
        return dp[m][n];

    }

    @Test
    void test(){
        String s = "aaa";
        String p = "ab*a*c*a";
        System.out.println(isMatch(s,p));
    }
}
