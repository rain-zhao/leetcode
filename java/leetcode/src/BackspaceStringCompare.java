import java.util.Stack;
import java.util.stream.StreamSupport;

public class BackspaceStringCompare {
    public static boolean backspaceCompare(String S, String T) {

        Stack a = produceStr(S);
        Stack b = produceStr(T);

        return a.equals(b);
    }

    private static Stack produceStr(String s){
        Stack stack = new Stack();
        for(char c :s.toCharArray()){
            if(c == '#'){
                if(!stack.isEmpty()){
                    stack.pop();
                }
            }else{
                stack.push(c);
            }
        }
        return stack;
    }

    public static boolean backspaceCompare2(String S, String T) {
        String a = produceStr2(S);
        String b = produceStr2(T);
        return a.equals(b);
    }

    //反向输出
    private static String produceStr2(String s){
        StringBuilder sb = new StringBuilder(8);
        int count = 0;
        for(int i = s.length()-1; i >= 0 ;--i){
            char c = s.charAt(i);
            if(c == '#'){
                ++count;
                continue;
            }
            if(count > 0){
                --count;
                continue;
            }
            sb.append(c);
        }

        return sb.toString();
    }


    public static void main(String[] args) {
        String s = "a##c";
        String t = "#a#c";

        System.out.println(backspaceCompare2(s,t));
    }
}
