import org.junit.jupiter.api.Test;
import sun.jvm.hotspot.debugger.win32.coff.TestDebugInfo;

import java.util.*;
import static org.junit.jupiter.api.Assertions.assertEquals;


public class Task52 {

//    int res = 0;
//    int n;
//    Set<Integer> p = new HashSet<>();
//    Set<Integer> q = new HashSet<>();
//    Set<Integer> r = new HashSet<>();
//
//    public int solveNQueens(int n) {
//        this.n = n;
//
//        solve(0);
//
//        return res;
//    }
//
//    void solve(int i){
//        //terminate
//        if(i == n){
//            ++res;
//            return;
//        }
//        for (int j = 0; j < n; j++) {
//            if(!p.contains(j) && !q.contains(i+j) && !r.contains(i-j)){
//                //put into set
//                p.add(j);
//                q.add(i+j);
//                r.add(i-j);
//
//                solve(i+1);
//
//                p.remove(j);
//                q.remove(i+j);
//                r.remove(i-j);
//
//            }
//        }
//    }

//#####################################位运算#################
    int res = 0;
    int n;

    public int totalNQueens(int n) {
        this.n = n;

        solve(0,0,0,0);

        return res;
    }

    void solve(int i,int p,int q,int r){
        //terminate
        if(i == n){
            ++res;
            return;
        }

        int bits = (~(p|q|r)) & ((1<<n)-1);

        int bit;
        while((bit=bits&-bits) != 0){
            solve(i+1,p|bit,(q|bit)<<1,(r|bit)>>1);
            bits &=(bits-1);
        }
    }

    @Test
    public void test(){
        System.out.println(totalNQueens(4));
    }
}
