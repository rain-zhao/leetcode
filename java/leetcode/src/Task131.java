import org.junit.jupiter.api.Test;

import java.util.*;

public class Task131 {
    public List<List<String>> partition(String s) {
        if (s == null || s.length() == 0) {
            return Collections.emptyList();
        }

        int len = s.length();
        boolean[][] dp = new boolean[len][len];
        for (int i = 0; i < len - 1; i++) {
            dp[i][i] = true;
            dp[i][i + 1] = s.charAt(i) == s.charAt(i + 1);
        }
        dp[len - 1][len - 1] = true;
        for (int k = 3; k <= len; k++) {
            for (int i = 0; i <= len-k; i++) {
                int j= i+k-1;
                dp[i][j] = dp[i+1][j-1] && s.charAt(i)==s.charAt(j);
            }
        }

        Map<String, List<List<String>>> map = new HashMap<>();

        return dfs(s, 0, map,dp);

    }

    List<List<String>> dfs(String s, int beg, Map<String, List<List<String>>> map,boolean[][] dp) {
        if(beg == s.length()){
            List<List<String>> list = new ArrayList<>();
            list.add(Collections.emptyList());
            return list;
        }
        if (map.containsKey(s.substring(beg))) {
            return map.get(s.substring(beg));
        }

        List<List<String>> list = new ArrayList<>();
        for (int i = beg; i < s.length(); i++) {
            if(dp[beg][i]){
                String subStr = s.substring(beg,i+1);
                for (List<String> l : dfs(s,i+1,map,dp)) {
                    List<String> subList = new ArrayList<>();
                    subList.add(subStr);
                    subList.addAll(l);
                    list.add(subList);
                }
            }
        }
        map.put(s.substring(beg),list);

        return map.get(s.substring(beg));
    }


    @Test
    void test() {
        String s = "cbbbcc";
        System.out.println(partition(s));
    }
}
