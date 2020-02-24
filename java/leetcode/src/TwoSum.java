import java.util.HashMap;
import java.util.Map;
import java.util.stream.Stream;

public class TwoSum {

    public static int[] twoSum(int[] nums, int target) {
        Map<Integer,Integer> map = new HashMap();
        for(int i = 0;i<nums.length;++i){
            int num = nums[i];
            if(map.containsKey(num)){
                return new int[]{map.get(num),i};
            }
            map.put(target-num,i);
        }
        return null;

    }

    public static void main(String[] args) {
        int[] nums = new int[]{2,7,11,15};
        int target = 9;
        System.out.println(twoSum(nums,target));
    }
}
