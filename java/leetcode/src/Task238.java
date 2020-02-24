import java.util.Arrays;

public class Task238 {
    public int[] productExceptSelf(int[] nums) {

        int[] res = new int[nums.length];

        int product = Arrays.stream(nums).reduce(1,(a,b)->a*b);

        for (int i = 0; i < nums.length; i++) {
            res[i] = product/nums[i];
        }

        return res;

    }

    public int[] productExceptSelf2(int[] nums) {
        int[] res = new int[nums.length];

        int product = 1;

        for (int i = 0; i < nums.length; i++) {
            res[i] = product;
            product*=nums[i];
        }

        product = 1;

        for (int i = nums.length - 1; i >= 0; i--) {
            res[i] *= product;
            product*= nums[i];
        }

        return res;
    }

    public static void main(String[] args) {
        int[] nums = new int[]{1,2,3,4};
        Task238 task = new Task238();
        System.out.println(task.productExceptSelf2(nums));
    }

}
