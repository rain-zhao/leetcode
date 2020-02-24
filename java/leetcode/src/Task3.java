import org.junit.jupiter.api.Test;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class Task3 {
    //dfs O(n2)
    public int lengthOfLongestSubstring(String s) {
        if(s==null || s.length() == 0){
            return 0;
        }

        int res = 0;
        for (int i = 0; i < s.length(); i++) {
            res = Math.max(res,dfs(s,i,new HashSet<>(),0));
        }

        return res;
    }

    int dfs(String s, int idx, Set<Character> set,int res){
        //terminator
        if(s.length() == idx || set.contains(s.charAt(idx))){
            return res;
        }

        //process
        set.add(s.charAt(idx));

        //recursion
        return dfs(s, idx+1,set,res+1);

        //reverse no need

    }

    //dp
    public int lengthOfLongestSubstring2(String s) {
        if(s==null || s.length() == 0){
            return 0;
        }

        int res = 1;
        //define
        int[] dp = new int[s.length()];
        Map<Character,Integer> map = new HashMap<>();

        //init
        dp[0] = 1;
        map.put(s.charAt(0),0);


        for (int i = 1; i < s.length() ; i++) {
            char c = s.charAt(i);
            if(map.containsKey(c)){
                dp[i] = Math.min(dp[i-1]+1,i-map.get(c));
            }else{
                dp[i] = dp[i-1]+1;
            }
            map.put(c,i);
            res = Math.max(dp[i],res);
        }


        return res;
    }

    //sliding window
    public int lengthOfLongestSubstring3(String s) {
        if(s==null || s.length() == 0){
            return 0;
        }
        int res = 1;


        Map<Character,Integer> map = new HashMap<>();
        int i=0,j = 0;

        while(j< s.length()){
            char c = s.charAt(j);
            int length;
            if(map.containsKey(c)){
                i = Math.max(i,map.get(c)+1);
            }

            map.put(c,j);
            res = Math.max(res,j-i+1);

            ++j;
        }


        return res;
    }

    //sliding window
    public int lengthOfLongestSubstring4(String s) {
        if(s==null || s.length() == 0){
            return 0;
        }
        int res = 0;


        int[] cnt = new int[128];

        int left = 0,right=0;

        while(right < s.length()){
            char c = s.charAt(right);
            ++cnt[c];
            ++right;

            while(cnt[c] == 2){
                --cnt[s.charAt(left)];
                ++left;
            }

            res = Math.max(res,right-left);

        }

        return res;
    }

    @Test
    void test(){
        String s = "abcabcbb";
        System.out.println(lengthOfLongestSubstring3(s));
    }


}
