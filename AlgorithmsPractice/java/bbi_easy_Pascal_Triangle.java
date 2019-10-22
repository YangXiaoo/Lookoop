/**
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
*/

// 2018-7-13
// 118. Pascal's Triangle
public class bbi_easy_Pascal_Triangle {
    public static void main(String[] args) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        int numRows = 5;
        res = solution.generate(numRows);
        System.out.println(Arrays.toString(res));
    }
    public static List<List<Integer>> generate(int numRows) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        int s = 0;
        while (s < numRows) {
            List<Integer> tmp = new ArrayList<Integer>();
            int t = 1;
            tmp.add(1);
            while (t < s) {
                List<Integer> row = res.get(s-1);
                tmp.add(row.get(t) + row.get(t-1));
                t++;
            }
            if (s > 0)
                tmp.add(1);
            res.add(new ArrayList(tmp));
            s++;
        }

        return res;
    }
}