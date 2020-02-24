import org.junit.jupiter.api.Test;

public class Task69 {

    public int mySqrt(int x) {
        int left = 1, right = x;
        int res=0;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            long result = 1L* mid * mid;
            if (result == x) {
                return mid;
            } else if (result > x) {
                right = mid - 1;

            } else {
                left = mid+1;
                res = mid;
            }

        }
        return res;
    }

    @Test
    void test(){
        System.out.println(mySqrt(2147395599));
    }
}
