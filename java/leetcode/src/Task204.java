import org.junit.jupiter.api.Test;

public class Task204 {
    public int countPrimes(int n) {
        int cnt = 0;
        boolean[] prime = new boolean[n];
        for (int i = 2; i < n ; i++) {
            if(!prime[i]){
                ++cnt;
                for (int j = 1; j*i < n ; j++) {
                    prime[j*i] = true;
                }
            }
        }

        return cnt;
    }

    @Test
    void test(){
        int n = 2;
        System.out.println(countPrimes(n));
    }
}
