import org.junit.jupiter.api.Test;

import java.util.HashMap;
import java.util.Map;

public class Task460 {
    class Node{
        Node prev;
        Node next;
        Integer val;
        Integer key;
        int cnt=1;

        Node(Integer key,Integer val){
            this.key = key;
            this.val = val;
        }
    }

    class LFUCache {

        Map<Integer,Node> map;

        Node head;

        Node tail;

        int remain;

        public LFUCache(int capacity) {
            map = new HashMap<>(capacity);
            this.remain = capacity;
            head = tail = new Node(null,-1);
        }

        public int get(int key) {
            if(map.containsKey(key)){
                Node node = map.get(key);
                manageNode(node);
                return node.val;
            }
            return -1;
        }

        public void put(int key, int value) {
            if(map.containsKey(key)){
                Node node = map.get(key);
                manageNode(node);
                node.val = value;

            }else{
                if(remain == 0){
                    if(head.next == null){
                        return;
                    }
                    map.remove(head.next.key);
                    unlink(head.next);
                }else{
                    --remain;
                }
                Node node = new Node(key,value);
                map.put(key,node);

                Node nextNode = head;
                while(nextNode.next != null && nextNode.next.cnt <= node.cnt){
                    nextNode = nextNode.next;
                }
                insertNext(node,nextNode);
            }
        }


        private void manageNode(Node node){
            ++node.cnt;
            Node nextNode = node;
            while(nextNode.next != null && nextNode.next.cnt <= node.cnt){
                nextNode = nextNode.next;
            }

            if(nextNode != node){
                //unlink
                unlink(node);
                insertNext(node,nextNode);
            }
        }

        private void insertNext(Node currNode,Node prevNode){
            currNode.next = prevNode.next;
            if(prevNode.next != null){
                prevNode.next.prev = currNode;
            }else{
                tail = currNode;
            }
            prevNode.next = currNode;
            currNode.prev = prevNode;
        }

        private void unlink(Node node){
            //prev must not null
            node.prev.next = node.next;
            if(node.next != null){
                node.next.prev = node.prev;
            }else{
                tail = node.prev;
            }
            node.prev = node.next = null;
        }
    }
    /**
     * Your LFUCache object will be instantiated and called as such:
     * LFUCache obj = new LFUCache(capacity);
     * int param_1 = obj.get(key);
     * obj.put(key,value);
     */

    @Test
    void test(){
        LFUCache cache = new LFUCache( 0 /* capacity (缓存容量) */ );

        cache.put(0, 0);
        System.out.println(cache.get(0));      // 返回 1


    }
}
