import org.junit.jupiter.api.Test;

import java.util.Arrays;

public class Task152 {
//    public int maxProduct(int[] nums) {
//
//        if(nums.length == 0){
//            return 0;
//        }
//
//        int l = nums.length;
//        int[][] dp = new int[l][2];
//        dp[0][0]=dp[0][1]=nums[0];
//
//        for (int i = 1; i < l; i++) {
//            if(nums[i] == 0){
//                dp[i][0]=dp[i][1] = 0;
//            }else if(nums[i]> 0){
//                dp[i][0] = Math.max(nums[i],dp[i-1][0]*nums[i]);
//                dp[i][1] = Math.min(nums[i],dp[i-1][1]*nums[i]);
//            }else{
//                dp[i][0] = Math.max (nums[i],dp[i-1][1]*nums[i]);
//                dp[i][1] = Math.min(nums[i],dp[i-1][0]*nums[i]);
//            }
//        }
//
//        int res = dp[0][0];
//        for (int i = 1; i < l; i++) {
//            if(dp[i][0] > res){
//                res = dp[i][0];
//            }
//        }
//        return res;
//
//    }

    public int maxProduct(int[] nums) {

        if (nums.length == 0) {
            return 0;
        }

        int l = nums.length;

        int res = nums[0], max = nums[0], min = nums[0];

        for (int i = 1; i < l; i++) {
            if (nums[i] == 0) {
                max = min = 0;
            } else if (nums[i] > 0) {
                max = Math.max(nums[i], max * nums[i]);
                min = Math.min(nums[i], min * nums[i]);
            } else {
                int temp = max;
                max = Math.max(nums[i], min * nums[i]);
                min = Math.min(nums[i], temp * nums[i]);
            }

            res = max > res ? max : res;
        }

        return res;

    }

    @Test
    void test() {
        int[] nums = {-4,-3,-2};
        System.out.println(maxProduct(nums));
    }

}
