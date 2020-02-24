import org.junit.jupiter.api.Test;

public class Task48 {
    public void rotate(int[][] matrix) {
        if(matrix.length < 2){
            return;
        }
        int max = matrix.length-1;
        for (int i = 0; i <= max/2; i++) {
            for (int j = i; j <= max-1-i; j++) {
                int m1 = i,n1=j;
                for (int k = 0; k < 3; k++) {
                    int m2=max-n1,n2=m1;
                    //swap
                    swap(matrix,m1,n1,m2,n2);
                    //iter
                    m1=m2;
                    n1=n2;
                }
            }
        }

    }

    void swap(int[][] matrix,int m1,int n1,int m2,int n2){
        if(matrix[m1][n1] == matrix[m2][n2]){
            return;
        }
        matrix[m1][n1] = matrix[m1][n1]^matrix[m2][n2];
        matrix[m2][n2] = matrix[m1][n1]^matrix[m2][n2];
        matrix[m1][n1] = matrix[m1][n1]^matrix[m2][n2];
    }




    @Test
    void test() {
        int[][] matrix = new int[][]{{5,1,9,11},{2,4,8,10},{13,3,6,7},{15,14,12,16}};
        System.out.println(matrix);
        rotate(matrix);
        System.out.println(matrix);
    }
}
