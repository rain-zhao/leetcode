import org.junit.jupiter.api.Test;

public class Task394 {
    int idx = 0;
    public String decodeString(String s) {
        char[] chars = s.toCharArray();

        return expandNext(chars);

    }

    private String expandNext(char[] chars) {
        String res = "";
        int multi = 0;
        while(idx < chars.length){
            if(chars[idx] >='0' && chars[idx] <='9'){
                multi = multi*10 +chars[idx]-'0';
                ++idx;
            }else if(chars[idx] == '['){
                ++idx;
                String repeat = expandNext(chars);
                for (int i = 0; i < multi; i++) {
                    res+=repeat;
                }

            }else if(chars[idx] == ']'){
                ++idx;
                return res;
            }else{
                res+=chars[idx];
                ++idx;
            }

        }

        return res;
    }


    @Test
    void test(){
        String s = "3[a]2[bc]";
        System.out.println(decodeString(s));
    }
}
