public class Task98 {

//    public static boolean isValidBST(TreeNode root) {
//
//
//        boolean lv = root.left==null?true:isValidBST(root.left) && root.val > rightMost(root.left);
//        boolean rv = root.right==null?true:isValidBST(root.right)&& root.val < leftMost(root.right);
//
//        return lv && rv ;
//    }
//
//    private static int leftMost(TreeNode node){
//        if(node.left != null){
//            return leftMost(node.left);
//        }
//        return node.val;
//    }
//
//    private static int rightMost(TreeNode node){
//        if(node.right != null){
//            return rightMost(node.right);
//        }
//        return node.val;
//    }
////#################################################################################
//
//    public static boolean isValidBST2(TreeNode root) {
//
//        return isValid(root,new int[2]);
//    }
//
//    public static boolean isValid(TreeNode node,int[] minmax){
//        boolean lv;
//        boolean rv;
//        if(node.left == null){
//            lv=true;
//            minmax[0]=node.val;
//        }else{
//            int[] temp = new int[2];
//            lv=isValid(node.left,temp) && node.val > temp[1];
//            minmax[0]=temp[0];
//        }
//
//        if(node.right == null){
//            rv=true;
//            minmax[1]=node.val;
//        }else{
//            int[] temp = new int[2];
//            rv=isValid(node.right,temp) && node.val < temp[0];
//            minmax[1]= temp[1];
//        }
//
//        return lv && rv ;
//    }
    //###########################################

//    static TreeNode prev=null;
//
//    public static boolean isValidBST(TreeNode root) {
//
//        if(root == null){
//            return true;
//        }
//        if(!isValidBST(root.left)){
//            return false;
//        }
//        if(prev != null && prev.val > root.val){
//            return false;
//        }
//        prev = root;
//        return isValidBST(root.right);
//
//    }

    public static boolean isValidBST(TreeNode root) {
        return isValid(root,null,null);

    }

    public static boolean isValid(TreeNode root,Integer min,Integer max) {
        if(root == null){
            return true;
        }
        if(min != null && root.val <= min){
            return false;
        }
        if(max != null && root.val >= max){
            return false;
        }

        return isValid(root.left,min,root.val)
                && isValid(root.right,root.val,max);

    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(2);
        root.left = new TreeNode(1);
        root.right = new TreeNode(3);

        System.out.println(isValidBST(root));
    }
}
