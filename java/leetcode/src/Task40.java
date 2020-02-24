import org.junit.jupiter.api.Test;

import java.util.*;

public class Task40 {
    //dfs
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        if (candidates.length == 0) {
            return Collections.emptyList();
        }

        Arrays.sort(candidates);
        List<List<Integer>> resList = new ArrayList<>();

        dfs(candidates,0,target,resList,new ArrayList<>());

        return resList;
    }

    private void dfs(int[] candidates, int idx, int target, List<List<Integer>> resList,List<Integer> res) {
        //terminator
        if(target == 0){
            resList.add(new ArrayList<>(res));
            return;
        }
        if(idx == candidates.length){
            return;
        }

        for (int i = idx; i < candidates.length; i++) {
            if(i != idx && candidates[i-1] == candidates[i]){
                continue;
            }

            int remain = target-candidates[i];
            if(remain < 0){
                break;
            }
            res.add(candidates[i]);
            dfs(candidates,i+1,remain,resList,res);
            res.remove(res.size()-1);

        }

    }


    @Test
    void test() {
        int[] candidates = new int[]{10, 1, 2, 7, 6, 1, 5};
        int target = 8;
        System.out.println(combinationSum2(candidates, target));
    }
}
