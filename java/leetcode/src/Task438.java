import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Task438 {
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> res = new ArrayList<>();
        if (s.length() < p.length()) {
            return res;
        }

        int[] cnt = new int[26];
        for (char c : p.toCharArray()) {
            ++cnt[c - 'a'];
        }


        //init
        int[] compareCnt = new int[26];
        for (int i = 0; i < p.length(); i++) {
            ++compareCnt[s.charAt(i) - 'a'];
        }
        if (Arrays.equals(cnt, compareCnt)) {
            res.add(0);
        }

        for (int i = 1; i <= s.length() - p.length(); i++) {
            --compareCnt[s.charAt(i - 1) - 'a'];
            ++compareCnt[s.charAt(i + p.length() - 1) - 'a'];
            if (Arrays.equals(cnt, compareCnt)) {
                res.add(i);
            }
        }

        return res;
    }

    public List<Integer> findAnagrams2(String s, String p) {
        List<Integer> res = new ArrayList<>();
        if (s.length() < p.length()) {
            return res;
        }

        int[] needs = new int[26];
        int needCheck = 0;
        for (char c : p.toCharArray()) {
            ++needs[c - 'a'];
        }
        needCheck = (int) Arrays.stream(needs).filter(val -> val > 0).count();

        int[] window = new int[26];
        int left=0,right=0;
        int valid = 0;

        while(right < s.length()){
            char c = s.charAt(right);
            ++window[c-'a'];
            if(window[c-'a'] == needs[c-'a']){
                ++valid;
            }
            ++right;

            while(valid == needCheck){
                if(right-left == p.length()){
                    res.add(left);
                }
                char cl = s.charAt(left);
                --window[cl-'a'];
                if(window[cl-'a'] == needs[cl-'a']-1){
                    --valid;
                }
                ++left;
            }

        }

        return res;
    }

    @Test
    void test() {
        String s = "cbaebabacd";
        String p = "abc";
        System.out.println(findAnagrams2(s, p));
    }
}
