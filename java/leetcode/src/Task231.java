import org.junit.jupiter.api.Test;

public class Task231 {
    public boolean isPowerOfTwo(int n) {
        if(n==0) return false;
        if((n&=(n-1))==0){
            return true;
        }
        return false;
    }

    @Test
    void test(){
        System.out.println(isPowerOfTwo(-2147483648));
    }
}
