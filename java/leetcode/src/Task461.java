import org.junit.jupiter.api.Test;

public class Task461 {
    public int hammingDistance(int x, int y) {
        int val = x^y;
        int res = 0;
        while(val != 0){
            val = val & (val-1);
            ++res;
        }

        return res;
    }

    @Test
    void test(){
        int x = 1;
        int y = 4;
        System.out.println(hammingDistance(x,y));
    }
}
