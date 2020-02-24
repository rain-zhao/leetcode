import org.junit.jupiter.api.Test;

import java.util.*;

public class Task347 {
    public List<Integer> topKFrequent(int[] nums, int k) {

        Map<Integer,Integer> map = new HashMap<>();

        //put into map
        for (int num : nums) {
            map.put(num,map.getOrDefault(num,0)+1);
        }

        //put into priority queue
        PriorityQueue<Integer> pq = new PriorityQueue<>(Comparator.comparingInt(map::get));

        map.forEach((key,val)->{
            pq.offer(key);
            if(pq.size() > k){
                pq.poll();
            }
        });

        List res = new ArrayList<>(pq);
        Collections.reverse(res);

        return res;
    }

    @Test
    void test(){
        int[] nums = new int[]{1,1,1,2,2,3};
        int k = 2;
        System.out.println(topKFrequent(nums,k));
    }
}
