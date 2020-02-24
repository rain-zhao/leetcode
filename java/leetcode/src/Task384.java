import org.junit.jupiter.api.Test;

import java.util.Random;

public class Task384 {
    class Solution {

        int[] nums;
        int[] random;
        int len;

        Random seed = new Random();

        public Solution(int[] nums) {
            this.nums = nums;
            random = nums.clone();
            len = nums.length;
        }

        /**
         * Resets the array to its original configuration and return it.
         */
        public int[] reset() {
            return nums;
        }

        /**
         * Returns a random shuffling of the array.
         */
        public int[] shuffle() {
            for (int i = 1; i < random.length; i++) {
                int j= seed.nextInt(i+1);
                int tmp =  random[i];
                random[i] = random[j];
                random[j] = tmp;
            }
            return random;
        }
    }

    @Test
    void test(){
        int[] nums = new int[]{1,2,3};
        Solution solution = new Solution(nums);
        solution.reset();
        int[] random = solution.shuffle();
        solution.reset();
        int[] random2 = solution.shuffle();
    }
}
