import org.junit.jupiter.api.Test;

import java.util.Arrays;

public class Task16 {
    //brute force
    public int threeSumClosest(int[] nums, int target) {
        int res = Integer.MAX_VALUE;
        for (int i = 0; i < nums.length-2; i++) {
            for (int j = i+1; j < nums.length-1; j++) {
                for (int k = j+1; k < nums.length; k++) {
                    int sum = nums[i]+nums[j]+nums[k];
                    res = Math.abs(sum - target) > Math.abs(res) ? res: sum - target;
                }
            }
        }

        return target + res;
    }

    public int threeSumClosest2(int[] nums, int target) {
        int res = Integer.MAX_VALUE;


        Arrays.sort(nums);
        for (int i = 1; i < nums.length-1; i++) {
            int j = i-1,k=i+1;
            while(j >=0 && k <nums.length){
                int sum = nums[i]+nums[j]+nums[k];
                res = Math.abs(sum - target) > Math.abs(res) ? res: sum - target;
                if(sum - target == 0){
                    return sum;
                }else if(sum - target > 0){
                    --j;
                }else{
                    ++k;
                }
            }

        }

        return target + res;
    }

    @Test
    void test(){
        int[] nums = new int[]{-1,2,1,-4};
        int target = 1;
        System.out.println(threeSumClosest2(nums,target));
    }
}
