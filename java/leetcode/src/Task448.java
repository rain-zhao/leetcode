import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.List;

public class Task448 {
    //1.hash
    //2.array

    public List<Integer> findDisappearedNumbers(int[] nums) {
        List<Integer> res = new ArrayList<>();
        if(nums.length < 2){
            return res;
        }

        int[] cnt = new int[nums.length+1];
        for (int num : nums) {
            ++cnt[num];
        }

        for (int i = 1; i < cnt.length; i++) {
            if(cnt[i] == 0){
                res.add(i);
            }
        }

        return res;
    }

    public List<Integer> findDisappearedNumbers2(int[] nums) {
        List<Integer> res = new ArrayList<>();
        if(nums.length < 2){
            return res;
        }
        int len = nums.length;

        for (int num : nums) {
            nums[(num-1)%len] +=len;
        }

        for (int i = 0; i < len; i++) {
            if(nums[i] <= len){
                res.add(i+1);
            }
        }

        return res;
    }

    @Test
    void test(){
        int[] nums = new int[]{4,3,2,7,8,2,3,1};
        System.out.println(findDisappearedNumbers2(nums));
    }
}
