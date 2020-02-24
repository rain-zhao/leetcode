import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Task54 {
    public List<Integer> spiralOrder(int[][] matrix) {
        if (matrix.length == 0 || matrix[0].length == 0) {
            return Collections.emptyList();
        }

        int m = matrix.length;
        int n = matrix[0].length;

        List<Integer> res = new ArrayList<>(m * n);

        int top = 0, bottom = m - 1, left = 0, right = n - 1;
        
        while(res.size() != m*n){
            for (int i = left; i <= right; i++) {
                res.add(matrix[top][i]);
            }
            ++top;
            for (int i = top; i <= bottom; i++) {
                res.add(matrix[i][right]);
            }
            --right;

            if(res.size() == m*n){
                break;
            }

            for (int i = right; i >= left ; --i) {
                res.add(matrix[bottom][i]);
            }
            --bottom;

            for (int i = bottom; i >= top; --i) {
                res.add(matrix[i][left]);
            }
            ++left;

        }
        
        return res;
    }


    @Test
    void test() {
        int[][] matrix = new int[][]{
                {1, 2, 3, 4},
                {5, 6, 7, 8},
                {9, 10, 11, 12}
        };

        System.out.println(spiralOrder(matrix));
    }
}
