public class Task124 {

    int max = Integer.MIN_VALUE;

    public int maxPathSum(TreeNode root) {
        if (root == null) {
            return 0;
        }

        dfs(root);

        return max;
    }

    //    private int dfs(TreeNode root) {
//        if(root == null){
//            return 0;
//        }
//
//        int left = dfs(root.left);
//        int right = dfs(root.right);
//
//        if(left > 0){
//            if(right > 0){
//                //left > 0 && right > 0;
//                max = Math.max(max,root.val+left+right);
//                return root.val+ Math.max(left,right);
//            }else{
//                //left > 0 && right <= 0;
//                max = Math.max(max,root.val+left);
//                return root.val+left;
//            }
//
//        }else if(right > 0){
//            //left <= 0 && right > 0;
//            max = Math.max(max,root.val+right);
//            return root.val+right;
//        }else {
//            //left <= 0 && right <= 0
//            max = Math.max(max,root.val);
//            return root.val;
//        }
//
//    }
    private int dfs(TreeNode root) {
        if (root == null) {
            return 0;
        }

        int left = dfs(root.left);
        int right = dfs(root.right);

        max = Math.max(max, root.val + left + right);

        return Math.max(root.val + Math.max(left, right),0);
    }
}
