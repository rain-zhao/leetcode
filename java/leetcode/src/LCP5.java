import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.List;

public class LCP5 {

    class Member {
        List<Member> childs = new ArrayList<>();
        Member parent;
        int total;
    }

    public int[] bonus(int n, int[][] leadership, int[][] operations) {
        Member[] members = new Member[n + 1];
        for (int i = 1; i <= n; i++) {
            members[i] = new Member();
        }
        for (int[] relation : leadership) {
            Member parent = members[relation[0]];
            Member child = members[relation[1]];
            parent.childs.add(child);
            child.parent = parent;
        }

        List<Integer> res = new ArrayList<>();

        for (int[] op : operations) {
            switch (op[0]) {
                case 1:
                    add(members[op[1]], op[2]);
                    break;
                case 2:
                    dfs(members[op[1]], op[2]);
                    break;
                case 3:
                    res.add(members[op[1]].total);
                    break;
            }
        }

        return res.stream().mapToInt(Integer::valueOf).toArray();
    }

    void dfs(Member meb, int coins) {
        for (Member child : meb.childs) {
            dfs(child, coins);
        }
        add(meb, coins);
    }

    void add(Member meb, int coins) {
        while (meb != null) {
            meb.total = (meb.total+ coins)%1000000007;
            meb = meb.parent;
        }
    }

    @Test
    void test() {

        int n = 6;
        int[][] leadership = new int[][]{
                {1, 2}, {1, 6}, {2, 3}, {2, 5}, {1, 4}
        };
        int[][] operations = new int[][]{
                {1, 1, 500}, {2, 2, 50}, {3, 1}, {2, 6, 15}, {3, 1}
        };
        System.out.println(bonus(n, leadership, operations));
    }
}
