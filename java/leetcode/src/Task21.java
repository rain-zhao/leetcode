import org.junit.jupiter.api.Test;

public class Task21 {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {

        ListNode prev = new ListNode(-1);
        ListNode cur=prev,cur1= l1,cur2=l2;

        while(cur1 != null || cur2 != null){
            ListNode min = cur1;

            if(cur2 != null){
                min = cur1 == null ? cur2 : cur1.val < cur2.val ? cur1:cur2;
            }

            cur.next = min;
            cur = cur.next;
            if(min == cur1){
                cur1 = cur1.next;
            }else{
                cur2 = cur2.next;
            }

        }

        return prev.next;
    }

    @Test
    void test(){
        ListNode l1 = new ListNode(1);
        l1.next(new ListNode(2)).next(new ListNode(4));

        ListNode l2 = new ListNode(1);
        l2.next(new ListNode(3)).next(new ListNode(4));

        l1.print();
        l2.print();

        ListNode merge = mergeTwoLists(l1,l2);
        merge.print();
    }

}
