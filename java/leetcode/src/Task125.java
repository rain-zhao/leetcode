import org.junit.jupiter.api.Test;

public class Task125 {
    public boolean isPalindrome(String s) {
        int left = 0,right = s.length()-1;

        while(left < right){
            char c1 = s.charAt(left);
            char c2 = s.charAt(right);
            if(!isValid(c1)){
                ++left;
            }else if(!isValid(c2)){
                --right;
            } else{
                if(c1 == c2|| c1 >= 'A' && c2 >= 'A' && (c1 - c2 == 32|| c1-c2 == -32 )){
                    ++left;
                    --right;
                }else {
                    return false;
                }
            }
        }

        return true;
    }

    boolean isValid(char c){
        return c >='0' && c<='9'  ||c >='a' && c<='z' ||c >='A' && c<='Z';
    }

    @Test
    void test(){
        String s = "A man, a plan, a canal: Panama";
        System.out.println(isPalindrome(s));
    }

}
