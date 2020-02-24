import org.junit.jupiter.api.Test;

import java.util.Arrays;

public class Task75 {
    public void sortColors(int[] nums) {
        if (nums.length < 2) {
            return;
        }

        int[] cnt = new int[3];

        for (int i = 0; i < nums.length; i++) {
            ++cnt[nums[i]];
        }

        Arrays.fill(nums, 0, cnt[0], 0);
        Arrays.fill(nums, cnt[0], cnt[0] + cnt[1], 1);
        Arrays.fill(nums, cnt[0] + cnt[1], cnt[0] + cnt[1] + cnt[2], 2);

    }

    public void sortColors2(int[] nums) {
        if (nums.length < 2) {
            return;
        }

        int p0 = 0, p2 = nums.length - 1, cur = 0;

        while (cur <= p2) {

            if (nums[cur] == 0) {
                swap(nums, p0++, cur++);
            }else if (nums[cur] == 1) {
                ++cur;
            }else {
                swap(nums, p2--, cur);
            }

        }
    }

    void swap(int[] nums, int x, int y) {
        if (nums[x] == nums[y]) {
            return;
        }
        nums[x] = nums[x] ^ nums[y];
        nums[y] = nums[x] ^ nums[y];
        nums[x] = nums[x] ^ nums[y];
    }

    @Test
    void test() {
        int[] nums = new int[]{2, 0, 2, 1, 1, 0};
        sortColors2(nums);
        System.out.println(nums);
    }
}
