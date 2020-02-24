import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Task412 {
    public List<String> fizzBuzz(int n) {
        if (n == 0) {
            return Collections.emptyList();
        }
        List<String> res = new ArrayList<>(n);

        for (int i = 1; i <= n; ++i) {
            if(i % 15 == 0){
                res.add("FizzBuzz");
            }else if(i % 3 == 0){
                res.add("Fizz");
            }else if(i % 5 == 0){
                res.add("Buzz");
            }else{
                res.add(""+i);
            }
        }

        return res;
    }

    @Test
    void test(){
        System.out.println(fizzBuzz(15));
    }
}
