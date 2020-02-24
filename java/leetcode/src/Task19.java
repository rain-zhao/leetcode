import org.junit.jupiter.api.Test;

public class Task19 {

    //use queue implement by array
    public ListNode removeNthFromEnd(ListNode head, int n) {
        if(head == null){
            return null;
        }

        ListNode prev = new ListNode(-1);
        prev.next = head;
        //store last n node
        ListNode[] list = new ListNode[n+1];
        //store bottom index
        int bottom = -1;

        //iteration
        ListNode cur = prev;
        while(cur != null){
            bottom = (bottom+1)%(n+1);
            list[bottom] = cur;
            cur = cur.next;
        }

        //delete the nth node
        ListNode before = list[(bottom+1)%(n+1)];
        before.next = before.next.next;

        return prev.next;
    }

    @Test
    void test(){
        ListNode node = new ListNode(1);
        node.next(2).next(3).next(4).next(5);
        ListNode head = removeNthFromEnd(node,2);
        head.print();

    }

}
