import org.junit.jupiter.api.Test;

public class Task541 {
    public String reverseStr(String s, int k) {
        if(k < 2){
            return s;
        }

        char[] res = s.toCharArray();

        int factor = 0;

        while(k*factor*2 < res.length-1){
            int left = k*factor*2;
            int right = Math.min(left + k-1,res.length-1);
            while(left < right){
                char tmp = res[left];
                res[left] = res[right];
                res[right] = tmp;
                --right;
                ++left;
            }
            ++factor;
        }

        return String.valueOf(res);
    }


    @Test
    void test(){
        String s = "abcdefg";
        int k = 2;

        String res = reverseStr(s,k);

        System.out.println(res);
    }
}
