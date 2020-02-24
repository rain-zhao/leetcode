import org.junit.jupiter.api.Test;

public class Task14 {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 0) {
            return "";
        }

        String str = strs[0];
        int idx;
        for (idx = 0; idx < str.length(); idx++) {
            boolean same = true;
            for (String s : strs) {
                if (s.length() < idx + 1 || s.charAt(idx) != str.charAt(idx)) {
                    same = false;
                    break;
                }
            }
            if (!same) {
                break;
            }
        }

        return str.substring(0, idx);
    }

    public String longestCommonPrefix2(String[] strs) {
        if (strs.length == 0) {
            return "";
        }
        if (strs.length == 1) {
            return strs[0];
        }

        String str = strs[0];
        int left = 0, right = str.length() - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            String prefix = str.substring(0, mid + 1);
            boolean same = true;
            for (String s : strs) {
                if (!s.startsWith(prefix)) {
                    same = false;
                    break;
                }
            }
            if (same) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }


        return str.substring(0,left);
    }


    @Test
    void test() {
        String[] strs = new String[]{"flower","flow","flight"};
        System.out.println(longestCommonPrefix2(strs));
    }
}
