import org.junit.jupiter.api.Test;

public class Task221 {
    public int maximalSquare(char[][] matrix) {
        if (matrix.length == 0) {
            return 0;
        }

        int diameter = 0;

        int m = matrix.length;
        int n = matrix[0].length;

        int[][] res = new int[m][n];

        for (int i = 0; i < m; i++) {
            if(matrix[i][0] == '1'){
                diameter = 1;
            }
            res[i][0] = matrix[i][0] - '0';
        }

        for (int i = 0; i < n; i++) {
            if(matrix[0][i] == '1'){
                diameter = 1;
            }
            res[0][i] = matrix[0][i] - '0';
        }

        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if(matrix[i][j] == '1'){
                    res[i][j] = Math.min(Math.min(res[i-1][j],res[i][j-1]),res[i-1][j-1])+1;
                    diameter = Math.max(diameter,res[i][j]);
                }
            }
        }

        return diameter * diameter;
    }


    @Test
    void test() {
        char[][] matrix = new char[][]{
                {'1', '0', '1', '0', '0'},
                {'1', '0', '1', '1', '1'},
                {'1', '1', '1', '1', '1'},
                {'1', '0', '0', '1', '0'}
        };

        System.out.println(maximalSquare(matrix));
    }
}
