import org.junit.jupiter.api.Test;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class Task101 {

    public boolean isSymmetric(TreeNode root) {
        if(root == null){
            return true;
        }
        //condition

        return  isMirror(root.left,root.right);
    }

    boolean isMirror(TreeNode t1,TreeNode t2){
        if(t1 == null){
            return t2 == null;
        }
        if(t2 == null){
            return t1 == null;
        }

        return t1.val == t2.val
                && isMirror(t1.left,t2.right)
                && isMirror(t1.right,t2.left);

    }


    public boolean isSymmetric2(TreeNode root) {
        if(root == null){
            return true;
        }
        //condition
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root.left);
        queue.offer(root.right);

        while (!queue.isEmpty()){
            TreeNode t1 = queue.poll();
            TreeNode t2 = queue.poll();
            if (t1 == null && t2 == null) continue;
            if (t1 == null || t2 == null) return false;
            if(t1.val != t2.val){
                return false;
            }
            queue.addAll(Arrays.asList(t1.left,t2.right,t1.right,t2.left));

        }

        return true;
    }


    @Test
    void test(){
        TreeNode root = new TreeNode(1);
        root.left(2).right(2);
        root.left.left(3).right(4);
        root.right.left(4).right(3);

        System.out.println(isSymmetric2(root));
    }
}
