import org.junit.jupiter.api.Test;

public class Task240 {
    //binary search
    public boolean searchMatrix(int[][] matrix, int target) {
        if (matrix.length == 0 || matrix[0].length == 0) {
            return false;
        }

        int m = matrix.length;
        int n = matrix[0].length;

        int left,right = n-1;
        for (int i = 0; i < m; i++) {
            left = 0;
            while(left <= right){
                int mid = left + (right-left)/2;
                if(target == matrix[i][mid]){
                    return true;
                }else if (target > matrix[i][mid]){
                    left = mid +1;
                }else{
                    right = mid -1;
                }
            }
        }

        return false;
    }



    //binary search
    public boolean searchMatrix2(int[][] matrix, int target) {
        if (matrix.length == 0 || matrix[0].length == 0) {
            return false;
        }

        int m = matrix.length;
        int n = matrix[0].length;

        return binarySearch(matrix,target,0,m-1,0,n-1);
    }

    public boolean binarySearch(int[][] matrix, int target,int top,int bottom,int left,int right){
        if(left > right || top > bottom){
            return false;
        }
        int colMid = left+(right-left)/2;
        int rowMid = top+(bottom-top)/2;
        if(target == matrix[rowMid][colMid]){
            return true;
        }else if (target < matrix[rowMid][colMid]){
            return binarySearch(matrix,target,top,rowMid-1,left,right)
                    ||binarySearch(matrix,target,rowMid,bottom,left,colMid-1);
        }else{
            return binarySearch(matrix,target,rowMid+1,bottom,left,right)
                    ||binarySearch(matrix,target,top,rowMid,colMid+1,right);
        }

    }

    public boolean searchMatrix3(int[][] matrix, int target) {
        if (matrix.length == 0 || matrix[0].length == 0 ) {
            return false;
        }

        int m = matrix.length;
        int n = matrix[0].length;

        if(matrix[0][0] > target || matrix[m-1][n-1] < target){
            return false;
        }

        int row = 0,col = n-1;
        while(row < m && col >=0){
            if(target == matrix[row][col]){
                return true;
            }else if(target > matrix[row][col]){
                ++row;
            }else{
                --col;
            }
        }
        return false;
    }
    @Test
    void test(){
        int[][] matrix = new int[][]{
                {1,   4,  7, 11, 15},
                {2,   5,  8, 12, 19},
                {3,   6,  9, 16, 22},
                {10, 13, 14, 17, 24},
                {18, 21, 23, 26, 30}
        };
        int target = 5;
        System.out.println(searchMatrix3(matrix,target));
    }


}
