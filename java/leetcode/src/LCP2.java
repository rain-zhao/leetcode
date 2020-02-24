import org.junit.jupiter.api.Test;

public class LCP2 {
    public int[] fraction(int[] cont) {
        int[] fraction = fraction(cont, 0);
        int gcd = gcd(fraction[0], fraction[1]);
        return new int[]{fraction[0] / gcd, fraction[1] / gcd};
    }

    int[] fraction(int[] cont, int pos) {
        if (pos == cont.length) {
            return new int[]{1, 0};
        }
        int[] fraction = fraction(cont, pos + 1);
        return new int[]{cont[pos] * fraction[0] + fraction[1], fraction[0]};
    }

    int gcd(int x, int y) {
        if (y == 0) {
            return x;
        }
        return gcd(y, x % y);
    }

    public int[] fraction2(int[] cont) {
        int[] res = new int[2];
        res[0] = 1;
        //res[1]=0;

        for (int i = cont.length - 1; i >= 0; i--) {
            int divisor = res[0];
            res[0] = res[0]*cont[i]+res[1];
            res[1] = divisor;
        }

        int gcd = gcd(res[0], res[1]);
        res[0] = res[0]/gcd;
        res[1] = res[1]/gcd;
        return res;
    }

    @Test
    void test() {
        int[] cont = new int[]{3, 2, 0, 2};
        System.out.println(fraction2(cont));
    }

}
