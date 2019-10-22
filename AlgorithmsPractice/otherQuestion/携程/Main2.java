import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
/*
豚厂给自研的数据库设计了一套查询表达式，在这个表达式中括号表示将里面的字符串翻转。请你帮助实现这一逻辑

输入
一行字符串

输出
一行字符串

如果表达式括号不匹配，输出空字符串


样例输入
((ur)oi)
样例输出
iour
*/

// AC 84%
public class Main2 {


/*请完成下面这个函数，实现题目要求的功能
当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^ 
******************************开始写代码******************************/
    static String resolve(String expr) {
        // 先判断括号不匹配的情况
        if (!goodCase(expr)) {
            return "";
        }
        Stack<String> stack = new Stack<>();
        StringBuilder tmp = new StringBuilder();
        for (int i = 0; i < expr.length(); ++i) {
            if (expr.charAt(i) == '(') {
                stack.push(tmp.toString());
            } else if (expr.charAt(i) == ')') {
                String tmpCur = tmp.toString();
                String pre = stack.pop();
                pre += tmpCur;
                tmpCur = reverse(pre); //翻转
                if (!stack.empty()) {   // 特殊情况
                    pre = stack.pop();
                    pre += tmpCur;
                    stack.push(pre);   
                } else {
                    stack.push(tmpCur);
                }
                tmp = new StringBuilder();
            } else {
                tmp.append(expr.charAt(i));
            }
        }
        if (stack.empty()) {
            return tmp.toString();
        } else {
            return stack.pop();
        }
        
    }

    // 翻转字符串
    static String reverse(String s) {
        StringBuilder sb = new StringBuilder();
        for (int i = s.length() - 1; i >= 0; --i) {
            sb.append(s.charAt(i));
        }

        return sb.toString();
    }

    // 判断表达式括号是否匹配
    static boolean goodCase(String s) {
        Stack<Character> stack = new Stack<>();
        for (int i = 0; i < s.length(); ++i) {
            if (s.charAt(i) == '(') {
                stack.push('(');
            } else if (s.charAt(i) == ')') {
                if (stack.empty()) {
                    return false;
                }
                Character tmp = stack.pop();
                if (tmp != '(') {
                    return false;
                }
            }
        }
        // System.out.println(stack.toString());
        if (stack.empty()) return true;

        return false;
    }
/******************************结束写代码******************************/


    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        while (in.hasNext()) {
            String res;
            String _expr;
            try {
                _expr = in.nextLine();
            } catch (Exception e) {
                _expr = null;
            }
      
            res = resolve(_expr);
            System.out.println(res);
        }
            

    }
}
