import javax.sound.midi.Soundbank;
import java.util.ArrayList;
import java.util.List;

public class ReverseNodesInKGroup {

    public static ListNode reverseKGroup(ListNode head, int k) {
        if(k<2){
            return head;
        }
        if(head == null || head.next == null){
            return head;
        }

        ListNode prev = new ListNode(0);
        prev.next = head;

        ListNode temp = prev;

        ListNode cur = head;

        ListNode[] array = new ListNode[k+1];

        int i=0;
        while(cur != null){
            //put to list
            array[i] = cur;

            if(i == k-1){
                ListNode next = cur.next;
                array[k] = prev;
                reverse(array);
                i=0;
                prev = array[0];
                cur = next;
            }else{
                cur=cur.next;
                ++i;
            }

        }

        if(prev != array[0]){
            prev.next = array[0];
        }else{
            prev.next = null;
        }

        return temp.next;
    }

    public static void reverse(ListNode[] array){
        for(int i = array.length-1; i> 0;--i){
            array[i].next =  array[i-1];
        }
    }


    //recursion
    public static ListNode reverseKGroup2(ListNode head, int k) {
        if(k<2){
            return head;
        }

        ListNode[] array = new ListNode[k+1];

        ListNode cur = head;

        for(int i = 0;i< k; ++i){
            if(cur == null){
                return head;
            }
            array[i]= cur;
            cur = cur.next;
        }

        //reverse
        for(int i = k-1; i > 0;--i){
            array[i].next =  array[i-1];
        }

        //connect
        array[0].next = reverseKGroup2(cur,k);

        return  array[k-1];

    }

    public static void main(String[] args) {
        ListNode a = new ListNode(1);
        ListNode b = new ListNode(2);
        ListNode c = new ListNode(3);
        ListNode d = new ListNode(4);
        ListNode e = new ListNode(5);
        a.next = b;
        b.next=c;
        c.next =d;
        d.next = e;
        int k = 2;
        ListNode head= reverseKGroup2(a,k);

        System.out.println(head);
    }

}
