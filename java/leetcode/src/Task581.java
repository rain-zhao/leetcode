import org.junit.jupiter.api.Test;

public class Task581 {
    public int findUnsortedSubarray(int[] nums) {
        if(nums.length < 2){
            return 0;
        }

        int left,right;

        left = 1;
        int i = 1;
        while(i< nums.length && nums[i] >= nums[i-1]){
            ++left;
            ++i;
        }
        if(i == nums.length){
            return 0;
        }
        for (; i < nums.length && left > 0 ; i++) {
            while(left > 0 && nums[i] < nums[left-1]){
                --left;
            }
        }

        right = nums.length-2;
        i = nums.length-2;

        while(i>=0 && nums[i] <= nums[i+1]){
           --right;
            --i;
        }

        for (; i >=0 && right<nums.length-1; i--) {
            while(right<nums.length-1 && nums[i] > nums[right+1]){
                ++right;
            }
        }

        return right-left+1;
    }

    @Test
    void test() {
        int[] nums = new int[]{2,5,3,1,4};
        System.out.println(findUnsortedSubarray(nums));
    }
}
