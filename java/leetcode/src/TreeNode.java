public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
        val = x;
    }

    TreeNode left(int val){
        left = new TreeNode(val);
        return this;
    }

    TreeNode right(int val){
        right = new TreeNode(val);
        return this;
    }
}