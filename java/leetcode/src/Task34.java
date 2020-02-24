import org.junit.jupiter.api.Test;

public class Task34 {
    public int[] searchRange(int[] nums, int target) {
        int[] res = new int[]{-1, -1};
        if (nums.length == 0) {
            return res;
        }

        int left = 0, right = nums.length - 1;
        //search start idx
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (target > nums[mid]) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        if(left < 0 | left  >= nums.length || nums[left] != target){
            return res;
        }
        res[0] = left;


        right = nums.length - 1;
        //search end idx
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (target >= nums[mid]) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        res[1] = right;

        return res;
    }

    @Test
    void test() {
        int[] nums = new int[]{5, 7, 7, 8, 8, 10};
        int target = 8;
        System.out.println(searchRange(nums, target));
    }
}
