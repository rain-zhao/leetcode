import org.junit.jupiter.api.Test;

public class Task38 {
    public String countAndSay(int n) {
        if (n == 1) {
            return "1";
        }
        StringBuilder sb = new StringBuilder();
        String preStr = countAndSay(n - 1);
        int cnt = 1;
        char c = preStr.charAt(0);
        for (int i = 1; i < preStr.toCharArray().length; i++) {
            if (c == preStr.charAt(i)) {
                ++cnt;
            } else {
               sb.append(""+cnt+c);
               c = preStr.charAt(i);
               cnt = 1;
            }
        }

        sb.append(""+cnt+c);

        return sb.toString();
    }

    @Test
    void test() {
        int n = 10;
        System.out.println(countAndSay(n));
    }
}
