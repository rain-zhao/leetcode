import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Task118 {
    public List<List<Integer>> generate(int numRows) {
        if (numRows == 0) {
            return Collections.emptyList();
        }

        List<List<Integer>> res = new ArrayList<>(numRows);
        res.add(Collections.singletonList(1));
        if (numRows == 1) {
            return res;
        }
        for (int i = 1; i < numRows; i++) {
            List<Integer> pre = res.get(i-1);

            List<Integer> cur = new ArrayList<>(i+1);
            cur.add(1);
            for (int j = 0; j < i-1; j++) {
                cur.add(pre.get(j)+pre.get(j+1));
            }
            cur.add(1);
            res.add(cur);
        }

        return res;
    }

    @Test
    void test(){
//        int num = 5;
//        System.out.println(generate(num));
        System.out.println('A'-'a');
    }


}
