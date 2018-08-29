/* 
Given the radius and x-y positions of the center of a circle, write a function randPoint which generates a uniform random point in the circle.

Note:

input and output values are in floating-point.
radius and x-y position of the center of the circle is passed into the class constructor.
a point on the circumference of the circle is considered to be in the circle.
randPoint returns a size 2 array containing x-position and y-position of the random point, in that order.
Example 1:

Input: 
["Solution","randPoint","randPoint","randPoint"]
[[1,0,0],[],[],[]]
Output: [null,[-0.72939,-0.65505],[-0.78502,-0.28626],[-0.83119,-0.19803]]
Example 2:

Input: 
["Solution","randPoint","randPoint","randPoint"]
[[10,5,-7.5],[],[],[]]
Output: [null,[11.52438,-8.33273],[2.46992,-16.21705],[11.13430,-12.42337]]
Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has three arguments, the radius, x-position of the center, and y-position of the center of the circle. randPoint has no arguments. Arguments are always wrapped with a list, even if there aren't any.

===================================================================
*/
// 2018-8-29
// 478. Generate Random Point in a Circle
// https://leetcode.com/problems/generate-random-point-in-a-circle/description/


class Solution {
private:
    double radius, x_center, y_center;

public:
    const double PI = 3.141592653589797323846264338327;
    Solution(double radius, double x_center, double y_center) {
        this->radius = radius;
        this->x_center = x_center;
        this->y_center = y_center;
    }

    double uniform()
    {
        // 产生0 - 1 的伪均匀分布随机数
        return rand() * 1.0 / (RAND_MAX * 1.0);
    }  

    vector<double> randPoint() {
        double theta = 2 * PI * uniform();
        // 使用sqrt()是为了让点在不同直径圆上的点均匀分布，详看以下链接
        // https://leetcode.com/problems/generate-random-point-in-a-circle/discuss/155650/Explanation-with-Graphs-why-using-Math.sqrt()
        double r = sqrt(uniform());
        vector<double> res = {x_center + r * radius * cos(theta), y_center + r * radius * sin(theta)};

        return res;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(radius, x_center, y_center);
 * vector<double> param_1 = obj.randPoint();
 */