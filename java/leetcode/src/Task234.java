import org.junit.jupiter.api.Test;

import java.util.Stack;

public class Task234 {
    public boolean isPalindrome(ListNode head) {
        if(head == null || head.next == null){
            return true;
        }

        ListNode cur = head;
        int size = 0;
        while(cur != null){
            ++size;
            cur = cur.next;
        }

        Stack<Integer> stack = new Stack<>();

        cur = head;
        int i = 0;
        while(i < size/2){
            stack.push(cur.val);
            cur = cur.next;
            ++i;
        }
        if((size & 1) == 1){
            cur = cur.next;
            ++i;
        }
        while(i < size){
            if(cur.val != stack.pop()){
                return false;
            }
            cur = cur.next;
            ++i;
        }

        return true;
    }

    @Test
    void test(){
        ListNode head = new ListNode(1);
        head.next(2).next(2).next(1);
        head.print();
        System.out.println(isPalindrome(head));
    }
}
