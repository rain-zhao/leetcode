import org.junit.jupiter.api.Test;

import java.util.HashMap;
import java.util.Map;

public class Task560 {

    public int subarraySum(int[] nums, int k) {
        if (nums.length == 0) {
            return 0;
        }

        int cnt = 0;
        int length = nums.length;
        int[] sums = new int[length+1];
        for (int i = 1; i <= length; i++) {
            sums[i] = sums[i-1]+nums[i-1];
        }

        for (int i = 1; i < sums.length; i++) {
            for (int j = 0; j < i; j++) {
                if(sums[i] - sums[j] == k){
                    ++cnt;
                }
            }
        }

        return cnt;
    }


    public int subarraySum2(int[] nums, int k) {
        if (nums.length == 0) {
            return 0;
        }

        int cnt = 0;

        Map<Integer,Integer> map = new HashMap<>();
        map.put(0,1);
        int sum = 0;


        for (int num : nums) {
            sum += num;
            //sum[j] - k = sum[i]
            cnt+=map.getOrDefault(sum-k,0);
            map.put(sum,map.getOrDefault(sum,0)+1);
        }

        return cnt;
    }

    @Test
    void test() {
        int[] nums = new int[]{1,1,1};
        int k = 2;
        System.out.println(subarraySum2(nums, k));
    }


}
