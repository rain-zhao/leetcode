import org.junit.jupiter.api.Test;

import java.util.HashSet;
import java.util.Set;

public class Task136 {
    public int singleNumber(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for(int num:nums){
            if(set.contains(num)){
                set.remove(num);
            }else {
                set.add(num);
            }
        }
        return set.iterator().next();
    }

    public int singleNumber2(int[] nums) {
        int res =0;

        for (int num : nums) {
            res ^=num;
        }

        return res;
    }

    @Test
    void test(){
        int[] nums = new int[]{4,1,2,1,2};
        System.out.println(singleNumber2(nums));
    }

}
