import org.junit.jupiter.api.Test;

public class Task202 {
    public boolean isHappy(int n) {
        if (n == 0) {
            return false;
        }
        int slow = n, fast = turn(n);
        while(slow != fast){
            slow = turn(slow);
            fast = turn(turn(fast));
            if(fast == 1){
                return true;
            }
        }

        return fast == 1;
    }

    int turn(int n) {
        int cur = 0;
        while (n != 0) {
            cur += Math.pow(n % 10, 2);
            n /= 10;
        }
        return cur;
    }

    @Test
    void test() {
        System.out.println(isHappy(1));
    }
}
