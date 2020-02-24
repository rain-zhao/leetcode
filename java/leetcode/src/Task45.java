import org.junit.jupiter.api.Test;

import java.util.Arrays;

public class Task45 {
    //dp
    public int jump(int[] nums) {
        if (nums.length < 2) {
            return 0;
        }

        //init
        int[] dp = new int[nums.length];
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[0] = 0;

        for (int i = 0; i < nums.length - 1; i++) {
            int max = Math.min(nums[i] + i, nums.length - 1);
            for (int j = i + 1; j <= max; j++) {
                dp[j] = Math.min(dp[j], dp[i] + 1);
            }
        }

        return dp[nums.length - 1];
    }

    public int jump2(int[] nums) {
        if (nums.length < 2) {
            return 0;
        }
        int cnt = 1;
        int cur = 0;

        while (cur + nums[cur] < nums.length-1) {
            int pos = cur;
            for (int i = cur + 1; i <= cur + nums[cur]; i++) {
                if(pos+nums[pos] < i+nums[i]){
                    pos = i;
                }
            }
            cur = pos;
            ++cnt;
        }

        return cnt;
    }

    public int jump3(int[] nums) {
        if (nums.length < 2) {
            return 0;
        }
        int end = 0;
        int cnt = 0;
        int maxPos = 0;

        for (int i = 0; i < nums.length-1; i++) {
            maxPos = Math.max(i+nums[i],maxPos);
            if(maxPos >= nums.length-1){
                ++cnt;
                break;
            }
            if(end == i){
                ++cnt;
                end = maxPos;
            }

        }


        return cnt;
    }


    @Test
    void test() {
        int[] nums = new int[]{2, 3, 1, 1, 4};
        System.out.println(jump2(nums));
    }
}
