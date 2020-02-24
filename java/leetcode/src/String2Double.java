import org.junit.jupiter.api.Test;

public class String2Double {

    double string2Double(String str) {
        if (str == null || str.equals("")) {
            return 0;
        }
        double res = 0;

        double exp = 0;
        for (char c : str.toCharArray()) {
            if(c =='.'){
                exp = 0.1;
                continue;
            }
            if(exp == 0){
                res = res*10 + (c-'0');
            }else{
                res += (c-'0')*exp;
                exp*=0.1;
            }

        }


        return res;
    }


    @Test
    void test() {
        String str = "345.12";
        System.out.println(string2Double(str));
    }

}
