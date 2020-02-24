import org.junit.jupiter.api.Test;

public class Task334 {
    public boolean increasingTriplet(int[] nums) {
        if (nums.length < 3) {
            return false;
        }

        int pivot = 0;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] > nums[pivot]) {
                nums[++pivot] = nums[i];
            } else {
                for (int j = 0; j <= pivot ; j++) {
                    if(nums[i] <= nums[j]){
                        nums[j] = nums[i];
                        break;
                    }

                }
            }

            if (pivot == 2) {
                return true;
            }
        }

        return false;
    }

    public boolean increasingTriplet2(int[] nums) {
        if (nums.length < 3) {
            return false;
        }

        int[] rank = new int[2];
        rank[0] = nums[0];
        rank[1] = Integer.MAX_VALUE;
        for (int i = 0; i < nums.length; i++) {
            if(nums[i] > rank[1]){
                return true;
            }
            for (int j = 1; j < 2; j++) {
                if(nums[i] <= rank[j]){
                    rank[j] = nums[i];
                    break;
                }
            }
        }

        return false;
    }

    @Test
    void test() {
        int[] nums = new int[]{2,1,5,0,3};
        System.out.println(increasingTriplet2(nums));
    }
}
