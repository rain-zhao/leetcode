import org.junit.jupiter.api.Test;

public class Task172 {
    public int trailingZeroes(int n) {
        int cnt = 0;
        while (n > 0) {
            n = n / 5;
            cnt += n;
        }

        return cnt;
    }

    @Test
    void test(){
        int n = 5;
        System.out.println(trailingZeroes(n));
    }
}
