public class Task328 {
    public ListNode oddEvenList(ListNode head) {
        if (head == null) {
            return head;
        }

        ListNode cur = head, prev = head;

        while (cur.next != null && cur.next.next != null) {
            ListNode next = cur.next;
            ListNode nextnext = next.next;
            next.next = nextnext.next;
            nextnext.next = prev.next;
            prev.next = nextnext;

            //next loop
            prev = prev.next;
            cur = next;

        }

        return head;
    }

    public ListNode oddEvenList2(ListNode head) {
        if (head == null) {
            return head;
        }

        ListNode odd = head, even = new ListNode(-1), evenHead = even;

        while (odd.next != null && odd.next.next != null) {
            even.next = odd.next;
            odd.next = odd.next.next;

            odd = odd.next;
            even = even.next;
        }
        even.next = odd.next;
        odd.next = evenHead.next;

        return head;
    }
}
