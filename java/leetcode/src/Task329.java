import org.junit.jupiter.api.Test;

public class Task329 {

    int[] dx = new int[]{1, -1, 0, 0};
    int[] dy = new int[]{0, 0, 1, -1};

    public int longestIncreasingPath(int[][] matrix) {
        if (matrix.length == 0 || matrix[0].length == 0) {
            return 0;
        }
        int m = matrix.length;
        int n = matrix[0].length;

        int max = 0;
        int[][] cache = new int[m][n];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                max = Math.max(max, dfs(matrix, i, j, cache));
            }
        }

        return max;

    }

    private int dfs(int[][] matrix, int i, int j, int[][] cache) {
        if (cache[i][j] != 0) {
            return cache[i][j];
        }

        int max = 0;
        for (int k = 0; k < dx.length; k++) {
            int x = i + dx[k];
            int y = j + dy[k];
            if (x >= 0 && x < matrix.length && y >= 0 && y < matrix[0].length && matrix[i][j] < matrix[x][y]) {
                max = Math.max(max, dfs(matrix, x, y, cache));
            }
        }

        cache[i][j] = ++max;
        return max;
    }


    @Test
    void test() {
//        int[][] nums = new int[][]{
//                {9, 9, 4},
//                {6, 6, 8},
//                {2, 1, 1}
//        };

        int[][] nums = new int[][]{
                {0},
                {1},
                {5},
                {5}
        };

        System.out.println(longestIncreasingPath(nums));
    }

}
