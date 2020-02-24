import org.junit.jupiter.api.Test;

public class Task227 {
    int pos = 0;

    public int calculate(String s) {
        s = "+"+s;
        int res = 0;
        while(hasNext(s)){
            if(s.charAt(pos++) == '+'){
                res +=add(s);
            }else{
                res -=add(s);
            }
        }

        return res;
    }


    int add(String s) {
        hasNext(s);
        int op1 = nextInt(s);

        while (hasNext(s) && ( s.charAt(pos) == '/' ||  s.charAt(pos) == '*')) {
            char op =  s.charAt(pos++);
            hasNext(s);
            int op2 = nextInt(s);
            if (op == '/') {
                op1 = op1 / op2;
            } else {
                op1 = op1 * op2;
            }
        }

        return op1;
    }

    boolean hasNext(String s){
        //trim space
        while (pos != s.length() && s.charAt(pos) == ' ') {
            ++pos;
        }
        return pos != s.length();
    }

    int nextInt(String s) {
        int cur = pos;
        while (pos != s.length() && s.charAt(pos) >= 48){
            ++pos;
        }
        return Integer.valueOf(s.substring(cur, pos));
    }

    @Test
    void test() {
       String s = "3+2*2";
        System.out.println(calculate(s));
    }
}
