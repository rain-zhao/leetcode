import org.junit.jupiter.api.Test;

import java.util.*;

public class Task140 {
    public List<String> wordBreak(String s, List<String> wordDict) {
        List<String> res = new ArrayList<>();
        if (wordDict.size() == 0) {
            res.add("");
            return res;
        }
        //put dict into set
        Set<String> set = new HashSet<>(wordDict);
        //define
        List<String> [] dp = new ArrayList[s.length()+1];
        for (int i = 0; i < dp.length; i++) {
            dp[i] = new ArrayList<>();
        }
        //init
        dp[0].add("");

        for (int i = 1; i <= s.length(); i++) {
            for (int j = i-1; j >=0 ; --j) {
                String str = s.substring(j,i);
                if(set.contains(str) && !dp[j].isEmpty()){
                    for (String val : dp[j]) {
                        if(val.equals("")){
                            dp[i].add(str);
                        }else{
                            dp[i].add(val+" "+str);
                        }
                    }
                }
            }
        }

        return dp[s.length()];

    }

    @Test
    void test(){
        String s = "pineapplepenapple";
        List<String> wordDict = Arrays.asList("apple", "pen", "applepen", "pine", "pineapple");
        System.out.println(wordBreak(s,wordDict));

    }
}
