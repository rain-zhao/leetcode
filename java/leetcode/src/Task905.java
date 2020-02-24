import org.junit.jupiter.api.Test;

public class Task905 {
    public int[] sortArrayByParity(int[] A) {
        if (A.length < 2) {
            return A;
        }

        int left = 0, right = A.length - 1;

        while (left < right) {

            if (left < right && (A[left] & 1) == 0) {
                //even
                ++left;
                continue;
            }

            while (left < right && (A[right] & 1) == 1) {
                --right;
            }

            //swap
            int tmp = A[left];
            A[left] =A[right];
            A[right] = tmp;
            ++left;
            --right;

        }

        return A;
    }

    @Test
    void test() {
        int[] a = new int[]{3, 1, 2, 4};
        System.out.println(sortArrayByParity(a));
    }
}
