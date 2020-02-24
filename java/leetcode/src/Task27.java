import org.junit.jupiter.api.Test;

public class Task27 {
    public int removeElement(int[] nums, int val) {
        if(nums.length == 0){
            return 0;
        }
        int idx = 0;
        for (int i = 0; i < nums.length; i++) {
            if(nums[i] != val){
                nums[idx++] = nums[i];
            }
        }
        return idx;
    }

    @Test
    void test(){
        int[] nums = new int[]{0,1,2,2,3,0,4,2};
        int val = 2;
        System.out.println(removeElement(nums,val));
    }
}
