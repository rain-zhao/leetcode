import org.junit.jupiter.api.Test;

import java.util.HashMap;
import java.util.Map;

public class Task166 {
    public String fractionToDecimal(int numerator, int denominator) {
        if(numerator == 0){
            return "0";
        }
        StringBuilder sb = new StringBuilder();

        long dividend = numerator;
        long divisor = denominator;
        if((numerator^denominator) < 0){
            sb.append('-');
            dividend = Math.abs(Long.valueOf(dividend));
            divisor = Math.abs(Long.valueOf(divisor));
        }
        sb.append(dividend/divisor);
        long remain = dividend%divisor;
        if(remain == 0){
            return sb.toString();
        }
        sb.append('.');

        Map<Long,Integer> map = new HashMap<>();
        map.put(remain,sb.length());
        while(remain != 0){
            sb.append((remain*10)/divisor);
            remain = (remain*10)%divisor;
            if(map.containsKey(remain)){
                sb.insert(map.get(remain),"(").append(')');
                break;
            }else{
                map.put(remain,sb.length());
            }
        }

        return sb.toString();
    }

    @Test
    void test(){
        int numerator = 7;
        int denominator = -12;
        System.out.println(fractionToDecimal(numerator,denominator));
    }
}
