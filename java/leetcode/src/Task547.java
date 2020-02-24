import org.junit.jupiter.api.Test;

import java.rmi.MarshalException;

public class Task547 {
//    public int findCircleNum(int[][] M) {
//        int l = M.length;
//        if(l == 0){
//            return 0;
//        }
//
//        QuickUnionUF uf = new QuickUnionUF(l);
//        int res = l;
//
//        for (int i = 1; i < l; i++) {
//            for (int j = 0; j < i; j++) {
//                if(M[i][j] == 1 && !uf.connected(i,j)){
//                    uf.union(i,j);
//                    --res;
//                }
//            }
//        }
//
//        return res;
//    }

    int res=0;
    //dfs
    public int findCircleNum(int[][] M) {
        int l = M.length;
        if(l < 2){
            return l;
        }

        int[] mark = new int[l];

        for (int i = 0; i < l; i++) {
            if(mark[i] == 0){
                ++res;
                dfs(M,i,mark);
            }
        }

        return res;
    }

    void dfs(int[][] M,int i,int[] mark){
        mark[i] = 1;
        for (int j = 0; j < M.length; j++) {
            if(M[i][j] ==1 && mark[j] ==0){
                dfs(M,j,mark);
            }
        }
    }

    @Test
    void test(){
        int[][]grid = new int[][]{{1,1,0},{1,1,0},{0,0,1}};
        System.out.println(findCircleNum(grid));
    }


}
