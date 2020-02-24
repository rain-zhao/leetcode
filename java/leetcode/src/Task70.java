import org.junit.jupiter.api.Test;

public class Task70 {
    public int climbStairs(int n) {

        int[] path = new int[n+1];
        path[0]=1;
        path[1]=1;

        for (int i = 2; i < n+1; i++) {
            path[i] = path[i-1]+path[i-2];
        }
        return path[n];
    }

    @Test
    void test(){
        System.out.println(climbStairs(3));
    }
}
