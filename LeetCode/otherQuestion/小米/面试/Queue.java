import java.util.*;
public class Queue {
    private Stack<Integer> stack1 = null;    // 入
    private Stack<Integer> stack2 = null;    // 出
    // private int capacity;    // 容量
    public Queue() {
        this.stack1 = new Stack<>();
        this.stack2 = new Stack<>();
    }
    public void add(int val) {
        stack1.push(val);
    }
    
    public Integer remove() {
        if (stack2.empty()) {    
            while (!stack1.empty()) {   
                int curVal = stack1.pop();  // 面试的时候写错了。。。
                stack2.push(curVal);
            }
        }
        
        if (stack2.empty()) {
            System.out.println("queue is empty");
            return -1;    // 队列为空返回-1
        }
        
        int ret = stack2.pop();
        return ret;
    }
}