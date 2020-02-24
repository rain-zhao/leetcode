import org.junit.jupiter.api.Test;

import java.util.HashSet;
import java.util.Set;

public class Task128 {
    public int longestConsecutive(int[] nums) {
        if(nums.length < 2){
            return nums.length;
        }

        Set<Integer> set = new HashSet<>();
        for (int num : nums) {
            set.add(num);
        }

        int res = 1;

        for (Integer num : set) {
            if(!set.contains(num-1)){
                int cur = 1;
                while(set.contains(num+cur)){
                    ++cur;
                }
                res = Math.max(res,cur);
            }
        }

        return res;
    }

    @Test
    void test(){
        int[] nums = new int[]{100, 4, 200, 1, 3, 2};
        System.out.println(longestConsecutive(nums));
    }
}
