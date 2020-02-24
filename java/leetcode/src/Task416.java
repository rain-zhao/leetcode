import org.junit.jupiter.api.Test;

import java.util.Arrays;

public class Task416 {
    public boolean canPartition(int[] nums) {
        if(nums.length == 0){
            return true;
        }
        if(nums.length == 1){
            return false;
        }

        int sum = Arrays.stream(nums).sum();
        if((sum & 1) ==1){
            return false;
        }
        int mid = sum>>1;

        boolean[][] dp = new boolean[nums.length+1][mid+1];
        for (boolean[] rows : dp) {
            rows[0] = true;
        }

        for (int i = 1; i < nums.length+1; i++) {
            for (int j = 1; j < mid+1 ; j++) {
                dp[i][j] = dp[i-1][j];
                if(j -nums[i-1] >=0 ){
                    dp[i][j] |= dp[i-1][j-nums[i-1]];
                }
            }
        }

        return dp[nums.length][mid];
    }


    @Test
    void test(){
        int[] nums = new int[]{1,2,3,5};
        System.out.println(canPartition(nums));
    }

}
