import org.junit.jupiter.api.Test;

public class Task162 {
    public int findPeakElement(int[] nums) {
        if(nums.length < 2){
            return 0;
        }
        int len = nums.length;
        if(nums[0] > nums[1]){
            return 0;
        }
        if(nums[len-1] > nums[len-2]){
            return len-1;
        }

        int beg = 0,end = len-1;
        while(beg < end){
            int mid = (beg+end)/2;
            if(nums[mid] < nums[mid+1]){
                beg = mid+1;
            }else{
                end = mid;
            }
        }

        return beg;
    }


    @Test
    void test(){
        int[] nums = new int[]{1,2,3,1};
        System.out.println(findPeakElement(nums));
    }
}
