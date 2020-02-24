import org.junit.jupiter.api.Test;

public class Task150 {
    int len;
    String[] tokens;

    public int evalRPN(String[] tokens) {
        len = tokens.length - 1;
        this.tokens = tokens;
        return recur();
    }

    private int recur() {
        if (tokens[len].equals("+") || tokens[len].equals("-") || tokens[len].equals("*") || tokens[len].equals("/")) {
            String token = tokens[len--];
            int num1 = recur();
            int num2 = recur();
            switch (token) {
                case "+":
                    return num2 + num1;
                case "-":
                    return num2 - num1;
                case "*":
                    return num2 * num1;
                case "/":
                    return num2 / num1;
                default:
                    return 0;
            }
        } else {
            return Integer.valueOf(tokens[len--]);
        }

    }


    @Test
    void test() {
        String[] tokens = new String[]{"4", "13", "5", "/", "+"};
        System.out.println(evalRPN(tokens));
    }

}
