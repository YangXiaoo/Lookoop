/**
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

*/
/**
解题思路：
动态规划方法，建立转移方程
【1】自顶向下：
MP[i][j] = min(MP[i][j],MP[i][j+1]+triangle[i][j])
需要n^2 space
【2】 自底向上
MP(3,0)=triangle[3][0]=4;

MP(3,1)=triangle[3][1]=1;

MP(3,2)=triangle[3][1]=8;

MP(3,3)=triangle[3][1]=3;

MP(2,0)=min{MP(3,0),MP(3,1)}+triangle[2][0]=1+6=7;

MP(2,1)=min{MP(3,1),MP(3,2)}+triangle[2][1]=1+5=6;

MP(2,2)=min{MP(3,2),MP(3,3)}+triangle[2][2]=3+7=10;

MP(1,0)=min{MP(2,0),MP(2,1)}+triangle[1][0]=6+3=9;

MP(1,1)=min{MP(2,1),MP(2,2)}+triangle[1][1]=6+6=12;

MP(0,0)=min{MP(1,0),MP(1,1)}+triangle[0][0]=9+2=11;
*/
// 2018-7-13
// 120. Triangle

public class bca_medium_Triangle {
    public int minimumTotal(List<List<Integer>> triangle) {

        int length = triangle.size();
        if(length == 0) return 0;
        if(length == 1) return triangle.get(0).get(0);
        
        List<Integer> sum = triangle.get(length-1);
        for(int i = length - 2; i >= 0; i--)
        {
            for(int j = 0; j<triangle.get(i).size(); j++)
            {
                int sum1 = triangle.get(i).get(j) + sum.get(j);
                int sum2 = triangle.get(i).get(j) + sum.get(j + 1);
                sum.set(j, Math.min(sum1, sum2));
            }
        }
        return sum.get(0);
        
