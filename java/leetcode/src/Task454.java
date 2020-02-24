import org.junit.jupiter.api.Test;

import java.util.HashMap;
import java.util.Map;

public class Task454 {
    public int fourSumCount(int[] A, int[] B, int[] C, int[] D) {
        int n = A.length;
        if(n == 0){
            return 0;
        }
        Map<Integer,Integer> map = new HashMap<>();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int sum = -A[i]-B[j];
                map.put(sum,map.getOrDefault(sum,0)+1);
            }
        }

        int cnt = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                cnt +=map.getOrDefault(C[i]+D[j],0);
            }
        }

        return cnt;
    }

    @Test
    void test(){
        int[] A = new int[]{ 1, 2};
        int[] B = new int[]{-2,-1};
        int[] C = new int[]{-1, 2};
        int[] D = new int[]{ 0, 2};
        System.out.println(fourSumCount(A,B,C,D));
    }

}
