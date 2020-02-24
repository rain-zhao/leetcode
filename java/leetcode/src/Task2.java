import org.junit.jupiter.api.Test;

public class Task2 {
    //1.转int 相加再转 listNode
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        long val1 = convert(l1);
        System.out.println("val1="+val1);
        long val2 = convert(l2);
        System.out.println("val2="+val2);
        long sum = val1+val2;
        System.out.println("sum="+sum);
        return convert(sum);

    }

    long convert(ListNode node){
        int depth = 0;
        long val = 0;
        while (node != null){
            val += node.val * Math.pow(10,depth++);
            node = node.next;
        }
        return val;
    }
    ListNode convert(long val){
        if(val == 0){
            return new ListNode(0);
        }

        ListNode prev = new ListNode(-1);
        ListNode cur = prev;
        while(val != 0){
            int subVal = (int)(val%10);

            ListNode node = new ListNode(subVal);
            cur.next = node;
            cur = node;

            val /=10;
        }

        return prev.next;
    }


    //reverse l1,l2 再相加（用原l1的空间）
    public ListNode addTwoNumbers2(ListNode l1, ListNode l2) {

        ListNode prev = new ListNode(-1);
        ListNode cur = prev,cur1 = l1 ,cur2=l2;


        int up = 0;
        while(cur1 != null || cur2 != null){

            int val1 = cur1 == null ? 0 : cur1.val;
            int val2 = cur2 == null ? 0 : cur2.val;

            int sum = (val1 + val2 + up)%10;
            up = (val1 + val2 + up)/10;

            ListNode node = new ListNode(sum);
            cur.next = node;


            cur = node;
            cur1 = cur1 == null ? null : cur1.next;
            cur2 = cur2 == null ? null : cur2.next;
        }

        if(up == 1){
            cur.next = new ListNode(1);
        }

        return prev.next;
    }

    @Test
    void test(){
        ListNode l1 = new ListNode(9);
//        l1.next(new ListNode(4)).next(new ListNode(3));

        ListNode l2 = new ListNode(1);
        l2.next(new ListNode(9))
                .next(new ListNode(9))
                .next(new ListNode(9))
                .next(new ListNode(9))
                .next(new ListNode(9))
                .next(new ListNode(9))
                .next(new ListNode(9))
                .next(new ListNode(9))
                .next(new ListNode(9));

        System.out.println(addTwoNumbers2(l1,l2));

    }

}
