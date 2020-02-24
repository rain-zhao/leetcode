import org.junit.jupiter.api.Test;

import java.util.*;

public class Task47 {
    public List<List<Integer>> permuteUnique(int[] nums) {
        if (nums.length == 0) {
            return Collections.emptyList();
        }
        List<List<Integer>> res = new ArrayList<>();

        Map<Integer, Integer> cnts = new HashMap<>();
        for (int num : nums) {
            cnts.compute(num, (k, v) -> v == null ? 1 : v + 1);
        }
        int len = nums.length;
        dfs(len,cnts,res,new ArrayList<>());

        return res;
    }

    private void dfs(int len, Map<Integer, Integer> cnts, List<List<Integer>> res, List<Integer> s) {
        if(s.size() == len){
            res.add(new ArrayList<>(s));
            return;
        }

        cnts.forEach((k,v)->{
            if(v != 0){
                cnts.put(k,v-1);
                s.add(k);
                dfs(len,cnts,res,s);
                s.remove(s.size()-1);
                cnts.put(k,v);
            }
        });

    }


    @Test
    void test() {
        int[] nums = new int[]{1, 1, 2};
        System.out.println(permuteUnique(nums));
    }
}
