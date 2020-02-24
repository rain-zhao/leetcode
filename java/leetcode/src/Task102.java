import java.util.*;

public class Task102 {
//    public List<List<Integer>> levelOrder(TreeNode root) {
//        List<List<Integer>> res = new ArrayList<>();
//        if(root == null){
//            return res;
//        }
//
//        int curLevel = -1;
//        Map<TreeNode,Integer> levelMap = new HashMap<>();
//        levelMap.put(root,0);
//
//        Queue<TreeNode> queue = new LinkedList<>();
//        queue.offer(root);
//
//        List<Integer> levelList = null;
//        //loop
//        while(!queue.isEmpty()){
//            //get the node info
//            TreeNode node = queue.poll();
//            int level = levelMap.get(node);
//            //process
//            if(curLevel != level){
//                levelList = new ArrayList<>();
//                res.add(levelList);
//                curLevel = level;
//            }
//            levelList.add(node.val);
//
//            //push childs into queue
//            if(node.left != null){
//                queue.offer(node.left);
//                levelMap.put(node.left,level+1);
//            }
//            if(node.right != null){
//                queue.offer(node.right);
//                levelMap.put(node.right,level+1);
//            }
//
//        }
//
//        return res;
//    }

//    public List<List<Integer>> levelOrder(TreeNode root) {
//
//        List<List<Integer>> res = new ArrayList<>();
//        if(root == null){
//            return res;
//        }
//
//        Queue<TreeNode> queue = new LinkedList<>();
//        queue.offer(root);
//
//        int levelLength;
//        //loop
//        while((levelLength = queue.size()) != 0){
//
//            //current level list
//            List<Integer>  levelList = new ArrayList<>();
//            res.add(levelList);
//
//            for (int i = 0; i < levelLength; i++) {
//                //get the node info
//                TreeNode node = queue.poll();
//                //add to res
//                levelList.add(node.val);
//
//                //push childs into queue
//                if(node.left != null){
//                    queue.offer(node.left);
//                }
//                if(node.right != null){
//                    queue.offer(node.right);
//                }
//
//            }
//
//        }
//
//        return res;
//    }


    //dfs
    public static List<List<Integer>> levelOrder(TreeNode root) {

        List<List<Integer>> res = new ArrayList<>();

        dfs(root,res,0);

        return res;
    }

    static void dfs(TreeNode node,List<List<Integer>> res,int level){
        if(node == null){
            return;
        }
        if(res.size() == level){
            res.add(new ArrayList<>());
        }
        res.get(level).add(node.val);

        dfs(node.left,res,level + 1);

        dfs(node.right, res, level + 1);
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(3);
        root.left = new TreeNode(9);
        root.right = new TreeNode(20);

        System.out.println(levelOrder(root));

    }

}
