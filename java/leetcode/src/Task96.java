import org.junit.jupiter.api.Test;

public class Task96 {
    public int numTrees(int n) {
        if(n < 2){
            return 1;
        }

        int[] dp = new int[n+1];
        dp[0]=dp[1]=1;

        for (int i = 2; i <= n; i++) {
            int sum=0;
            for (int j = 0; j < i; j++) {
                sum+= dp[j] * dp[i-j-1];
            }
            dp[i]=sum;
        }

        return dp[n];
    }

    @Test
    void test(){
        int n = 3;
        System.out.println(numTrees(n));
    }
}
