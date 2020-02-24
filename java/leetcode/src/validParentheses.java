import java.util.*;

public class validParentheses {

    public static boolean isValid(String s) {
        if(s == null){
            return true;
        }

        Map<Character,Character> pair = new HashMap<>(3);
        pair.put('}','{');
        pair.put(']','[');
        pair.put(')','(');

        Stack<Character> stack = new Stack<>();

        for(char c:s.toCharArray()){
            if(!pair.containsKey(c)){
                stack.push(c);
                continue;
            }
            if(stack.isEmpty() || stack.pop() != pair.get(c)){
                return false;
            }

        }

        return stack.isEmpty();
    }

    public static void main(String[] args) {
        String s = "()";
        System.out.println(isValid(s));
    }
}
