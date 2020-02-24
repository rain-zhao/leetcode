import org.junit.jupiter.api.Test;

public class Task312 {
    public int maxCoins(int[] nums) {
        if(nums.length == 0){
            return 0;
        }
        if(nums.length == 1){
            return nums[0];
        }

        int[] array = new int[nums.length+2];
        System.arraycopy(nums,0,array,1,nums.length);
        int size = array.length;
        array[0] = array[size-1] = 1;

        int[][] dp = new int[size][size];


        for (int len = 2; len < size; len++) {
            for (int i = 0; i < size-len; i++) {
                int j = i+len;
                for (int k = i+1; k < j; k++) {
                    dp[i][j] = Math.max(dp[i][j],dp[i][k]+dp[k][j]+array[k]*array[i]*array[j]);
                }
            }
        }

        return dp[0][size-1];
    }

    @Test
    void test(){
        int[] nums = new int[]{3,1,5,8};
        System.out.println(maxCoins(nums));
    }
}
