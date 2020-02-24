import org.junit.jupiter.api.Test;

public class Task189 {
    public void rotate(int[] nums, int k) {
        if (nums.length < 2 || k == 0) {
            return;
        }

        int n = nums.length;

        int cnt = 0;
        for (int i = 0; cnt < n; i++) {
            int pre = nums[i];
            int pos = i;
            do {
                pos = (pos + k) % n;
                int tmp = nums[pos];
                nums[pos] = pre;
                pre = tmp;
                ++cnt;
            } while (i != pos);
        }
    }

    @Test
    void test() {
        int[] nums = new int[]{1, 2, 3, 4, 5, 6};
        int k = 2;
        System.out.println(nums);
        rotate(nums, k);
        System.out.println(nums);
    }
}
