import java.util.HashMap;
import java.util.Map;

public class Task169 {
//    public static int majorityElement(int[] nums) {
//        Map<Integer,Integer> map = new HashMap<>();
//        for(int num:nums){
//            int cnt = map.getOrDefault(num,0)+1;
//            map.put(num,cnt);
//        }
//
//        int max=0,num=0;
//        for(Map.Entry<Integer,Integer> entry:map.entrySet()){
//            if(entry.getValue() > max) {
//               num = entry.getKey();
//               max = entry.getValue();
//
//            }
//
//        }
//        return num;
//    }

    public static int majorityElement(int[] nums) {
        int res = nums[0],cnt = 0;

        for(int num :nums){
            if(cnt == 0) res = num;
            if(res == num){
                ++cnt;
            }else{
                --cnt;
            }
        }
        return res;
    }

    public static void main(String[] args) {
        int[] nums = new int[]{3,3,4};

        System.out.println(majorityElement(nums));
    }
}
