import org.junit.jupiter.api.Test;

import java.util.HashSet;
import java.util.Set;

public class Task260 {
    public int[] singleNumber(int[] nums) {

        int[] res = new int[2];

        Set<Integer> set = new HashSet<>();
        for (int num : nums) {
            if (set.contains(num)) {
                set.remove(num);
            } else {
                set.add(num);
            }
        }

        int i = 0;
        for (Integer integer : set) {
            res[i++] = integer;
        }

        return res;
    }

    public int[] singleNumber2(int[] nums) {

        int[] res = new int[2];

        int xor = 0;

        for (int num : nums) {
            xor ^= num;
        }

        int mask = xor & (-xor);

        for (int num : nums) {
            if ((num & mask) == 0) {
                res[0] ^=num;
            }else{
                res[1] ^=num;
            }
        }

        return res;
    }

    @Test
    void test() {
        int[] nums = new int[]{1, 2, 1, 3, 2, 5};
        System.out.println(singleNumber(nums));
    }
}
