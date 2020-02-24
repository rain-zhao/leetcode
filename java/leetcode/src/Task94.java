import org.junit.jupiter.api.Test;

import java.util.*;

public class Task94 {

    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<>();

        recursion(root,res);

        return res;
    }

    void recursion(TreeNode root,List<Integer> res){
        if(root == null){
            return;
        }

        recursion(root.left,res);
        res.add(root.val);
        recursion(root.right,res);
    }

    //iteration
    public List<Integer> inorderTraversal2(TreeNode root) {
        List<Integer> res = new ArrayList<>();

        if(root == null){
            return res;
        }
        Stack<TreeNode> stack = new Stack<>();

        TreeNode cur = root;
        while (cur != null ||!stack.isEmpty()){
            while (cur != null){
                stack.push(cur);
                cur = cur.left;
            }
            cur = stack.pop();
            res.add(cur.val);
            cur = cur.right;
        }

        return res;
    }

    @Test
    void test(){
        TreeNode root = new TreeNode(1);
        root.right(2).right.left(3);
        System.out.println(inorderTraversal2(root));
    }
}
