import org.junit.jupiter.api.Test;

public class Task367 {

    public boolean isPerfectSquare(int num) {
        int left = 1, right = num;
        int res=0;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            long result = 1L* mid * mid;
            if (result == num) {
                return true;
            } else if (result > num) {
                right = mid - 1;

            } else {
                left = mid+1;
                res = mid;
            }

        }
        return false;
    }

    @Test
    void test(){
        System.out.println(isPerfectSquare(4));
    }
}
