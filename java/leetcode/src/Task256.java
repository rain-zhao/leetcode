import java.util.*;

public class Task256 {
//    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
//        if(root == null) return null;
//        if(root ==q || root == p){
//            return root;
//        }
//        TreeNode left = lowestCommonAncestor(root.left, p, q);
//        TreeNode right = lowestCommonAncestor(root.right, p, q);
//
//        if (left == null) {
//            return right;
//        }
//        if(right == null){
//            return left;
//        }
//        return root;
//    }

    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {

        if(root == null){
            return null;
        }
        if(root ==q || root == p){
            return root;
        }

        Map<TreeNode,TreeNode> prevMap = new HashMap<>();

        markPrev(root,prevMap);

        TreeNode res = null;
        Set<TreeNode> pathSet= new HashSet<>();
        while(p != null){
            pathSet.add(p);
            p=prevMap.get(p);
        }

        while(q != null) {
            if ( pathSet.contains(q)){
                return q;
            }
            q=prevMap.get(q);
        }
        return null;

    }

    public static void markPrev(TreeNode node, Map<TreeNode,TreeNode> prevMap){
        if(node ==null){
            return;
        }
        if(node.left !=null){
            prevMap.put(node.left,node);
            markPrev(node.left,prevMap);
        }
        if(node.right !=null){
            prevMap.put(node.right,node);
            markPrev(node.right,prevMap);
        }
    }

    public static void main(String[] args) {
        List<Integer> list = new ArrayList<>();
    }
}
