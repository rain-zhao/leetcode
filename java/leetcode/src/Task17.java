import org.junit.jupiter.api.Test;

import java.util.*;

public class Task17 {

    static Map<Character,String> map = new HashMap<>();

    List<String> res = new ArrayList<>();

    static {
        map.put('2',"abc");
        map.put('3',"def");
        map.put('4',"ghi");
        map.put('5',"jkl");
        map.put('6',"mno");
        map.put('7',"pqrs");
        map.put('8',"tuv");
        map.put('9',"wxyz");
    }

    //dfs
    public List<String> letterCombinations(String digits) {

        if(digits.length() == 0){
            return res;
        }

        dfs(digits,0,"");

        return  res;
    }

    void dfs(String digits , int idx,String result){
        //ternimator
        if(idx == digits.length()){
            res.add(result);
            return;
        }

        //process
        String str = map.get(digits.charAt(idx));

        //recursion
        for(char c:str.toCharArray()){
            dfs(digits,idx+1,result+c);
        }

        //reverse
    }

    //bfs
    public List<String> letterCombinations2(String digits) {

        if(digits.length() == 0){
            return res;
        }

        LinkedList<String> ans = new LinkedList<String>();

        //init
        ans.offer("");

        for(char digit:digits.toCharArray()){
            int size = ans.size();
            for (int j = 0; j < size ; j++) {
                String subAns = ans.poll();
                for(char c:map.get(digit).toCharArray()){
                    ans.offer(subAns+c);
                }
            }
        }

        return new ArrayList<>(ans);
    }

    @Test
    void test(){
        String digits = "23";
        System.out.println(letterCombinations2(digits));
    }

}
