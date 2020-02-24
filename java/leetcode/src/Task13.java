import org.junit.jupiter.api.Test;

public class Task13 {
    public int romanToInt(String s) {
        if(s.equals("")){
            return 0;
        }

        int[] vals = new int[]{1000,900,500,400,100,90,50,40,10,9,5,4,1};
        String[] roms = new String[]{"M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"};
        int idx = 0;
        int res = 0;
        while(!s.equals("")){
            while(!s.startsWith(roms[idx])){
                ++idx;
            }
            res+=vals[idx];
            s = s.substring(roms[idx].length());
        }
        return res;
    }

    @Test
    void test(){
        String s = "III";
        System.out.println(romanToInt(s));
    }

}
