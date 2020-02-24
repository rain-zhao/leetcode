import org.junit.jupiter.api.Test;

import java.util.Arrays;

public class Task283 {
    public void moveZeroes(int[] nums) {
        int cnt = 0;
        for (int i = 0; i < nums.length; i++) {
            if(nums[i] == 0){
                ++cnt;
            }else {
                nums[i-cnt] = nums[i];
            }
        }
        Arrays.fill(nums,nums.length-cnt,nums.length,0);
    }

    public void moveZeroes2(int[] nums) {
        int cnt = 0;
        for (int i = 0; i < nums.length; i++) {
            if(nums[i] == 0){
                ++cnt;
            }else {
                swap(nums,i-cnt,i);
            }
        }
    }

    void swap(int[] nums,int i,int j){
        if(i == j){
            return;
        }
        nums[i] = nums[i]^nums[j];
        nums[j] = nums[i]^nums[j];
        nums[i] = nums[i]^nums[j];
    }


    @Test
    void test(){
        int[] nums = new int[]{0,1,0,3,12};
        System.out.println(nums);
        moveZeroes(nums);
        System.out.println(nums);
    }
}
