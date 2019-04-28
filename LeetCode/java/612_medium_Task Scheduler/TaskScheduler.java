/*
Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks. Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.

 

Example:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
 

Note:

The number of tasks is in the range [1, 10000].
The integer n is in the range [0, 100].
*/

// 2019-4-28
// 621. Task Scheduler [medium]
// https://leetcode.com/problems/task-scheduler/
import java.util.*;

public class TaskScheduler {
	// 公式(count(maxChar) - 1) * (n + 1) + maxCate
	// 即(最大词频出现此处 - 1) * (中间间隔数 + 1) + 最大词频相同次数

    public int leastInterval(char[] tasks, int n) {


    	// 获得任务中每个字符出现的次数
        HashMap<Character, Integer> map = new HashMap<>();
        for (char c : tasks) {
        	if (map.containsKey(c)) {
        		map.put(c, map.get(c) + 1);
        	} else {
        		map.put(c, 1);
        	}
        }

        // 对字典排序
        List<Map.Entry<Character, Integer>> list = new ArrayList<>(map.entrySet());
        Collections.sort(list, new Comparator<Map.Entry<Character, Integer>>() {
        	@Override
        	public int compare(Map.Entry<Character, Integer> en1, Map.Entry<Character, Integer> en2) {
        		return en1.getValue().compareTo(en2.getValue());
        	}
        });

        // 上面步骤可以用数组替代 
        // int[] taskCount = new int[26]; 
        // ...
        System.out.println(list.toString());
        int maxCount = 0, maxCate = 0;
        for (int i = 0; i < list.size(); ++i) {
        	if (list.get(i).getValue() > maxCount) {
        		maxCount = list.get(i).getValue();
        		maxCate = 1;
        	} else if (list.get(i).getValue() == maxCount) {
        		maxCate += 1;
        	}
        } 

        return Math.max(tasks.length, (maxCount - 1) * (n + 1) + maxCate);
    }


    public void test(String testName, char[] tasks, int n, int expect) {
    	int ret = leastInterval(tasks, n);
    	System.out.println(testName + ", expect: " + expect + ", result: " + ret);
    }

    public static void main(String[] args) {
    	TaskScheduler test = new TaskScheduler();

    	char[] tasks1 = {'A','A','A','B','B','B'};
    	test.test("test-1", tasks1, 2, 8);
    }
}