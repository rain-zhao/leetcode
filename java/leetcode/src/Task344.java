import org.junit.jupiter.api.Test;

public class Task344 {
    public void reverseString(char[] s) {
        if(s.length < 2){
            return;
        }

        for (int i = 0; i < s.length/2; i++) {
            char tmp = s[s.length-1-i];
            s[s.length-1-i] = s[i];
            s[i]=tmp;
        }

    }



    @Test
    void test(){
        char[] s = new char[]{'h','e','l','l','o'};

        reverseString(s);

        System.out.println(s);
    }
}
