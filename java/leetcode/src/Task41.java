import org.junit.jupiter.api.Test;

import java.util.Arrays;

public class Task41 {
    public int firstMissingPositive(int[] nums) {
        if(nums.length == 0){
            return 1;
        }

        Arrays.sort(nums);
        int length = nums.length;

        int i = 0;
        while(i< length &&  nums[i] <= 0){
            ++i;
        }
        int miss = 1;
        for (; i < nums.length; ++i) {
            if(miss == nums[i]){
                ++miss;
            }else if(miss < nums[i]){
                break;
            }
        }

        return miss;
    }

    public int firstMissingPositive2(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            while(nums[i] != i+1 && nums[i] > 0 && nums[i] <= nums.length && nums[i] != nums[nums[i]-1]){
                int j = nums[i];
                nums[i] = nums[j-1];
                nums[j-1] = j;
            }
        }

        for (int i = 0; i < nums.length; i++) {
            if(nums[i] != i+1){
                return i+1;
            }
        }

        return nums.length+1;
    }

    @Test
    void test(){
        int[] nums = new int[]{3,4,-1,1};
        System.out.println(firstMissingPositive2(nums));
    }
}
