import org.junit.jupiter.api.Test;

import java.util.Stack;

public class Task230 {
//    int cnt = 0;
//    int res;
//    public int kthSmallest(TreeNode root, int k) {
//        recur(root,k);
//        return res;
//    }
//
//    void recur(TreeNode root, int k) {
//        if(root == null || cnt >= k){
//            return;
//        }
//
//        recur(root.left,k);
//
//        ++cnt;
//        if(cnt == k){
//            res = root.val;
//        }
//
//        recur(root.right,k);
//
//    }

    public int kthSmallest(TreeNode root, int k) {
        int cnt = 0;
        Stack<TreeNode> stack = new Stack<>();

        TreeNode node = root;
        while (!stack.isEmpty() || node != null) {

            while (node != null) {
                stack.push(node);
                node = node.left;
            }

            node = stack.pop();
            ++cnt;
            if (cnt == k) {
                return node.val;
            }

            node = node.right;

        }
        return -1;
    }

    @Test
    void test() {
        TreeNode root = new TreeNode(3);
        root.left(1).right(4);
        root.left.right(2);
        System.out.println(kthSmallest(root, 1));
    }

}
