import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Task30 {
    public List<Integer> findSubstring(String s, String[] words) {
        List<Integer> res = new ArrayList<>();

        if (words.length == 0 || s.length() == 0) {
            return res;
        }

        int wordLength = words[0].length();
        int length = words.length;

        if (s.length() < length * wordLength) {
            return res;
        }

        if (wordLength == 0) {
            for (int i = 0; i <= s.length(); i++) {
                res.add(i);
            }
            return res;
        }

        ///////////////////////////////////////////////////////
        Map<String, Integer> referee = new HashMap<>();
        for (String word : words) {
            referee.put(word, referee.getOrDefault(word, 0) + 1);
        }

        for (int i = 0; i <= s.length() - length * wordLength; i++) {
            int cur = i;
            Map<String, Integer> window = new HashMap<>();

            for (; cur + wordLength <= s.length(); cur += wordLength) {
                String word = s.substring(cur, cur + wordLength);
                window.put(word, window.getOrDefault(word, 0) + 1);
                if (referee.getOrDefault(word, 0) < window.get(word)) {
                    break;
                }
            }
            if (cur - i == length * wordLength) {
                res.add(i);
            }

        }

        return res;
    }

    @Test
    void test() {
        String str = "aaaaaaaa";
        String[] words = new String[]{"aa", "aa", "aa"};
        System.out.println(findSubstring(str, words));
    }
}
