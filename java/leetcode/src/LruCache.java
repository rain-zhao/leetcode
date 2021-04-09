import java.util.HashMap;
import java.util.LinkedList;

public class LruCache {

    private static class Pair{
        private Integer key;
        private Integer val;

        public Pair(Integer key, Integer val) {
            this.key = key;
            this.val = val;
        }

        public Integer getKey() {
            return key;
        }

        public Integer getVal() {
            return val;
        }
    }


    private HashMap<Integer,Pair> map = new HashMap<>();

    private LinkedList<Pair> list = new LinkedList<>();

    private int maxSize;

    public LruCache(int maxSize) {
        this.maxSize = maxSize;
    }

    public Integer get(Integer key){
        if (!map.containsKey(key)){
            return null;
        }

        Pair pair = map.get(key);

        list.remove(pair);

        list.addFirst(pair);

        return pair.getVal();
    }


    public void put(Integer key,Integer val){

        Pair pair = new Pair(key,val);

        if (map.containsKey(key)){
            list.remove(map.get(key));
            map.remove(key);
        }

        map.put(key,pair);
        list.addFirst(pair);

        //over size
        if (list.size() > maxSize){
            Pair last = list.removeLast();
            map.remove(last.getKey());
        }

    }


    public static void main(String[] args) {
        LruCache cache = new LruCache(10);

        cache.put(1,1);
        cache.put(2,2);
        cache.put(3,3);
        cache.put(4,4);
        cache.put(5,5);
        cache.put(6,6);
        cache.put(7,7);
        cache.put(8,8);
        cache.put(9,9);
        cache.put(10,10);


        cache.put(11,11);
        System.out.println(cache.get(1));//none
        System.out.println(cache.get(2));
        cache.put(12,12);
        System.out.println(cache.get(3));//none
        cache.put(13,13);
        System.out.println(cache.get(3));


    }


}
