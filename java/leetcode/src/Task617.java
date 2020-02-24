import org.junit.jupiter.api.Test;

public class Task617 {
    public TreeNode mergeTrees(TreeNode t1, TreeNode t2) {
        if(t1 == null ){
            return t2;
        }
        if(t2 == null ) {
            return t1;
        }

        TreeNode res = new TreeNode(t1.val + t2.val);
        res.right = mergeTrees(t1.right,t2.right);
        res.left = mergeTrees(t1.left,t2.left);

        return res;
    }



    @Test
    void test(){
        TreeNode t1 = new TreeNode(1);
        t1.left(3).right(2);
        t1.left.left(5);
        TreeNode t2 = new TreeNode(2);
        t2.left(1).right(3);
        t2.left.right(4);
        t2.right.right(7);

        TreeNode t3 = mergeTrees(t1,t2);

        System.out.println(t3);
    }

}
