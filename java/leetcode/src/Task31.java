import org.junit.jupiter.api.Test;

import java.util.Arrays;

public class Task31 {
    public void nextPermutation(int[] nums) {

        if(nums.length < 2){
            return;
        }

        int length = nums.length;

        int i = length-2;

        while(i >= 0 && nums[i] >= nums[i+1]){
            --i;
        }

        if(i == -1){
            Arrays.sort(nums);
            return;
        }
        int j = length-1;
        while(nums[i] >= nums[j]){
            --j;
        }
        swap(nums,i,j);
        reverse(nums,i+1,nums.length-1);

    }

    void reverse(int[] nums,int l,int r){
        while(l < r){
            swap(nums,l,r);
            ++l;
            --r;
        }
    }

    void swap(int[] nums,int i,int j){
        nums[i] = nums[i]^nums[j];
        nums[j] = nums[i]^nums[j];
        nums[i] = nums[i]^nums[j];
    }


    @Test
    void test(){
        int[] nums = new int[]{1,5,1};
        nextPermutation(nums);
        //print 1,3,1,2,4,7
    }
}
