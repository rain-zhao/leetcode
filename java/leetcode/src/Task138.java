import java.util.HashMap;
import java.util.Map;

public class Task138 {
    class Node {
        public int val;
        public Node next;
        public Node random;

        public Node() {}

        public Node(int _val,Node _next,Node _random) {
            val = _val;
            next = _next;
            random = _random;
        }
    };

    public Node copyRandomList(Node head) {
        if(head == null){
            return head;
        }

        Map<Node,Node> map = new HashMap<>();

        Node dummy = new Node();

        Node pre = dummy;
        Node cur = head;

        while(cur != null){
            Node node;
            if(map.containsKey(cur)){
                node = map.get(cur);
            }else{
                node = new Node();
                map.put(cur,node);
            }

            if(cur.random != null){
                if(map.containsKey(cur.random)){
                    node.random = map.get(cur.random);
                }else{
                    Node random = new Node();
                    node.random = random;
                    map.put(cur.random,random);
                }
            }

            node.val = cur.val;
            pre.next = node;

            pre = pre.next;
            cur = cur.next;
        }

        return dummy.next;
    }
}
