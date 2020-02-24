import org.junit.jupiter.api.Test;

import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Task139 {
    public boolean wordBreak(String s, List<String> wordDict) {
        if (wordDict.size() == 0) {
            return s.length() == 0;
        }

        //put dict into set
        Set<String> set = new HashSet<>(wordDict);

        //define
        boolean[] dp = new boolean[s.length() + 1];
        dp[0] = true;
        //init

        //loop
        for (int i = 1; i <= s.length(); i++) {
            for (int j = i - 1; j >= 0; j--) {
                String subStr = s.substring(j, i);
                if (set.contains(subStr) && dp[j]) {
                    dp[i] = true;
                }
            }

        }

        return dp[s.length()];
    }


    @Test
    void test() {
        String s = "leetcode";
        List<String> wordDict = Arrays.asList("leet", "tcode");

        System.out.println(wordBreak(s, wordDict));
    }
}
