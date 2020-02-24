import org.junit.jupiter.api.Test;

public class Task289 {
    public void gameOfLife(int[][] board) {
        if (board.length == 0 || board[0].length == 0) {
            return;
        }
        int m = board.length;
        int n = board[0].length;
        int[] dx = new int[]{-1, -1, -1, 0, 0, 1, 1, 1};
        int[] dy = new int[]{-1, 0, 1, -1, 1, -1, 0, 1};

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] <= 0) {
                    continue;
                }
                for (int k = 0; k < dx.length; k++) {
                    int p = i + dx[k];
                    int q = j + dy[k];
                    if (p >= 0 && p < m && q >= 0 && q < n) {
                        board[p][q] = board[p][q] <= 0 ? board[p][q] - 1 : board[p][q] + 1;
                    }
                }
            }
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] > 0) { //prev live
                    board[i][j] = board[i][j] == 3 || board[i][j] == 4 ? 1 : 0;
                } else {//prev dead
                    board[i][j] = board[i][j] == -3 ? 1 : 0;
                }
            }
        }
    }


    @Test
    void test() {
        int[][] board = new int[][]{
                {0, 1, 0},
                {0, 0, 1},
                {1, 1, 1},
                {0, 0, 0}
        };
        System.out.println(board);
        gameOfLife(board);
        System.out.println(board);
    }
}
