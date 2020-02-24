public class Task116 {
    class Node {
        public int val;
        public Node left;
        public Node right;
        public Node next;

        public Node() {
        }

        public Node(int _val, Node _left, Node _right, Node _next) {
            val = _val;
            left = _left;
            right = _right;
            next = _next;
        }
    }

    //    public Node connect(Node root) {
//        if(root == null){
//            return null;
//        }
//
//        Queue<Node> queue = new LinkedList<>();
//        queue.offer(root);
//
//        while(!queue.isEmpty()){
//            int size = queue.size();
//            for (int i = 0; i < size-1; i++) {
//                Node node = queue.poll();
//                node.next = queue.peek();
//                if(node.left != null){
//                    queue.offer(node.left);
//                    queue.offer(node.right);
//                }
//            }
//            Node node = queue.poll();
//            if(node.left != null){
//                queue.offer(node.left);
//                queue.offer(node.right);
//            }
//
//        }
//
//        return root;
//    }
//    public Node connect(Node root) {
//        if(root == null){
//            return root;
//        }
//        Node left = root.left;
//        Node right = root.right;
//        while(left != null){
//            left.next = right;
//            left = left.right;
//            right = right.left;
//        }
//        connect(root.left);
//        connect(root.right);
//
//        return root;
//    }

    public Node connect(Node root) {
        if (root == null) {
            return null;
        }
        Node left = root.left;
        Node right = root.right;

        if (left != null) {
            left.next = right;
            if (root.next != null) {
                right.next = root.next.left;
            }
        }

        connect(root.left);
        connect(root.right);


        return root;
    }

}
