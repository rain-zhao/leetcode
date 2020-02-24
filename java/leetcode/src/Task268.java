import org.junit.jupiter.api.Test;

public class Task268 {
//    public int missingNumber(int[] nums) {
//
//        int n = nums.length;
//        boolean nflag = false;
//        for (int i = 0; i < n; i++) {
//            if(nums[i] % (n+1) == n){
//                nflag = true;
//            }else{
//                nums[nums[i] % (n+1)] +=n+1;
//            }
//        }
//        if(!nflag){
//            return n;
//        }else{
//            for (int i = 0; i < n ; i++) {
//                if(nums[i] < n+1){
//                    return i;
//                }
//            }
//        }
//        return -1;
//    }

    //    public int missingNumber(int[] nums) {
//        int n = nums.length;
//        int expectsum = n*(n+1)/2;
//        int sum = 0;
//        for (int num : nums) {
//            sum+=num;
//        }z
//
//        return expectsum - sum;
//    }
    public int missingNumber(int[] nums) {
        int miss = nums.length;
        for (int i = 0; i < nums.length; i++) {
            miss^=i^nums[i];
        }
        return miss;
    }

    @Test
    void test() {
        int[] nums = new int[]{9, 6, 4, 2, 3, 5, 7, 0, 1};
        System.out.println(missingNumber(nums));

    }
}
