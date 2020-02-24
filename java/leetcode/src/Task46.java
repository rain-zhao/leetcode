import org.junit.jupiter.api.Test;

import java.util.*;

public class Task46 {
    List<List<Integer>> res=  new ArrayList<>();
    //dfs
    public List<List<Integer>> permute(int[] nums) {
        if(nums.length == 0){
            res.add(new ArrayList<>());
            return res;
        }

        dfs(nums,new ArrayList<>(),new HashSet<>());

        return res;
    }

    private void dfs(int[] nums,ArrayList<Integer> result, Set<Integer> used) {
        //terminator
        if(result.size() == nums.length){
            res.add(new ArrayList<>(result));
        }

        //drill down
        for (int i = 0; i < nums.length; i++) {
            int val = nums[i];
            if(used.contains(val)){
                continue;
            }
            result.add(val);
            used.add(val);
            dfs(nums,result,used);
            used.remove(val);
            result.remove(result.size()-1);
        }

    }

    public List<List<Integer>> permute2(int[] nums) {
        if(nums.length == 0){
            res.add(new ArrayList<>());
            return res;
        }
        Integer[] copy = new Integer[nums.length];
        for (int i = 0; i < nums.length; i++) {
            copy[i] = nums[i];
        }
        recursion(copy,nums.length-1);
        return res;
    }

    private void recursion(Integer[] nums, int idx) {
        if(idx == 0){
            res.add(Arrays.asList(nums.clone()));
        }
        for (int i = idx; i >=0; --i) {
            swap(nums,i,idx);
            recursion(nums, idx-1);
            swap(nums,i,idx);
        }
    }

    private void swap(Integer[] nums, int i, int j) {
        if(i == j){
            return;
        }
        nums[i] = nums[i]^nums[j];
        nums[j] = nums[i]^nums[j];
        nums[i] = nums[i]^nums[j];
    }


    @Test
    void test(){
        int[] nums = new int[]{1,2,3};
        System.out.println(permute2(nums));
    }
}
