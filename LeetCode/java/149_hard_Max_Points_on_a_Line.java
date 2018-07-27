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
class 149_hard_Max_Points_on_a_Line {
    public int maxPoints(Point[] points) {
        int lens = points.length;
        int max = 2;
        if (lens < 3 ) return lens;
        for (int i = 0; i < lens - 2; i++) {
            for (int j = i + 1; j < lens - 1; j++) {
                Point m = points[j];
                Point n = points[i];
                int a = m.x - n.x;
                int x1 = m.x;
                int b = m.y - n.y;
                int y1 = m.y;
                int length = 2;
                for (int k = j + 1; k < lens; k++) {
                    Point p = points[k];
                    if (a == 0 && b != 0) {
                        if (x1 == p.x) length++;
                        continue;
                    }

                    if (b == 0 && a != 0) {
                        if (y1 == p.y) length++;
                        continue;
                    }
                    
                    if (a*(p.x - x1) - b*(p.y - y1) == 0) {
                        length++;
                    }
                }

                if (length > max) max = length;
            }
        }

        return max;
    }
}