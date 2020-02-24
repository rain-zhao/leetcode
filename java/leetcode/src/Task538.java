import org.junit.jupiter.api.Test;

public class Task538 {
    int sum =0;
    public TreeNode convertBST(TreeNode root) {
        if(root == null){
            return root;
        }
        convertBST(root.right);
        sum += root.val;
        root.val = sum;
        convertBST(root.left);

        return root;
    }

    @Test
    void test(){
        TreeNode root = new TreeNode(5).left(2).right(13);
        convertBST(root);
    }
}
