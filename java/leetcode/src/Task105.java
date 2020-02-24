import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class Task105 {


//    public TreeNode buildTree(int[] preorder, int[] inorder) {
//        if (preorder.length == 0) {
//            return null;
//        }
//        TreeNode root = new TreeNode(preorder[0]);
//        int i = 0;
//        while (preorder[0] != inorder[i]) {
//            ++i;
//        }
//        root.left = buildTree(Arrays.copyOfRange(preorder,1,i+1),Arrays.copyOfRange(inorder,0,i));
//        root.right = buildTree(Arrays.copyOfRange(preorder,i+1,preorder.length),Arrays.copyOfRange(inorder,i+1,inorder.length));
//
//        return root;
//    }
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        for (int i = 0; i < inorder.length; i++) {
            inOrdMap.put(inorder[i],i);
        }
        this.preorder = preorder;
        this.inorder = inorder;

        return buildTree(0,preorder.length,0,inorder.length);
    }

    int[] preorder;
    int[] inorder;
    Map<Integer,Integer> inOrdMap = new HashMap<>();

    TreeNode buildTree(int preIdxfrom,int preIdxTo,int inIdxfrom,int inIdxTo) {
        if(preIdxfrom == preIdxTo){
            return null;
        }
        int rootVal = preorder[preIdxfrom];
        TreeNode root = new TreeNode(rootVal);

        int idx = inOrdMap.get(rootVal);
        int length = idx - inIdxfrom;

        root.left = buildTree(preIdxfrom+1,preIdxfrom+1+length,inIdxfrom,inIdxfrom+length);
        root.right =buildTree(preIdxfrom+1+length,preIdxTo,inIdxfrom+length+1,inIdxTo);

        return root;
    }


}
