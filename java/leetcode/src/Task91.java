import org.junit.jupiter.api.Test;

public class Task91 {
    public int numDecodings(String s) {
        if(s.length() == 0 || s.charAt(0) == '0' ){
            return 0;
        }

        int[][] dp = new int[s.length()][2];
        dp[0][0] = 1;

        char[] array = s.toCharArray();
        for (int i = 1; i < array.length; i++) {
            if(array[i] != '0'){
                dp[i][0] = dp[i-1][0]+dp[i-1][1];
            }
            if(array[i-1] == '1' || array[i-1] == '2' && array[i] <='6'){
                dp[i][1] = dp[i-1][0];
            }

        }

        return dp[s.length()-1][0]+dp[s.length()-1][1];
    }

    public int numDecodings2(String s) {
        if(s.length() == 0 || s.charAt(0) == '0' ){
            return 0;
        }

        int[] dp = new int[s.length()+1];
        dp[0] = 1;
        dp[1] = 1;

        char[] array = s.toCharArray();
        for (int i = 1; i < array.length; i++) {
            if(array[i] != '0'){
                dp[i+1]+= dp[i];
            }
            if(array[i-1] == '1' || array[i-1] == '2' && array[i] <='6'){
                dp[i+1]+= dp[i-1];
            }

        }

        return dp[s.length()];
    }

    @Test
    void test(){
        String s = "226";
        System.out.println(numDecodings2(s));
    }
}
