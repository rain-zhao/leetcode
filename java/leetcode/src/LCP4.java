import org.junit.jupiter.api.Test;

import java.util.Arrays;

public class LCP4 {

    int[] delta = {1, 0, -1, 0, 1};

    boolean[] visit;
    int[] board;
    int n;
    int m;


    //backtrack
    public int domino(int n, int m, int[][] broken) {
        if (broken.length == 0) {
            return n * m / 2;
        }

        //init
        visit = new boolean[n * m + 1];
        board = new int[n * m + 1];
        this.n = n;
        this.m = m;
        for (int[] b : broken) {
            board[b[0] * m + b[1] + 1] = -1;
        }

        int res = 0;

        for (int i = 0; i < n; i++) {
            for (int j = i % 2; j < m; j += 2) {
                if (board[i * m + j + 1] == -1) {
                    continue;
                }
                Arrays.fill(visit, false);
                if (find(i, j)) {
                    ++res;
                }
            }
        }

        return res;
    }

    private boolean find(int row, int col) {
        for (int i = 0; i < 4; i++) {
            int x = row + delta[i];
            int y = col + delta[i + 1];
            if (x >= 0 && x < n && y >= 0 && y < m) {
                int pos = x * m + y + 1;
                if (board[pos] == -1 || visit[pos]) {
                    continue;
                }
                visit[pos] = true;
                if (board[pos] == 0 || find((board[pos]-1) / m, (board[pos]-1) % m)) {
                    board[pos] = row * m + col + 1;
                    return true;
                }

            }
        }

        return false;
    }

    @Test
    void test() {
        int n = 8;
        int m = 8;
        int[][] broken = new int[][]{
                {0, 1},
                {2, 0},
                {4, 3},
                {4, 7},
                {5, 4}

        };
//        int n = 2;
//        int m = 3;
//        int[][] broken = new int[][]{
//                {1, 0},
//                {1, 1},
//
//        };
        System.out.println(domino(n, m, broken));
    }


}
