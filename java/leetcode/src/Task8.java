import org.junit.jupiter.api.Test;

public class Task8 {
    public int myAtoi(String str) {
        if(str.length() == 0){
            return 0;
        }

        int idx = 0;
        char[] charArray = str.toCharArray();

        //trim space prefix
        while(idx < charArray.length && charArray[idx] == ' '){
            ++idx;
        }

        //symbol
        int symbol = 1;
        if(idx < charArray.length){
            if(charArray[idx] == '+'){
                ++idx;
            }else if(charArray[idx] == '-'){
                ++idx;
                symbol = -1;
            }
        }

        //number
        long res = 0;
        while(idx < charArray.length && charArray[idx] >= '0' && charArray[idx] <= '9'){
            res = res* 10 + charArray[idx]-'0';
            if(res*symbol < Integer.MIN_VALUE){
                return Integer.MIN_VALUE;
            }else if(res*symbol > Integer.MAX_VALUE){
                return Integer.MAX_VALUE;
            }
            ++idx;
        }

        return (int)res*symbol;
    }


    @Test
    void test(){
        String s = "4193 with words";
        System.out.println(myAtoi(s));
    }
}
