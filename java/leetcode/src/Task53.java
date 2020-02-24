import org.junit.jupiter.api.Test;

public class Task53 {
    public int maxSubArray(int[] nums) {
        if(nums.length == 0){
            return 0;
        }

        int res = nums[0];
        int max = res;

        for (int i = 1; i < nums.length; i++) {
            max = max > 0 ? max+nums[i] : nums[i];

            res = Math.max(res,max);
        }

        return res;
    }



    @Test
    void test(){
        int[] nums = new int[]{-2,1,-3,4,-1,2,1,-5,4};
        System.out.println(maxSubArray(nums));
    }
}
