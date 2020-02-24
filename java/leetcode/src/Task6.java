import org.junit.jupiter.api.Test;

public class Task6 {
    public String convert(String s, int numRows) {
        if(numRows == 1){
            return s;
        }

        StringBuilder[] sbs = new StringBuilder[numRows];
        for (int i = 0; i < sbs.length; i++) {
            sbs[i] = new StringBuilder();
        }

        int idx = 0;
        while(idx < s.length()){
            for (int i = 0; i < numRows && idx < s.length(); ++i,++idx) {
                sbs[i].append(s.charAt(idx));
            }

            for (int i = numRows-2; i > 0 && idx < s.length(); --i,++idx) {
                sbs[i].append(s.charAt(idx));
            }

        }

        for (int i = 1; i < numRows; i++) {
            sbs[0].append(sbs[i]);
        }

        return sbs[0].toString();
    }


    @Test
    void test(){
        String s = "LEETCODEISHIRING";
        int numRows = 2;

        System.out.println(convert(s,numRows));
    }

}
