class ListNode {
    int val;
    ListNode next;

    ListNode(int x) {
        val = x;
        next = null;
    }

    ListNode next(ListNode next) {
        this.next = next;
        return next;
    }
    ListNode next(int nextVal){
        this.next = new ListNode(nextVal);
        return next;
    }

    public void print(){
        StringBuilder sb = new StringBuilder();
        sb.append(val + "->");
        ListNode node = next;
        while(node != null){
            sb.append(node.val + "->");
            node = node.next;
        }
        sb.append("#");
        System.out.println(sb.toString());

    }

}