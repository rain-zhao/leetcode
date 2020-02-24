import org.junit.jupiter.api.Test;

public class Task66 {
    public int[] plusOne(int[] digits) {
        if (digits.length == 0) {
            return digits;
        }

        int carry = 1;
        int cur = digits.length - 1;
        while (carry == 1) {
            if (cur == -1) {
                int[] newDigits = new int[digits.length + 1];
                newDigits[0] = 1;
                System.arraycopy(digits, 0, newDigits, 1, digits.length);
                digits = newDigits;
                break;
            }

            carry = digits[cur] == 9 ? 1 : 0;
            digits[cur] = (digits[cur] +1)%10;

            -- cur;
        }

        return digits;
    }


    @Test
    void test(){
        int[] digits = new int[]{9,9,9};
        System.out.println(plusOne(digits));
    }


}
