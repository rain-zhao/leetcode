import org.junit.jupiter.api.Test;

public class Task148 {
    public ListNode sortList(ListNode head) {
        if (head == null || head.next == null){
            return head;
        }

        return sortList(head,null);
    }

    private ListNode sortList(ListNode head, ListNode end) {
        if(head.next == end){
            return head;
        }
        ListNode slow = head,fast = head;
        while(fast.next != end && fast.next.next != end){
            slow = slow.next;
            fast = fast.next.next;
        }
        ListNode list1 = sortList(head,slow.next);
        ListNode list2 = sortList(slow.next,end);

        ListNode dummy = new ListNode(-1);
        ListNode cur = dummy;
        while (list1 != slow.next && list2 != end){
            if(list1.val <= list2.val){
                cur.next = list1;
                list1 = list1.next;
            }else{
                cur.next = list2;
                list2 = list2.next;
            }
            cur = cur.next;
        }
        if(list1 == slow.next){
            cur.next = list2;
        }else {
            cur.next = list1;
            slow.next = end;
        }

        return dummy.next;
    }


    @Test
    void test(){
        ListNode head = new ListNode(-1);
        head.next(5).next(3).next(4).next(0);
        head.print();
        ListNode sort = sortList(head);
        sort.print();
    }


}
