import org.junit.jupiter.api.Test;

import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;

public class Task23 {
    public ListNode mergeKLists(ListNode[] lists) {
        if(lists == null || lists.length == 0){
            return null;
        }
        if(lists.length ==1 ){
            return lists[0];
        }

        ListNode prev = new ListNode(-1);
        ListNode cur = prev;

        PriorityQueue<ListNode> queue = new PriorityQueue<>(Comparator.comparingInt(o -> o.val));

        //init
        for (int i = 0; i < lists.length; i++) {
            if(lists[i] != null){
                queue.offer(lists[i]);
            }
        }

        ListNode node;
        while((node = queue.poll()) != null){
            cur.next = node;
            cur = cur.next;

            if(node.next != null){
                queue.offer(node.next);
            }
        }

        return prev.next;
    }


    @Test
    void test(){
        ListNode l1 = new ListNode(1);
        l1.next(new ListNode(4)).next(new ListNode(5));

        ListNode l2 = new ListNode(1);
        l2.next(new ListNode(3)).next(new ListNode(4));

        ListNode l3 = new ListNode(2);
        l3.next(new ListNode(6));

        l1.print();
        l2.print();
        l3.print();

        ListNode merge = mergeKLists(new ListNode[]{l1,l2,l3});
        merge.print();
    }
}
