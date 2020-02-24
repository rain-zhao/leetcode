/**
 * Definition for singly-linked list.
 * public class ListNode {
 * int val;
 * ListNode next;
 * ListNode(int x) { val = x; }
 * }
 */
public class ReverseLinkedList {

    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode curNode = head;
        ListNode newHead;
        while (curNode != null) {
            //cache next node
            newHead = curNode.next;
            //insert before prev
            curNode.next = prev;
            prev = curNode;
            //next node
            curNode = newHead;
        }

        return prev;
    }

}
