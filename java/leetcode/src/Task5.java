import org.junit.jupiter.api.Test;

public class Task5 {
    public String longestPalindrome(String s) {
        if(s.length() < 2){
            return s;
        }

        String res = s.substring(0,1);
        int l = s.length();
        //define
        boolean[][] dp = new boolean[l][l];

        //init
        for (int i = 0; i < l-1; i++) {
            dp[i][i] = true;
            dp[i][i+1] = s.charAt(i) == s.charAt(i+1);
            if(dp[i][i+1]){
                res = s.substring(i,i+2);
            }
        }
        dp[l-1][l-1] = true;

        //loop
        for (int j = 2; j < l; j++) {
            for (int i = 0; i < j-1; i++) {
                dp[i][j] = dp[i+1][j-1] && (s.charAt(i) == s.charAt(j));

                if(dp[i][j]){
                    res = s.substring(i,j+1);
                }
            }
        }

        //result
        return res;
    }

    // 中心扩展法
    public String longestPalindrome2(String s) {
        if(s.length() < 2){
            return s;
        }

        int start = 0,end=0;

        for (int i = 0; i < s.length(); i++) {
            int l1 = expand(s,i,i);
            int l2 = expand(s,i-1,i);
            int l = Math.max(l1,l2);
            if(l > end-start+1){
                start = i-l/2;
                end = i+(l-1)/2;
            }
        }

        return s.substring(start,end+1);
    }

    int expand(String s,int l,int r){
        while(l >=0 && r<=s.length() && s.charAt(l)==s.charAt(r)){
            --l;
            ++r;
        }
        return r-l-1;
    }

    @Test
    void test(){
        String s = "babad";
        System.out.println(longestPalindrome(s));
    }

}
