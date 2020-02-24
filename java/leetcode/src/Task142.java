public class Task142 {
    public ListNode detectCycle(ListNode head) {
        ListNode fast=head,slow = head;
        boolean flag = false;

        //phase1
        while(fast != null && fast.next != null && slow != null){
            slow = slow.next;
            fast = fast.next.next;
            if(slow == fast){
                flag = true;
                break;
            }
        }

        if(!flag){
            return null;
        }

        //phase2
        slow = head;
        while(slow != fast){
            slow = slow.next;
            fast = fast.next;
        }

        return slow;
    }
}
