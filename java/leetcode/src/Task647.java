import org.junit.jupiter.api.Test;

public class Task647 {
    public int countSubstrings(String s) {
        if(s.length() < 2){
            return  s.length();
        }

        int res = 0;

        for (int i = 0; i < s.length() ; i++) {
            res += count(s,i,i);
            res += count(s,i,i+1);
        }

        return res;
    }

    int count(String s,int left,int right){
        int cnt = 0;
        while(left >=0 && right < s.length() && s.charAt(left--) == s.charAt(right++)){
            ++cnt;
        }
        return cnt;
    }


    @Test
    void test(){
        String s = "aaa";
        System.out.println(countSubstrings(s));
    }
}
