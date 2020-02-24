import org.junit.jupiter.api.Test;

public class Task59 {
    public int[][] generateMatrix(int n) {
        int[][] res = new int[n][n];

        int[] dx = new int[]{0, 1, 0, -1};
        int[] dy = new int[]{1, 0, -1, 0};

        int num = n * n;
        int x = 0, y = -1;
        int cur = 0;
        for (int i = 1; i <= num; i++) {
            int tx = x + dx[cur];
            int ty = y + dy[cur];
            if (tx < n && tx >= 0 && ty < n && ty >= 0 && res[tx][ty] == 0) {
                x = tx;
                y = ty;
            } else {
                cur = (cur + 1) % 4;
                x += dx[cur];
                y += dy[cur];
            }
            res[x][y] = i;
        }

        return res;
    }

    @Test
    void test() {
        int n = 3;
        System.out.println(generateMatrix(n));
    }
}
