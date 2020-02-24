import org.junit.jupiter.api.Test;

public class Task29 {
    public int divide(int dividend, int divisor) {
        if (dividend == Integer.MIN_VALUE && divisor == -1) {
            return Integer.MAX_VALUE;
        }

        int sign = dividend < 0 && divisor > 0 || dividend > 0 && divisor < 0 ? -1 : 1;
        long up=Math.abs((long) dividend);
        long down=Math.abs((long) divisor);

        int res = 0;
        int shift = 0;

        while(up > down){
            down<<=1;
            ++shift;
        }
        for (; shift  >= 0 ; --shift) {
           if(up >= down) {
               up -= down;
               res+= (1<<shift);
           }
           down >>=1;
        }

        return res*sign;
    }


    @Test
    void test() {
        int dividend = Integer.MIN_VALUE, divisor = 1;
        System.out.println(divide(dividend,divisor));
    }
}
