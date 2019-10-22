// 2019/9/9

class Node {
    int val;
    Node next = null;
    public Node(int val) {
        this.val = val;
    }
}

public class Main1 {
    public static void main(String[] args) {
        // test
        int[] nums = {1, 2, 3, 4};
        Node head = getLinkedList(nums);
        head = reverseLinkedList(head);
        printLinkedList(head);  // 4 -> 3 -> 2 -> 1 -> null
    }
    
    // 翻转链表
    // return Node
    public static Node reverseLinkedList(Node head) {
        Node cur = head;
        Node pre = null;    // 定义翻转链表头结点
        while (cur != null) {
            Node curNext = cur.next;    // 保存下一个节点
            cur.next = pre;
            pre = cur;
            cur = curNext;
        }
        
        return pre;
    }

    public static Node getLinkedList(int[] nums) {
        Node head = new Node(0);
        Node cur = head;
        for (int n : nums) {
            cur.next = new Node(n);
            cur = cur.next;
        }

        return head.next;
    }

    public static void printLinkedList(Node head) {
        Node cur = head;
        while (cur != null) {
            System.out.print(cur.val + " -> ");
            cur = cur.next;
        }
        System.out.print("null\n");
    }
}