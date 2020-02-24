import org.junit.jupiter.api.Test;

public class Task543 {

    int size;
    public int diameterOfBinaryTree(TreeNode root) {
        if(root == null){
            return 0;
        }

        int left = depth(root.left);
        int right = depth(root.right);
        size = Math.max(size,left+right);


        return size;
    }

    private int depth(TreeNode root) {
        if(root == null){
            return 0;
        }

        int left = depth(root.left);
        int right = depth(root.right);
        size = Math.max(size,left+right);

        return Math.max(left,right)+1;
    }


    @Test
    void test(){
        TreeNode root = new TreeNode(1).left(2).right(3);
        root.left.left(4).right(5);

        System.out.println(diameterOfBinaryTree(root));
    }
}
