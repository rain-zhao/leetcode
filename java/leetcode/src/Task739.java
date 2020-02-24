import org.junit.jupiter.api.Test;

import java.util.Stack;

public class Task739 {
    public int[] dailyTemperatures(int[] T) {

        int[] res = new int[T.length];
        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i < T.length; i++) {
            while(!stack.isEmpty() && T[stack.peek()] < T[i]){
                int idx = stack.pop();
                res[idx] = i-idx;
            }
            stack.push(i);
        }

        return res;
    }



    @Test
    void test(){
        int[] T = new int[]{73, 74, 75, 71, 69, 72, 76, 73};
        int[] res = dailyTemperatures(T);
        System.out.println(res);
    }
}
