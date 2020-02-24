import org.junit.jupiter.api.Test;

import java.util.HashSet;
import java.util.Set;

public class Task160 {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {

        Set<ListNode> set = new HashSet<>();
        ListNode cur1=headA,cur2=headB;
        while(cur1 != null){
            set.add(cur1);
            cur1 = cur1.next;
        }

        while(cur2 != null){
            if(set.contains(cur2)){
                return cur2;
            }
            cur2 = cur2.next;
        }

        return null;
    }

    public ListNode getIntersectionNode2(ListNode headA, ListNode headB) {
        if(headA == null || headB == null){
            return null;
        }
        if(headA == headB){
            return  headA;
        }

        ListNode cur1=headA,cur2=headB;
        int status = 0;

        while (status != 2){
            if(cur1.next == null){
                ++status;
                cur1 = headB;
            }else{
                cur1 = cur1.next;
            }
            if(cur2.next == null){
                ++status;
                cur2 = headA;
            }else{
                cur2 = cur2.next;
            }

        }
        while (cur1 != null){
            if(cur1 == cur2){
                return cur1;
            }
            cur1 = cur1.next;
            cur2 = cur2.next;
        }

        return null;
    }


    @Test
    void test(){
        ListNode headA = new ListNode(4);
        headA.next(1).next(8).next(4).next(5);
        headA.print();
        ListNode headB = new ListNode(5);
        headB.next(0).next(1).next(headA.next.next);
        headB.print();

        ListNode node = getIntersectionNode2(headA,headB);

        node.print();

    }
}
