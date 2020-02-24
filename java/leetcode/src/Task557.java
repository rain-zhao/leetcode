import org.junit.jupiter.api.Test;

import java.util.Stack;

public class Task557 {
    public String reverseWords(String s) {
        if(s.length() < 2){
            return s;
        }

        StringBuilder sb = new StringBuilder();
        Stack<Character> stack = new Stack<>();


        for (char c : s.toCharArray()) {
            if(c == ' '){
                while(!stack.isEmpty()){
                    sb.append(stack.pop());
                }
                sb.append(" ");
            }else{
                stack.push(c);
            }
        }
        while(!stack.isEmpty()){
            sb.append(stack.pop());
        }

        return sb.toString();
    }



    @Test
    void test(){
        String s = "Let's take LeetCode contest";
        String res = reverseWords(s);
        System.out.println(res);
    }
}
