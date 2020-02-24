import org.junit.jupiter.api.Test;

import java.util.*;

public class Task301 {
//    List<String> res = new ArrayList<>();
//
//    //dfs
//    public List<String> removeInvalidParentheses(String s) {
//        res.add("");
//
//        if (s.length() == 0) {
//            return res;
//        }
//
//        dfs(s, 0, 0, 0, "");
//
//
//        return new ArrayList<>(new HashSet<>(res));
//    }
//
//    void dfs(String s, int idx, int left, int right, String result) {
//        //terminator
//        if (s.length() == idx) {
//            if (left == right) {
//                if (result.length() == res.get(0).length()) {
//                    res.add(result);
//                } else if (result.length() > res.get(0).length()) {
//                    res.clear();
//                    res.add(result);
//                }
//            }
//            return;
//        }
//        if (right > left) {
//            return;
//        }
//
//        //process
//        char c = s.charAt(idx);
//
//        //recursion
//
//        //has 'c'
//        if (c == '(') {
//            dfs(s, idx + 1, left + 1, right, result + c);
//        } else if (c == ')') {
//            dfs(s, idx + 1, left, right + 1, result + c);
//        } else {
//            dfs(s, idx + 1, left, right, result + c);
//        }
//
//        //or no 'c'
//        dfs(s, idx + 1, left, right, result);
//
//        //reverse
//    }


    Set<String> resultSet = new HashSet<>();

    public List<String> removeInvalidParentheses(String s) {

        //count left and right misplace
        int left = 0,right = 0;
        for (char c : s.toCharArray()) {
            if(c == '('){
                ++left;
            }else if(c == ')'){
                if(left > 0){
                    --left;
                }else{
                    ++right;
                }
            }
        }

        dfs(s,0,0,0,left,right,"");

        return new ArrayList<>(resultSet);
    }


    void dfs(String s, int idx, int left, int right,int mLeft,int mRight, String result) {
        //terminator
        if (s.length() == idx) {
            if (left == right) {
                resultSet.add(result);
            }
            return;
        }

        if(left < right){
            return;
        }

        //process
        char c = s.charAt(idx);

        //recursion

        if(c == '(' ){
            //delete left
            if( mLeft > 0){
                dfs(s,idx+1,left,right,mLeft-1,mRight,result);
            }
            //use left
            dfs(s,idx+1,left+1,right,mLeft,mRight,result+c);
        }else if(c == ')' ) {
            //delete right
            if( mRight > 0){
                dfs(s,idx+1,left,right,mLeft,mRight-1,result);
            }
            //use left
            dfs(s,idx+1,left,right+1,mLeft,mRight,result+c);

        }else{
            //use c
            dfs(s,idx+1,left,right,mLeft,mRight,result+c);
        }



        //reverse
    }



    @Test
    void test() {
        String s = "()())()";
        System.out.println(removeInvalidParentheses(s));
    }
}
