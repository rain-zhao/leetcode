public class Task255 {
//    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
//        if(root == null){
//            return null;
//        }
//
//        if(root.val > p.val && root.val > q.val){
//            return lowestCommonAncestor(root.left, p, q);
//        }
//        if(root.val < p.val && root.val < q.val){
//            return lowestCommonAncestor(root.right, p, q);
//        }
//        return root;
//    }
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {

        while(root != null){
            if(root.val > p.val && root.val > q.val){
                root = root.left;
                continue;
            }
            if(root.val < p.val && root.val < q.val){
                root = root.right;
                continue;
            }
            return root;
        }
        return null;
    }
}
