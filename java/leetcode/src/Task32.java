import org.junit.jupiter.api.Test;

import java.util.Stack;

public class Task32 {
    public int longestValidParentheses(String s) {

        if (s == null || s.length() == 0) {
            return 0;
        }

        int res = 0;

        Stack<Integer> stack = new Stack();
        stack.push(-1);

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '(') {
                stack.push(i);
            } else {
                stack.pop();
                if (stack.isEmpty()) {
                    stack.push(i);
                } else {
                    res = Math.max(res, i - stack.peek());
                }
            }
        }

        return res;
    }

    public int longestValidParentheses2(String s) {

        int res = 0;

        int left = 0, right = 0;

        for (char c : s.toCharArray()) {
            if (c == '(') {
                ++left;
            } else {
                ++right;
                if (left == right) {
                    res = Math.max(left + right, res);
                } else if (right > left) {
                    left = right = 0;
                }
            }
        }

        left = right = 0;
        for (int i = s.length() - 1; i >= 0; --i) {
            char c = s.charAt(i);
            if (c == ')') {
                ++right;
            } else {
                ++left;
                if (left == right) {
                    res = Math.max(left + right, res);
                } else if (right < left) {
                    left = right = 0;
                }
            }
        }

        return res;
    }


    //dp
    public int longestValidParentheses3(String s) {

        int res = 0;
        int[] dp = new int[s.length()];

        for (int i = 1; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == ')') {
                char c1 = s.charAt(i - 1);
                if (c1 == '(') {
                    dp[i] = (i - 2 >= 0 ? dp[i-2]:0) + 2;
                } else if ((i - dp[i - 1] - 1) >= 0 && s.charAt(i - dp[i - 1] - 1) == '(') {
                    dp[i] = dp[i - 1] + 2 + ((i - dp[i - 1] - 2) >=0 ?dp[i - dp[i - 1] - 2] : 0);
                }
               res = Math.max(res,dp[i]);
            }
        }
        return res;
    }


    @Test
    void test() {
        String s = "(()())";
        System.out.println(longestValidParentheses3(s));
    }
}
