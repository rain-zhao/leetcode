import org.junit.jupiter.api.Test;

import java.util.LinkedList;

public class Task300 {
    //dp
    public int lengthOfLIS(int[] nums) {

        int l = nums.length;

        if(l < 1){
            return l;
        }

        int res = 1;

        int[] dp = new int[l];

        //init
        dp[0]=1;

        for (int i = 1; i < l; i++) {
            int imax = 0;
            for (int j = 0; j < i; j++) {
                if(dp[j] > imax && nums[i] > nums[j]){
                    imax = dp[j];
                }
            }
            dp[i] = imax + 1;
            res = Math.max(res,dp[i]);
        }

        return res;
    }

    //binary search
    public int lengthOfLIS2(int[] nums) {
        int l = nums.length;

        if(l < 1){
            return l;
        }

        int[] array = new int[l];

        //init
        array[0] = nums[0];
        int size = 1;

        for (int i = 1; i < l; i++) {
            int left = 0,right=size-1;
            while(left <= right){
                int p = left + (right-left)/2;
                if(nums[i] > array[p]){
                    //TODO
                    left = p+1;
                }else{
                    //TODO
                    right = p-1;

                }
            }
            array[left] = nums[i];
            if(left == size ){
               ++size;
            }

        }


        return size;
    }

    @Test
    void test(){
        int[] nums = new int[]{10,9,2,5,3,7,101,18};
        System.out.println(lengthOfLIS2(nums));
    }
}
