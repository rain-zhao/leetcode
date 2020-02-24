import org.junit.jupiter.api.Test;
import sun.jvm.hotspot.debugger.win32.coff.TestDebugInfo;

import java.util.*;
import static org.junit.jupiter.api.Assertions.assertEquals;


public class Task51 {

    List<List<String>> res = new ArrayList<>();
    int n;
    public List<List<String>> solveNQueens(int n) {
        this.n = n;

        solve(0,new ArrayList<>(),new HashSet<>(),new HashSet<>(),new HashSet<>());

        return res;
    }

    void solve(int i, List<String> list, Set<Integer> p,Set<Integer> q,Set<Integer> r){
        //terminate
        if(i == n){
            res.add(list);
            return;
        }
        for (int j = 0; j < n; j++) {
            if(!p.contains(j) && !q.contains(i+j) && !r.contains(i-j)){
                List<String> tempList = new ArrayList<>(list);
                Set<Integer> tempP = new HashSet<>(p);
                Set<Integer> tempQ = new HashSet<>(q);
                Set<Integer> tempR = new HashSet<>(r);
                //add to list
                StringBuilder sb = new StringBuilder();
                for (int k = 0; k < n; k++) {
                    if(k ==j){
                        sb.append('Q');
                    }else{
                        sb.append('.');
                    }
                }
                tempList.add(sb.toString());
                //put into set
                tempP.add(j);
                tempQ.add(i+j);
                tempR.add(i-j);

                solve(i+1,tempList,tempP,tempQ,tempR);

            }
        }
    }

    @Test
    public void test(){
        System.out.println(solveNQueens(4));
    }
}
