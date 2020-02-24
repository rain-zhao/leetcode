import org.junit.jupiter.api.Test;

public class Task72 {
    public int minDistance(String word1, String word2) {

        int l1 = word1.length();
        int l2 = word2.length();
        int[][] dp = new int[l1 + 1][l2 + 1];

        //init
        for (int i = 1; i <= l1; i++) {
            dp[i][0] = i;
        }
        for (int i = 1; i <= l2; i++) {
            dp[0][i] = i;
        }


        for (int i = 0; i < l1; i++) {
            for (int j = 0; j < l2; j++) {
                if(word1.charAt(i) == word2.charAt(j)){
                    dp[i+1][j+1]=dp[i][j];
                }else{
                    dp[i+1][j+1] = Math.min(Math.min(dp[i+1][j],dp[i][j+1]),dp[i][j])+1;
                }
            }
        }

        return dp[l1][l2];
    }

    @Test
    void test(){
        String word1 = "horse", word2 = "ros";
        System.out.println(minDistance(word1,word2));
    }
}
