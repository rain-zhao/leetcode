import java.util.*;

public class Task380 {
    //    class RandomizedSet {
//
//        Set<Integer> set = new HashSet<>();
//        Random random = new Random();
//
//        /** Initialize your data structure here. */
//        public RandomizedSet() {
//
//        }
//
//        /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
//        public boolean insert(int val) {
//            return set.add(val);
//        }
//
//        /** Removes a value from the set. Returns true if the set contained the specified element. */
//        public boolean remove(int val) {
//            Random
//            return set.remove(val);
//        }
//
//        /** Get a random element from the set. */
//        public int getRandom() {
//            int iter = random.nextInt(set.size());
//            Iterator<Integer> iterator = set.iterator();
//            for (int i = 0; i < iter ; i++) {
//                iterator.next();
//            }
//            return iterator.next();
//        }
//    }
    class RandomizedSet {

        Map<Integer, Integer> map = new HashMap<>();
        List<Integer> list = new ArrayList<>();
        Random random = new Random();

        /**
         * Initialize your data structure here.
         */
        public RandomizedSet() {

        }

        /**
         * Inserts a value to the set. Returns true if the set did not already contain the specified element.
         */
        public boolean insert(int val) {
            if (map.containsKey(val)) {
                return false;
            }

            map.put(val, list.size());
            list.add(val);
            return true;
        }

        /**
         * Removes a value from the set. Returns true if the set contained the specified element.
         */
        public boolean remove(int val) {
            if (!map.containsKey(val)) {
                return false;
            }
            int idx = map.remove(val);
            if (list.size() != idx + 1) {
                int lstVal = list.get(list.size() - 1);
                list.set(idx, lstVal);
                map.put(lstVal, idx);
            }
            list.remove(list.size() - 1);
            return true;
        }

        /**
         * Get a random element from the set.
         */
        public int getRandom() {
            return list.get(random.nextInt(list.size()));
        }
    }
}
