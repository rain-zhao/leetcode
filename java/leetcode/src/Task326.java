public class Task326 {
    public boolean isPowerOfThree(int n) {

        int cur = 3;

        while (cur < n) {
            cur *= 3;
        }

        if (cur == n) {
            return true;
        } else {
            return false;
        }
    }
}
