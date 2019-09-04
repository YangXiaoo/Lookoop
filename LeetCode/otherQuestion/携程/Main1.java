import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

/*
链表排序
时间限制：C/C++语言 1000MS；其他语言 3000MS
内存限制：C/C++语言 65536KB；其他语言 589824KB
题目描述：
给定一个单向链表和一个整数m，将链表中小于等于m的节点移到大于m的节点之前，要求两部分中的节点各自保持原有的先后顺序

输入
输入数据包含两行，

第一行，整数m

第二行，空格分隔的整数序列

输出
逗号分隔的整数序列


样例输入
4
9 6 3 7 6 5
样例输出
3,9,6,7,6,5
*/
// 2019/9/4
// AC 100%
public class Main {

	 public static class ListNode {
	     int val;
	     ListNode next;
	     ListNode(int x) {
	         val = x;
	         next = null;
	     }
	 }

/*请完成下面这个函数，实现题目要求的功能
******************************开始写代码******************************/
    static ListNode partition(ListNode head,int m) {
        ListNode leftHead = new ListNode(0);
        ListNode lDummy = leftHead;
        ListNode rightHead = new ListNode(0);
        ListNode rDummy = rightHead;
        ListNode cur = head;
        // 先判断特殊情况
        if (cur == null || cur.next == null) {
        	return head;
        }

        while (cur != null) {
        	ListNode next = cur.next;	// 下一个节点
        	cur.next = null;
        	if (cur.val <= m) {
        		lDummy.next = cur;
        		lDummy = lDummy.next;
        	} else {
        		rDummy.next = cur;
        		rDummy = rDummy.next;
        	}

        	cur = next;
        }
        // 拼接
        lDummy.next = rightHead.next;
        
        return leftHead.next;
    }
/******************************结束写代码******************************/


    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        ListNode head=null;
        ListNode node=null;
        int m=in.nextInt();
        while(in.hasNextInt()){
            int v=in.nextInt();
            if(head==null){
                node=new ListNode(v);
                head=node;
            }else{
                node.next=new ListNode(v);
                node=node.next;
            }
        }
        head= partition(head,m);
        if(head!=null){
              System.out.print(head.val);
              head=head.next;
              while(head!=null){
                    System.out.print(",");
                    System.out.print(head.val);
                    head=head.next;
              }
         }
         System.out.println();
    }
}
