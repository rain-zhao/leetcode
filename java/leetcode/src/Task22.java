import java.util.ArrayList;
import java.util.List;

public class Task22 {
    public static List<String> generateParenthesis(int n) {
        List<String> res = new ArrayList<>();

        generateParenthesis(n,n,res,"");

        return res;
    }

    static void generateParenthesis(int left,int right,List<String> res,String str){
        if(left == 0 && right ==0){
            res.add(str);
        }
        if(left > 0){
            generateParenthesis(left-1,right,res,str+"(");
        }
        if(right > left){
            generateParenthesis(left,right-1,res,str+")");
        }
    }

    public static void main(String[] args) {
        System.out.println(generateParenthesis(3));
    }


}
