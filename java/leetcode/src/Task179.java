import org.junit.jupiter.api.Test;

import java.util.Arrays;

public class Task179 {
    public String largestNumber(int[] nums) {
        if(nums.length == 0){
            return "";
        }

        String[] strs = Arrays.stream(nums).boxed().map(String::valueOf).toArray(String[]::new);

        Arrays.sort(strs,(s1,s2)->{
            String a = s1+s2;
            String b = s2+s1;
            return b.compareTo(a);
        });
        if (strs[0].equals("0")) {
            return "0";
        }

        return Arrays.stream(strs).reduce((a,b)->a+b).orElse("");

    }

    @Test
    void test(){
        int[] nums = new int[]{3,30,34,5,9};
        System.out.println(largestNumber(nums));
    }
}
