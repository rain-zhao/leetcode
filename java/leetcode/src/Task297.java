import org.junit.jupiter.api.Test;

import java.util.*;

public class Task297 {
    //    public class Codec {
//
//        // Encodes a tree to a single string.
//        public String serialize(TreeNode root) {
//            if(root == null){
//                return "[]";
//            }
//            List<Integer> res = new ArrayList<>();
//
//            Queue<TreeNode> queue = new LinkedList<>();
//            queue.add(root);
//
//            while (!queue.isEmpty()){
//                TreeNode node = queue.poll();
//                if(node == null){
//                    res.add(null);
//                }else{
//                    res.add(node.val);
//                    queue.offer(node.left);
//                    queue.offer(node.right);
//                }
//
//            }
//            while(res.get(res.size()-1) == null){
//                res.remove(res.size()-1);
//            }
//            return res.toString();
//        }
//
//        // Decodes your encoded data to tree.
//        public TreeNode deserialize(String data) {
//            if(data.equals("[]")){
//                return null;
//            }
//            Integer[] array = Arrays.stream(data.substring(1, data.length() - 1).split(","))
//                    .map(String::trim).map(val->val.equals("null") ? null:Integer.valueOf(val)).toArray(Integer[]::new);
//
//            TreeNode root = new TreeNode(array[0]);
//            int cur = 1;
//
//            Queue<TreeNode> queue = new LinkedList<>();
//            queue.offer(root);
//
//            while(!queue.isEmpty()){
//                TreeNode node = queue.poll();
//                //left
//                if(cur < array.length){
//                    Integer left = array[cur++];
//                    if(left != null){
//                        TreeNode leftNode = new TreeNode(left);
//                        node.left = leftNode;
//                        queue.offer(leftNode);
//                    }
//                }
//
//                //right
//                if(cur < array.length){
//                    Integer right = array[cur++];
//                    if(right != null){
//                        TreeNode rightNode = new TreeNode(right);
//                        node.right = rightNode;
//                        queue.offer(rightNode);
//                    }
//                }
//            }
//
//            return root;
//        }
//
//
//
//    }
    public class Codec {
        // Decodes your encoded data to tree.
        public TreeNode deserialize(String data) {

            Queue<String> queue = new LinkedList<>(Arrays.asList(data.split(",")));

            TreeNode root = recursion(queue);

            return root;
        }

        private TreeNode recursion(Queue<String> queue) {
            String val = queue.poll();
            if(val.equals("nil")){
                return null;
            }else{
                TreeNode node = new TreeNode(Integer.valueOf(val));
                node.left = recursion(queue);
                node.right = recursion(queue);
                return  node;
            }

        }

        // Encodes a tree to a single string.
        public String serialize(TreeNode root) {

            StringBuilder sb = new StringBuilder();

            dfs(root, sb);

            return sb.toString();

        }

        private void dfs(TreeNode root, StringBuilder sb) {
            if(root == null){
                sb.append("nil,");
                return;
            }
            sb.append(root.val).append(",");

            dfs(root.left,sb);
            dfs(root.right,sb);
        }


    }

    @Test
    void test() {
        String data = "1,2,3,nil,nil,4,nil,nil,5,nil,nil,";
        Codec codec = new Codec();
        TreeNode root = codec.deserialize(data);
        String des = codec.serialize(root);

    }

}
