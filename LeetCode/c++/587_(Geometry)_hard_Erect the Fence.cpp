/* 
There are some trees, where each tree is represented by (x,y) coordinate in a two-dimensional garden. Your job is to fence the entire garden using the minimum length of rope as it is expensive. The garden is well fenced only if all the trees are enclosed. Your task is to help find the coordinates of trees which are exactly located on the fence perimeter.

Example 1:
Input: [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
Output: [[1,1],[2,0],[4,2],[3,3],[2,4]]
Explanation:

Example 2:
Input: [[1,2],[2,2],[4,2]]
Output: [[1,2],[2,2],[4,2]]
Explanation:

Even you only have trees in a line, you need to use rope to enclose them. 
Note:

All trees should be enclosed together. You cannot cut the rope to enclose trees that will separate them in more than one group.
All input integers will range from 0 to 100.
The garden has at least one tree.
All coordinates are distinct.
Input points have NO order. No order required for output.

===================================================================
*/
// 2018-8-30
// 587. Erect the Fence
// https://leetcode.com/problems/erect-the-fence/description/

// https://leetcode.com/problems/erect-the-fence/discuss/103299/Java-Solution-Convex-Hull-Algorithm-Gift-wrapping-aka-Jarvis-march




// 使用 Andrew's Monotone Chain Algorithm 算法实现
// 算法介绍： http://geomalgorithms.com/a10-_hull-1.html
// 算法程序： http://www.algorithmist.com/index.php/Monotone_Chain_Convex_Hull.cpp

/*
Andrew's Monotone Chain Algorithm
[Andrew, 1979] discovered an alternative to the Graham scan that uses a linear lexographic sort of the point set by the x and y-coordinates. This is an advantage if this ordering is already known for a set, which is sometimes the case. But even if sorting is required, this is a faster sort than the angular Graham-scan sort with its more complicated comparison function. The "Monotone Chain" algorithm computes the upper and lower hulls of a monotone chain of points, which is why we refer to it as the "Monotone Chain" algorithm. Like the Graham scan, it runs in O(nlog-n) time due to the sort time. After that, it only takes O(n) time to compute the hull. This algorithm also uses a stack in a manner very similar to Graham's algorithm.

First the algorithm sorts the point set S={P0,P1,...,Pn-1} by increasing x and then y coordinate values. Let the minimum and maximum x-coordinates be xmin and xmax. Clearly, P0.x=x-min, but there may be other points with this minimum x-coordinate. Let Pminmin be a point in S with P.x=x-min first and then min y among all those points. Also, let Pminmax be the point with P.x=x-min first and then max y second. Note that Pminmin=Pminmax when there is a unique x-minimum point. Similarly define Pmaxmin and Pmaxmax as the points with P.x=x-max first, and then y min or max second. Again note that Pmaxmin=Pmaxmax when there is a unique x-maximum point. Next, join the lower two points, Pminmin and Pmaxmin to define a lower line L-min. Also, join the upper two points, Pminmax and Pmaxmax to define an upper line L-max. These points and lines are shown in the following example diagram.


The algorithm now proceeds to construct a lower convex vertex chain OMEGA-min below L-min and joining the two lower points Pminmin and Pmaxmin; and also an upper convex vertex chain OMEGA-max above L-max and joining the two upper points Pmaxmax and Pminmax. Then the convex hull OMEGA of S is constructed by joining OMEGA-min and OMEGA-max together.

The lower or upper convex chain is constructed using a stack algorithm almost identical to the one used for the Graham scan. For the lower chain, start with Pminmin on the stack. Then process the points of S in sequence. For OMEGA-min, only consider points strictly below the lower line L-min. Suppose that at any stage, the points on the stack are the convex hull of points below L-min that have already been processed. Now consider the next point Pk that is below L-min. If the stack contains only the one point Pminmin then put Pk onto the stack and proceed to the next stage. Otherwise, determine whether Pk is strictly left of the line between the top two points on the stack. If it is, put Pk onto the stack and proceed. If it is not, pop the top point off the stack, and test Pk against the stack again. Continue until Pk gets pushed onto the stack. After this stage, the stack again contains the vertices of the lower hull for the points already considered. The geometric rationale[ˌræʃəˈnæl] is exactly the same as for the Graham scan. After all points have been processed, push Pmaxmin onto the stack to complete the lower convex chain.

The upper convex chain OMEGA-max is constructed in an analogous[əˈnæləɡəs] manner. But, process S in decreasing order {Pn-1,Pn-2,...,P0}, starting at Pmaxmax, and only considering points above L-max. Once the two hull chains have been found, it is easy to join them together (but be careful to avoid duplicating the endpoints).


Pseudo-Code: Andrew's Monotone Chain Algorithm



    Input: a set S = {P = (P.x,P.y)} of N points

    Sort S by increasing x and then y-coordinate.
    Let P[] be the sorted array of N points.

    Get the points with 1st x min or max and 2nd y min or max
        minmin = index of P with min x first and min y second
        minmax = index of P with min x first and max y second
        maxmin = index of P with max x first and min y second
        maxmax = index of P with max x first and max y second

    Compute the lower hull stack as follows:
    (1) Let L_min be the lower line joining P[minmin] with  P[maxmin].
    (2) Push P[minmin] onto the stack.
    (3) for i = minmax+1 to maxmin-1 (the points between xmin and xmax)
        {
            if (P[i] is above or on L_min)
                Ignore it and continue.
            while (there are at least 2 points on the stack)
            {
                Let PT1 = the top point on the stack.
                Let PT2 = the second point on the stack.
                if (P[i] is strictly left of the line from PT2 to PT1)
                // https://blog.csdn.net/tuibianyanzi/article/details/51884501
                    break out of this while loop.
                Pop the top point PT1 off the stack.
            }
            Push P[i] onto the stack.
        }
    (4) Push P[maxmin] onto the stack.

    Similarly, compute the upper hull stack.

    Let OMEGA = the join of the lower and upper hulls.

    Output: OMEGA = the convex hull of S.
*/

/*

*/
/**
 * Definition for a point.
 * struct Point {
 *     int x;
 *     int y;
 *     Point() : x(0), y(0) {}
 *     Point(int a, int b) : x(a), y(b) {}
 * };
 */
class Solution {
public:
    vector<Point> outerTrees(vector<Point>& points) {
        
    }
};