import org.junit.jupiter.api.Test;

public class CountPath {

    int countPath(int[][] map) {
        int m = map.length;
        int n = map[0].length;

        //init
        //default 0
        int[][] path = new int[m+1][n+1];
        path[0][1] = 1;


        for (int i = 1; i < m+1; i++) {
            for (int j = 1; j < n+1; j++) {
                if(map[i-1][j-1] == 1){
                    path[i][j] = 0;
                }
                else{
                    path[i][j] = path[i-1][j]+path[i][j-1];
                }
            }
        }
        return path[m][n];
    }


    @Test
    void test() {
        int[][] map = new int[][]{  {0, 0, 0, 0, 0, 0, 0, 0},
                                    {0, 0, 1, 0, 0, 0, 1, 0},
                                    {0, 0, 0, 0, 1, 0, 0, 0},
                                    {1, 0, 1, 0, 0, 1, 0, 0},
                                    {0, 0, 1, 0, 0, 0, 0, 0},
                                    {0, 0, 0, 1, 1, 0, 1, 0},
                                    {0, 1, 0, 0, 0, 1, 0, 0},
                                    {0, 0, 0, 0, 0, 0, 0, 0}
                                  };
        System.out.println(countPath(map));

    }
}
