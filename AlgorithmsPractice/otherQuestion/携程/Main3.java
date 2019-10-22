import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
/*
在m个节点的分布式计算系统中，有一批任务需要执行，每个任务需要的时间是array[i]，每个节点同一时间只能执行一个任务，每个节点只能执行连续的任务，例如i,i+1,i+2,但是不能执行i,i+2。请问任务完成的最短时间

输入
输入数据包含两行

第一行，空格分隔的两个整数m和n，分别表示节点个数和任务个数(m>0,n>=0)

第二行，空格分隔的正整数序列，表示每个任务需要的时间

输出
一个整数，表示最短完成时间


样例输入
3 5
1 5 3 4 2
样例输出
6

提示
第一个节点执行：任务1和任务2，耗时=1+5=6
第二个节点执行：任务3，耗时=3
第三个节点执行：任务4和任务5，耗时=4+2=6
所以，总最短耗时=6
*/
// leetcode 410
public class Main3 {
/*请完成下面这个函数，实现题目要求的功能
当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^ 
******************************开始写代码******************************/
    static int schedule(int m,int[] array) {
        List<Integer> ret = new LinkedList<>();
        List<Integer> tmp = new LinkedList<>();
        dfs(m, array, tmp, ret, 0);

        int min = ret.get(1);
        for (int i = 1; i < ret.size(); ++i) {
            if (ret.get(i) < min) {
                min = ret.get(i);
            }
        }

        return min;
}

    // 这个函数有问题【2019/9/4 22:01 已修改】
    static int computeSum(List<Integer> list, int[] array) {
        int min = 0;
        for (int i = 0; i < list.size() - 1; ++i) {
            int tmp = 0;
            int last = list.get(i+1);
            if (i == (list.size() - 2)) {
                last = array.length;
            }
            for (int j = list.get(i); j < last; ++j) {
                tmp += array[j];
            }

            if (tmp > min) {
                min = tmp;
            }
        }

        return min;
    }
    
    // 获得所有组合方式
    static void dfs(int m, int[] array, List<Integer> tmp, List<Integer> ret, int curIndex) {
        if (tmp.size() == m) {
            int cur = computeSum(tmp, array);
            ret.add(cur);
        } else {
            for (int i = curIndex; i < array.length; ++i) {
                tmp.add(i);
                dfs(m, array, tmp, ret, i+1);
                tmp.remove(tmp.size()-1);
            }
        }
    }
/******************************结束写代码******************************/


    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        int m = in.nextInt();
        int size  = in.nextInt();
        int[] array = new int[size];
        for(int i = 0; i < size; i++) {
            array[i] = in.nextInt();
        }
        int res = schedule(m,array);
        System.out.println(String.valueOf(res));    
    }
}
