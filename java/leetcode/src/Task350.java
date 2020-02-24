import org.junit.jupiter.api.Test;

import java.util.*;

public class Task350 {
    public int[] intersect(int[] nums1, int[] nums2) {
        List<Integer> res = new ArrayList<>();
        if(nums1.length > nums2.length){
            int[] tmp = nums1;
            nums1 = nums2;
            nums2 = tmp;
        }

        Map<Integer,Integer> map = new HashMap<>();

        for (int i = 0; i < nums1.length; i++) {
            map.put(nums1[i],map.getOrDefault(nums1[i],0)+1);
        }

        for (int i = 0; i < nums2.length; i++) {
            int cnt = map.getOrDefault(nums2[i],0);
            if(cnt > 0){
                res.add(nums2[i]);
                map.put(nums2[i],cnt-1);
            }
        }

        return res.stream().mapToInt(Integer::valueOf).toArray();
    }

    @Test
    void test(){
        int[] nums1 = new int[]{4,9,5};
        int[] nums2 = new int[]{9,4,9,8,4};
        System.out.println(intersect(nums1,nums2));
    }
}
