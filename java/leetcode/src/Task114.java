import org.junit.jupiter.api.Test;

public class Task114 {
    public void flatten(TreeNode root) {
        if(root == null){
            return;
        }

        recursion2(root);

    }

    TreeNode recursion(TreeNode root){
        if(root.left == null && root.right == null){
            return root;
        }

        TreeNode tail = root;
        if(root.left != null){
            TreeNode tailL = recursion(root.left);
            tailL.right = root.right;
            root.right = root.left;
            root.left = null;
            tail = tailL;
        }

        if(tail.right != null){
            tail = recursion(tail.right);
        }

        return tail;
    }

    TreeNode recursion2(TreeNode root){
        if(root == null ){
            return root;
        }

        TreeNode tail = root;
        TreeNode tailL = recursion(root.left);
        TreeNode tailR = recursion(root.right);

        if(tailL != null){
            tail = tailL;
            tailL.right = root.right;
            root.right = root.left;
            root.left = null;
        }

        if(tailR!= null){
            tail = tailR;
        }

        return tail;
    }

    @Test
    void test(){
        TreeNode root = new TreeNode(1).left(2).right(5);
        root.left.left(3).right(4);
        root.right.right(6);
        System.out.println(root);
        flatten(root);
        System.out.println(root);
    }

}
