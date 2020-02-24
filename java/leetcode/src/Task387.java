import org.junit.jupiter.api.Test;

public class Task387 {
    public int firstUniqChar(String s) {
        int[] cnt = new int[123];
        char[] chars = s.toCharArray();

        for (char c : chars) {
            ++cnt[c];
        }
        for (int i = 0; i < chars.length; i++) {
            if(cnt[chars[i]] == 1){
                return i;
            }
        }

        return -1;
    }

    @Test
    void test(){
        String s = "loveleetcode";
        System.out.println(firstUniqChar(s));
    }
}
