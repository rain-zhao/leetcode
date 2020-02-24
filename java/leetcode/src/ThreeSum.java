import java.util.*;

public class ThreeSum {

    public static List<List<Integer>> threeSum(int[] nums) {
        List res = new ArrayList();
        if(nums.length < 3){
            return res;
        }

        Map<Integer,Map<Integer,Integer>> resMap = new HashMap<>();

        Arrays.sort(nums);

        for (int i = 0; i < nums.length-2; i++) {
            //same node contiue
            if(i > 0 && nums[i]==nums[i-1]){
                continue;
            }
            Set<Integer> set = new HashSet<>();

            for (int j = i+1; j < nums.length; j++) {
                if(set.contains(nums[j])){
                    if(!resMap.containsKey(nums[i])){
                        resMap.put(nums[i],new HashMap<>());
                    }
                    resMap.get(nums[i]).put(-nums[i]-nums[j],nums[j]);
                }else{
                    set.add(-nums[i]-nums[j]);
                }
            }
        }

        resMap.forEach((a,map)->{
            map.forEach((b,c)->{
                res.add(Arrays.asList(a,b,c));
            });
        });

        return res;
    }

    //逼近法
    public static List<List<Integer>> threeSum2(int[] nums) {

        List res = new ArrayList();
        if(nums.length < 3){
            return res;
        }

        //sort
        Arrays.sort(nums);

        for (int i = 0; i < nums.length-2; i++) {
            //same node contiue
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }
            int l = i+1,r=nums.length-1;

            while(l < r){

                if(l != i+1 && nums[l] == nums[l-1]){
                    ++l;
                    continue;
                }
                if(r !=nums.length-1 && nums[r] == nums[r+1]){
                    --r;
                    continue;
                }

                int sum = nums[i]+nums[l]+nums[r];

                if(sum > 0){
                    --r;
                    continue;
                }
                if(sum < 0){
                    ++l;
                    continue;
                }

                res.add(Arrays.asList(nums[i],nums[l],nums[r]));
                ++l;
                --r;

            }
        }

        return res;

    }



    public static void main(String[] args) {
        int[] nums = new int[]{-1, 0, 1, 2, -1, -4};
        System.out.println(threeSum(nums));
    }

}
