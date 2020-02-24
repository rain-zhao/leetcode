public class SwapNodesInPairs {
    public class ListNode {
        int val;
        ListNode next;

        ListNode(int x) {
            val = x;
        }
    }

    public ListNode swapPairs(ListNode head) {
        ListNode cur =head;
        ListNode newHead = cur;
        ListNode prev = new ListNode(0);
        ListNode next;
        ListNode temp;

        //assign new head
        if(cur != null && cur.next != null){
            newHead = cur.next;
        }
        while(cur != null && cur.next != null){
            //asign node
            next = cur.next;
            temp = next.next;
            //swap
            prev.next = next;
            next.next = cur;
            cur.next = temp;
            //recur
            prev = cur;
            cur = temp;
        }
        return newHead;
    }

    public ListNode swapPairs2(ListNode head) {
        //create prev
        ListNode prev = new ListNode(0);
        prev.next = head;

        ListNode temp = prev;
        ListNode cur,next;

        //loop
        while(prev.next != null && prev.next.next != null){
            cur = prev.next;
            next = cur.next;
            //swap
            cur.next = next.next;
            next.next = cur;
            prev.next = next;

            //recur
            prev = cur;
        }

        return temp.next;
    }
}
