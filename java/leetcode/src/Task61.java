public class Task61 {
    public ListNode rotateRight(ListNode head, int k) {
        if (head == null || k == 0) {
            return head;
        }

        ListNode p1 = head;
        int i = 0;
        while (i < k && p1.next != null) {
            p1 = p1.next;
            ++i;
        }
        if (i < k) {
            k %= (i+1);
            p1 = head;
            i = 0;
            while (i < k) {
                p1 = p1.next;
                ++i;
            }
        }


        ListNode p2 = head;
        while (p1.next != null) {
            p1 = p1.next;
            p2 = p2.next;
        }

        p1.next = head;
        head = p2.next;
        p2.next = null;

        return head;
    }
}
