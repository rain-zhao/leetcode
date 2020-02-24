import org.junit.jupiter.api.Test;

public class Task33 {
    public int search(int[] nums, int target) {
        if (nums.length == 0) {
            return -1;
        }
        if (nums.length == 1) {
            return nums[0] == target ? 0 : -1;
        }
        if(target == nums[0]){
            return 0;
        }

        //search the min index
        int left=0,right = nums.length-1;
        int minIdx = -1;
        while(left <= right){
            int mid = left + (right-left)/2;
            if(nums[mid] > nums[(mid+1)%nums.length]){
                minIdx = (mid+1)%nums.length;
                break;
            }
            if(nums[mid] < nums[0]){
                right = mid - 1;
            }else {
                left = mid + 1;
            }
        }

        // binary search
        if(target >  nums[0]){
            left = 0;
            right = (minIdx-1+nums.length)%nums.length;
        }else{
            left = minIdx;
            right = nums.length-1;
        }

        while(left <= right){
            int mid = left + (right-left)/2;
            if(target == nums[mid]){
                return mid;
            }else if(target > nums[mid]){
                left = mid+1;
            }else{
                right = mid-1;
            }
        }

        return -1;
    }


    @Test
    void test() {
        int[] nums = new int[]{8,9,2,3,4};
        int target = 9;
        System.out.println(search(nums, target));
    }
}
