import org.junit.jupiter.api.Test;

import java.util.HashMap;
import java.util.Map;

public class Task76 {
    public String minWindow(String s, String t) {
        if (s.length() == 0 || t.length() == 0) {
            return "";
        }

        String res = "";

        Map<Character, Integer> needs = new HashMap<>();
        int needCheck = 0;

        for (char c : t.toCharArray()) {
            needs.put(c, needs.getOrDefault(c, 0) + 1);
        }
        needCheck = needs.size();


        int left = 0, right = 0;
        Map<Character, Integer> window = new HashMap<>();
        int valid = 0;

        while(right < s.length()){
            char c = s.charAt(right);
            //add right
            window.put(c,window.getOrDefault(c,0)+1);
            if(window.get(c).equals(needs.get(c))){
                ++valid;
            }
            ++right;
            while(valid == needCheck){
                if(res.equals("") || right - left < res.length() ){
                    res = s.substring(left,right);
                }
                //remove left
                char cl = s.charAt(left);
                window.put(cl,window.get(cl)-1);
                if(needs.containsKey(cl) &&  window.get(cl).equals(needs.get(cl)-1)){
                    --valid;
                }
                ++left;
            }
        }

        return res;
    }


    @Test
    void test() {
        String s = "ADOBECODEBANC";
        String t = "ABC";
        System.out.println(minWindow(s, t));

    }
}
