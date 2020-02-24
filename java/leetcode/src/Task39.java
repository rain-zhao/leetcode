import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.List;

public class Task39 {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> res = new ArrayList<>();

        if(candidates.length == 0 ){
            return res;
        }

        if(target <= 0){
            return res;
        }

        dfs(candidates,target,0,res,new ArrayList<>());

        return res;
    }

    private void dfs(int[] candidates, int target, int idx, List<List<Integer>> res,ArrayList<Integer> result) {
        //terminator
        if(target == 0){
            res.add(new ArrayList<>(result));
            return;
        }
        if(target < 0){
            return;
        }

        //drill down
        for (int i = idx; i < candidates.length; i++) {
            int remain = target - candidates[i];
            result.add(candidates[i]);
            dfs(candidates,remain,i,res,result);
            //reverse
            result.remove(result.size()-1);

        }

    }


    @Test
    void test() {
        int[] nums = new int[]{2,3,6,7};
        int target = 7;
        System.out.println(combinationSum(nums, target));
    }
}
