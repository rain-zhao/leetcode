import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Task78 {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();

        if(nums.length == 0){
            res.add(Arrays.asList());
            return res;
        }

        dfs(nums,0,res,new ArrayList<>());


        return res;
    }

    private void dfs(int[] nums, int idx, List<List<Integer>> res, List<Integer> result) {
        if(idx == nums.length){
            res.add(new ArrayList<>(result));
            return;
        }

        dfs(nums,idx+1,res,result);//不选
        result.add(nums[idx]);
        dfs(nums,idx+1,res,result);//选
        result.remove(result.size()-1);

    }


    public List<List<Integer>> subsets2(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();

        if(nums.length == 0){
            res.add(Arrays.asList());
            return res;
        }

        dfs2(nums,0,res,new ArrayList<>());

        return res;
    }

    private void dfs2(int[] nums, int idx, List<List<Integer>> res, List<Integer> result) {
        res.add(new ArrayList<>(result));
        for (int i = idx; i < nums.length; i++) {
            result.add(nums[i]);
            dfs2(nums,i+1,res,result);
            result.remove(result.size()-1);
        }
    }

    public List<List<Integer>> subsets3(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        res.add(Arrays.asList());

        if(nums.length == 0){
            return res;
        }

        for (int num: nums) {
            int size = res.size();
            for (int i = 0; i < size; i++) {
                List<Integer> result = new ArrayList<>(res.get(i));
                result.add(num);
                res.add(result);
            }
        }

        return res;
    }


    @Test
    void test(){
        int[] nums = new int[]{1,2,3};
        System.out.println(subsets3(nums));
    }
}
