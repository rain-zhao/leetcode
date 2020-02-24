import org.junit.jupiter.api.Test;

import java.util.Stack;

public class Task445 {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {

        if(l1 == null){
            return l2;
        }
        if(l2 == null){
            return l1;
        }

        ListNode r1 = reverse(l1);
        ListNode r2 = reverse(l2);

        ListNode prev = new ListNode(-1);

        int carry = 0;
        ListNode cur1 = r1,cur2=r2,cur = prev;

        while(r1 != null || r2 != null){
            int val1 = r1==null? 0:r1.val;
            int val2 = r2 == null ? 0:r2.val;

            int val = (carry+val1+val2)%10;
            carry = (carry+val1+val2)/10;

            cur.next = new ListNode(val);
            cur = cur.next;
            r1 = r1 == null ? null : r1.next;
            r2 = r2 == null ? null : r2.next;

        }

        if(carry == 1){
            cur.next = new ListNode(carry);
        }

        ListNode r3 = prev.next;

        return reverse(r3);
    }

    ListNode reverse(ListNode node){
        if(node == null){
            return node;
        }

        ListNode prev = null;
        ListNode cur = node;
        while(cur != null){
            ListNode next = cur.next;
            cur.next = prev;
            prev = cur;
            cur = next;
        }

        return prev;
    }


    //use stack
    public ListNode addTwoNumbers2(ListNode l1, ListNode l2) {
        if(l1 == null){
            return l2;
        }
        if(l2 == null){
            return l1;
        }

        ListNode prev = new ListNode(-1);

        Stack<ListNode> stack1 = new Stack<>();
        Stack<ListNode> stack2 = new Stack<>();

        ListNode cur1=l1,cur2=l2;
        while (cur1 != null){
            stack1.push(cur1);
            cur1 = cur1.next;
        }
        while (cur2 != null){
            stack2.push(cur2);
            cur2 = cur2.next;
        }

        int carry = 0;
        while(!stack1.isEmpty() || !stack2.isEmpty()){

            int val1 = stack1.isEmpty() ? 0: stack1.pop().val;
            int val2 = stack2.isEmpty() ? 0: stack2.pop().val;

            int val = (carry+val1+val2)%10;
            carry = (carry+val1+val2)/10;

            ListNode node = new ListNode(val);
            node.next = prev.next;
            prev.next = node;

        }
        if(carry == 1){
            ListNode node = new ListNode(carry);
            node.next = prev.next;
            prev.next = node;

        }

        return prev.next;
    }

    @Test
    void test(){
        ListNode l1 = new ListNode(7);
        l1.next(2).next(4).next(3);
        l1.print();
        ListNode l2 = new ListNode(5);
        l2.next(6).next(4);
        l2.print();

        ListNode res = addTwoNumbers2(l1,l2);
        res.print();
    }
}
