import org.junit.jupiter.api.Test;

public class Fib {
    int fib(int n) {
        if (n <= 1){
            return n;
        }

        int[] opt = new int[n+1];
        opt[0]=0;
        opt[1]=1;
        for (int i = 2; i <= n; i++) {
            opt[i] =  opt[i-1]+ opt[i-2];
        }
        return opt[n];
    }

    @Test
    void test(){
        System.out.println(fib(2));
    }
}
