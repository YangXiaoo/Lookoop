/**
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

Example 1:

Input: [[1,1],[2,2],[3,3]]
Output: 3
Explanation:
^
|
|        o
|     o
|  o  
+------------->
0  1  2  3  4
Example 2:

Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
Explanation:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6
 */

// 2018-7-27
// 149. Max Points on a Line
// https://leetcode-cn.com/problems/max-points-on-a-line/description/
// https://blog.csdn.net/tingting256/article/details/49647407
/**
 * Definition for a point.
 * class Point {
 *     int x;
 *     int y;
 *     Point() { x = 0; y = 0; }
 *     Point(int a, int b) { x = a; y = b; }
 * }
 */
// 结果溢出。可以考虑将Double转换为String类型，这样就不会溢出
class 149_hard_Max_Points_on_a_Line {
    public int maxPoints(Point[] points) {  
        int lens = points.length;
        if (lens < 3) return lens;
        int max = 0;
        for (int i = 0; i < lens; i++) {
            HashMap<Double, Integer> map = new HashMap<Double, Integer>();
            int dup = 1;
            for (int j = 0; j < lens; j++) {
                if (i == j) continue;

                Point p1 = points[i];
                Point p2 = points[j];
                double k = 0.0;
                if (p1.x == p2.x) {
                    if (p1.y == p2.y) {
                        dup++;
                        continue;
                    } else {
                        k = Double.MAX_VALUE;
                    }
                } else {
                    if (p1.x > p2.x) {
                        k = ((double) (p1.y - p2.y) / (p1.x - p2.x));
                    } else {
                        k = ((double) (p2.y - p1.y) / (p2.x - p1.x));
                    }
                }

                if (map.contiansKey(k)) {
                    map.put(k, map.get(k) + 1);
                } else {
                    map.put(k, 1)
                }
            }

            double key;
            if(map.size() == 0) max = max>dup?max:dup;
            for(Double d:map.keySet())
            {
                max = max >dup + map.get(d)?max:dup+map.get(d);
            }
        }
        return max;
    }
}