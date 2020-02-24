import org.junit.jupiter.api.Test;

public class Task191 {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        int cnt = 0;
        while(n !=0){
            ++cnt;
            n&=n-1;
        }

        return cnt;
    }

    @Test
    void test(){
        System.out.println(hammingWeight(0b11111111111111111111111111111101));
    }
}
