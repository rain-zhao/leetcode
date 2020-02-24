import org.junit.jupiter.api.Test;

public class Task395 {
    public int longestSubstring(String s, int k) {
        if(k < 2){
            return s.length();
        }
        return count(s.toCharArray(),k,0,s.length());
    }

    private int count(char[] chars, int k, int beg, int end) {
        if(end-beg < k){
            return 0;
        }
        int[] cnts = new int[123];
        for (int i = beg; i < end; ++i) {
            ++cnts[chars[i]];
        }

        while(beg < end && cnts[chars[beg]] < k){
            ++beg;
        }
        while(beg < end && cnts[chars[end-1]] < k){
            --end;
        }

        for (int i = beg+1; i < end-1; i++) {
            if(cnts[chars[i]] < k){
                return Math.max(count(chars,k,beg,i),count(chars,k,i,end));
            }
        }

        return end-beg;
    }

    @Test
    void test(){
        String s = "weitong";
        int k = 2;
        System.out.println(longestSubstring(s,k));
    }
}
