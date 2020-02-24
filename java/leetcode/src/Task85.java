import org.junit.jupiter.api.Test;

import java.util.Stack;

public class Task85 {

    public int maximalRectangle(char[][] matrix) {
        if (matrix.length == 0 || matrix[0].length == 0) {
            return 0;
        }

        int m = matrix.length;
        int n = matrix[0].length;

        int res = 0;

        int[][] rows = new int[m][n];
        for (int i = 0; i < m; i++) {
            rows[i][0] = matrix[i][0] - '0';
        }
        for (int i = 0; i < m; i++) {
            for (int j = 1; j < n; j++) {
                rows[i][j] = matrix[i][j] == '1' ? rows[i][j - 1] + 1 : 0;
            }
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int width = rows[i][j];
                int top = i;
                while (top != -1 && rows[top][j] != 0) {
                    width = Math.min(width, rows[top][j]);
                    res = Math.max(res, width * (i - top + 1));
                    --top;
                }
            }
        }

        return res;
    }

    public int maximalRectangle2(char[][] matrix) {
        if (matrix.length == 0 || matrix[0].length == 0) {
            return 0;
        }

        int m = matrix.length;
        int n = matrix[0].length;

        int res = 0;

        int[] dp = new int[n];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                dp[j] = matrix[i][j] == '0' ? 0 : dp[j] + 1;
            }
            res = Math.max(res, largestRectangleArea(dp));
        }

        return res;
    }

    public int largestRectangleArea(int[] heights) {
        if (heights.length == 0) {
            return 0;
        }
        if (heights.length == 1) {
            return heights[0];
        }

        int res = 0;

        Stack<Integer> stack = new Stack<>();

        stack.push(-1);

        for (int i = 0; i < heights.length; i++) {

            while (stack.peek() != -1 && heights[i] < heights[stack.peek()]) {
                res = Math.max(res, heights[stack.pop()] * (i - stack.peek() - 1));
            }
            stack.push(i);

        }

        while (stack.peek() != -1) {
            res = Math.max(res, heights[stack.pop()] * (heights.length - stack.peek() - 1));
        }

        return res;
    }

    public int maximalRectangle3(char[][] matrix) {
        if (matrix.length == 0 || matrix[0].length == 0) {
            return 0;
        }

        int m = matrix.length;
        int n = matrix[0].length;

        int res = 0;

        int[][] dp = new int[n][3];

        for (int i = 0; i < m; i++) {
            int prevLeft = -1,prevRight = n;
            for (int j = 0; j < n; j++) {
                //height
                dp[j][0] = matrix[i][j] == '0' ? 0 : dp[j][0] + 1;
                //left
                if(matrix[i][j] == '0'){
                    prevLeft = j;
                    dp[j][1] = 0;
                }else{
                    dp[j][1] = dp[j][1] == 0 ? j-prevLeft : Math.min(dp[j][1],j-prevLeft);
                }

                //right
                int jr = n - 1 - j;
                if(matrix[i][jr] == '0'){
                    prevRight = jr;
                    dp[jr][2] = 0;
                }else{
                    dp[jr][2] = dp[jr][2] == 0 ? prevRight - jr : Math.min(dp[jr][2],prevRight - jr);
                }

            }
            // update area
            for (int j = 0; j < n; j++) {
                res = Math.max(res, (dp[j][1] + dp[j][2] - 1) * dp[j][0]);
            }

        }

        return res;
    }


    @Test
    void test() {
        char[][] matrix = new char[][]{
                {'1', '0', '1', '0', '0'},
                {'1', '0', '1', '1', '1'},
                {'1', '1', '1', '1', '1'},
                {'1', '0', '0', '1', '0'}
        };
        System.out.println(maximalRectangle3(matrix));

    }

}
