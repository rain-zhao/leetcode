import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;
import java.util.LinkedList;

public class SlidingWindowMaximum {

    public static int[] maxSlidingWindow(int[] nums, int k) {

        if(nums == null || k == 0 || nums.length < k){
            return new int[]{};
        }

        Deque<Integer> window = new LinkedList<>();//store index

        int[] res = new int[nums.length-k+1];

        //init window
        window.offer(0);
        res[0]=nums[0];

        for (int i = 1; i < nums.length; i++) {

            // remove item out of index
            if(i-k >= window.peekFirst()){
                window.pollFirst();
            }

            // remove all items lower than current num
            while(!window.isEmpty() && nums[window.peekLast()] <= nums[i]){
                window.pollLast();
            }

            window.offer(i);
            if(i >= k-1){
                res[i-k+1] = nums[window.peekFirst()];
            }
        }

        return res;
    }

    public static void main(String[] args) {
        int[] nums = new int[]{1};
        int k = 1;
        System.out.println(maxSlidingWindow(nums,k));

    }
}
