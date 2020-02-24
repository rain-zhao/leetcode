import org.junit.jupiter.api.Test;

import java.util.Arrays;

public class Task494 {

    int cnt = 0;
    public int findTargetSumWays(int[] nums, int S) {
        if(nums.length == 0){
            return 0;
        }

        backtrack(nums,S,0);

        return cnt;
    }

    private void backtrack(int[] nums, int s, int idx) {
        if(idx == nums.length){
            if(s == 0){
                ++cnt;
            }
            return;
        }

        backtrack(nums,s+nums[idx],idx+1);
        backtrack(nums,s-nums[idx],idx+1);

    }


    //dp
    public int findTargetSumWays2(int[] nums, int S) {
        if(nums.length == 0){
            return 0;
        }

        int max = Arrays.stream(nums).sum();


        if((S < 0 && -max > S) ||(S > 0 && max < S)){
           return 0;
        }

        int[][] dp = new int[nums.length][max*2+1];

        //init
        ++dp[0][max+nums[0]];
        ++dp[0][max-nums[0]];

        int sum =nums[0];
        for (int i = 1; i < nums.length; i++) {
            for (int j = max-sum; j <= max+sum ; j++) {
                dp[i][j+nums[i]]+=dp[i-1][j];
                dp[i][j-nums[i]]+=dp[i-1][j];
            }
            sum+=nums[i];
        }

        return dp[nums.length-1][max+S];
    }



    @Test
    void test(){
        int[] nums = new int[]{0,0,0,0,0,0,0,0,1};
        int s = 1;
        System.out.println(findTargetSumWays2(nums,s));
    }
}
