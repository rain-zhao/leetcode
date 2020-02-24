import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.List;

public class Task89 {
    public List<Integer> grayCode(int n) {
        List<Integer> res = new ArrayList<>((int) Math.pow(2, n));
        res.add(0);

        for (int i = 1; i <= n; i++) {
            for (int k = res.size()-1; k >= 0; k--) {
                res.add(1 << (i-1) | res.get(k));
            }
        }

        return res;
    }

    @Test
    void test() {
        int n = 3;
        System.out.println(grayCode(n));
    }
}
