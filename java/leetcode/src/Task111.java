import java.util.LinkedList;
import java.util.Queue;

public class Task111 {

    //    public int minDepth(TreeNode root) {
//
//        int minDepth = 0;
//
//        if(root == null){
//            return minDepth;
//        }
//
//        Queue<TreeNode> queue = new LinkedList<>();
//        queue.offer(root);
//
//        int levelLength;
//        while((levelLength = queue.size()) != 0){
//            ++minDepth;
//            for (int i = 0; i < levelLength; i++) {
//                TreeNode node = queue.poll();
//
//                if(node.left == null && node.right == null){
//                    return minDepth;
//                }
//
//                if(node.left != null){
//                    queue.offer(node.left);
//                }
//                if(node.right != null){
//                    queue.offer(node.right);
//                }
//            }
//        }
//
//        return minDepth;
//    }
    public int minDepth(TreeNode root) {

        if (root == null) {
            return 0;
    }
        int left = minDepth(root.right);
        int right = minDepth(root.left);
        return (left == 0 || right == 0) ? left + right + 1 : 1 + Math.min(left, right);
    }
}
