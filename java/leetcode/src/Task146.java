import org.junit.jupiter.api.Test;

import java.util.*;
class Task146{
    class LRUCache {

        LinkedHashMap<Integer,Integer> map;
        int capacity;

        public LRUCache(int capacity) {
            map = new LinkedHashMap<>(capacity, 0.75f,true);
            this.capacity = capacity;
        }

        public int get(int key) {
            return map.getOrDefault(key,-1);
        }

        public void put(int key, int value) {
            map.put(key,value);

            if(map.size() > capacity){
                int removeKey = map.keySet().iterator().next();
                map.remove(removeKey);
            }

        }
        /**
         * Your LRUCache object will be instantiated and called as such:
         * LRUCache obj = new LRUCache(capacity);
         * int param_1 = obj.get(key);
         * obj.put(key,value);
         */



    }

    @Test
    void test(){
        LRUCache cache = new LRUCache(2);
        cache.put(2, 1);
        cache.put(1, 2);
        cache.put(2, 3);
        cache.put(4, 1);
        System.out.println(cache.get(1));
        System.out.println(cache.get(2));

    }
}


