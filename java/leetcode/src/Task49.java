import org.junit.jupiter.api.Test;

import java.util.*;

public class Task49 {
    public List<List<String>> groupAnagrams(String[] strs) {
        if(strs.length == 0){

            return new ArrayList<>();
        }

        Map<String,List<String>> map = new HashMap<>();
        for (String str : strs) {
            char[] chars = str.toCharArray();
            Arrays.sort(chars);
            String key = String.valueOf(chars);
            if(map.containsKey(key)){
                map.get(key).add(str);
            }else{
                map.put(key, new ArrayList<>(Arrays.asList(str)));
            }
        }
        return new ArrayList<>(map.values());
    }


    final int CHAR_SIZE = 26;
    public List<List<String>> groupAnagrams2(String[] strs) {
        if(strs.length == 0){
            return new ArrayList<>();
        }

        Map<Integer,List<String>> map = new HashMap<>();
        int[] count = new int[26];
        int key;
        for (String str : strs) {
            Arrays.fill(count, 0);
            for (char c : str.toCharArray()) {
                ++count[c-'a'];
            }
            //sum
            key = 0;
            for (int i : count) {
                key*=CHAR_SIZE;
                key +=i;
            }

            if(map.containsKey(key)){
                map.get(key).add(str);
            }else{
                map.put(key, new ArrayList<>(Arrays.asList(str)));
            }

        }

        return new ArrayList<>(map.values());
    }

    @Test
    void test(){
        String[] strs = new String[]{"eat", "tea", "tan", "ate", "nat", "bat"};
        System.out.println(groupAnagrams2(strs));
    }
}
