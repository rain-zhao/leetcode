import org.junit.jupiter.api.Test;

public class Task43 {
    public String multiply(String num1, String num2) {
        if (num1.equals("0") || num2.equals("0")) {
            return "0";
        }

//        if(num1.length() + num2.length() < 11){
//            return String.valueOf(Integer.valueOf(num1)*Integer.valueOf(num2));
//        }

        if (num1.length() < num2.length()) {
            String tmp = num2;
            num2 = num1;
            num1 = tmp;
        }

        int l1 = num1.length();
        int l2 = num2.length();


        int[] res = new int[l1 + l2];

        for (int i = l2 - 1; i >= 0; --i) {
            int multi = num2.charAt(i) - '0';
            if (multi == 0) {
                continue;
            }
            int carry = 0;
            for (int j = l1 - 1; j >= 0; --j) {
                int bit = num1.charAt(j) - '0';
                int sum = bit * multi + carry+res[i + j + 1];
                carry = sum / 10;
                res[i + j + 1] = sum % 10;

            }
            res[i] = carry;
        }

        StringBuilder sb = new StringBuilder();
        if(res[0] != 0){
            sb.append(res[0]);
        }
        for (int i = 1; i < res.length; i++) {
            sb.append(res[i]);
        }

        return sb.toString();

    }

    @Test
    void test() {
        String num1 = "123456789", num2 = "987654321";
        System.out.println(multiply(num1,num2));
    }
}
