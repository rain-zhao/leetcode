import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Task18 {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        List<List<Integer>> res = new ArrayList<>();

        if (nums.length < 4) {
            return res;
        }

        Arrays.sort(nums);
        for (int i = 0; i < nums.length - 3; i++) {
            for (int j = i + 1; j < nums.length - 2; j++) {
                int k = j + 1, l = nums.length - 1;
                while (k < l) {
                    int sum = nums[i] + nums[j] + nums[k] + nums[l];
                    if (sum == target) {
                        res.add(Arrays.asList(nums[i], nums[j], nums[k], nums[l]));
                        while (l-1 > k && nums[l] == nums[l-1]){
                            --l;
                        }
                        --l;
                        while (k+1 < l && nums[k] == nums[k+1]){
                            ++k;
                        }
                        ++k;
                    } else if (sum > target) {
                        while (l-1 > k && nums[l] == nums[l-1]){
                            --l;
                        }
                        --l;
                    } else {
                        while (k+1 < l && nums[k] == nums[k+1]){
                            ++k;
                        }
                        ++k;
                    }
                }

                while( j+1 < nums.length - 2 && nums[j] == nums[j+1]){
                    ++j;
                }
            }
            while( i+1 < nums.length - 3 && nums[i] == nums[i+1]){
                ++i;
            }
        }


        return res;
    }

    @Test
    void test(){
        int[] nums = new int[]{1, 0, -1, 0, -2, 2};
        int target = 0;
        System.out.println(fourSum(nums,target));
    }
}
