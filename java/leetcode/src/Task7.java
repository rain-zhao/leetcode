import org.junit.jupiter.api.Test;

public class Task7 {
    public int reverse(int x) {
        if (x == 0) {
            return x;
        }

        long res = 0;

        while(x != 0){
            res = res*10 + x%10;
            x /= 10;
        }

        if(res > Integer.MAX_VALUE || res < Integer.MIN_VALUE){
            return 0;
        }

        return (int)res;
    }

    @Test
    void test() {
        int x = -123;
        System.out.println(reverse(x));
    }
}
