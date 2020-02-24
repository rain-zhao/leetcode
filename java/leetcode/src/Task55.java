import org.junit.jupiter.api.Test;

public class Task55 {
    public boolean canJump(int[] nums) {
        if(nums.length < 2){
            return true;
        }

        int length = nums.length;
        //define
        int[] dp = new int[length];
        //init
        dp[0] = nums[0];

        if(dp[0] == 0){
            return false;
        }

        for (int i = 1; i < length-1; i++) {
            dp[i] = Math.max(dp[i-1]-1,nums[i]);
            if(dp[i]==0){
                return false;
            }
        }

        return true;
    }

    public boolean canJump2(int[] nums) {
        if(nums.length < 2){
            return true;
        }

        int length = nums.length;
        //define
        int max = nums[0];

        if(max== 0){
            return false;
        }

        for (int i = 1; i < length-1; i++) {
            max = Math.max(max-1,nums[i]);
            if(max==0){
                return false;
            }
        }

        return true;
    }

    //greedy
    public boolean canJump3(int[] nums) {
        if(nums.length < 2){
            return true;
        }

        int length = nums.length;
        //define
        int max = 0;


        for (int i = 0; i < length-1; i++) {
            max = Math.max(max,i+nums[i]);
            if(max == i){
                return false;
            }
        }

        return true;
    }

    @Test
    void test(){
        int[] nums = new int[]{2,0,0};
        System.out.println(canJump3(nums));
    }

}
