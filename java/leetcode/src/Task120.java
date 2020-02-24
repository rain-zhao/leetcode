import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Task120 {
//    public int minimumTotal(List<List<Integer>> triangle) {
//        int l = triangle.size();
//
//        int[][] map = new int[l+1][l+1];
//
//        for (int i = l-1; i >= 0; i--) {
//            for (int j = i; j >= 0 ; j--) {
//                map[i][j] = Math.min(map[i+1][j],map[i+1][j+1])+triangle.get(i).get(j);
//            }
//        }
//
//        return map[0][0];
//    }

    public int minimumTotal(List<List<Integer>> triangle) {
        int l = triangle.size();

        int[] map = new int[l+1];

        for (int i = l-1; i >= 0; i--) {
            for (int j = 0; j <= i ; j++) {
                map[j] = Math.min(map[j],map[j+1])+triangle.get(i).get(j);
            }
        }

        return map[0];
    }

    @Test
    void test(){
        List<List<Integer>> triangle = new ArrayList<>();
        triangle.add(Arrays.asList(2));
        triangle.add(Arrays.asList(3,4));
        triangle.add(Arrays.asList(6,5,7));
        triangle.add(Arrays.asList(4,1,8,3));


        System.out.println(minimumTotal(triangle));
    }
}
