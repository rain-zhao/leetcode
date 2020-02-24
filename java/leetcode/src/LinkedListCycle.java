import java.util.HashSet;
import java.util.Set;

public class LinkedListCycle {


    //使用快慢指针
    public boolean hasCycle1(ListNode head) {
        ListNode fast=head,slow = head;

        while(fast != null && fast.next != null && slow != null){
            slow = slow.next;
            fast = fast.next.next;
            if(slow == fast){
                return true;
            }
        }

        return false;
    }

    //使用hashset
    public boolean hasCycle2(ListNode head) {
        ListNode cur = head;
        Set set = new HashSet(8);

        while(cur != null){
            if(set.contains(cur)){
                return true;
            }
            set.add(cur);
            cur = cur.next;
        }
        return false;
    }
}
