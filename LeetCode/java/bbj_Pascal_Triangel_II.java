/**
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.
*/

// 2018-7-13
// 119. Pascal's Triangle II

public class bbj_Pascal_Triangel_II {
    public List<Integer> getRow(int rowIndex) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        int s = 0;
        while (s <= rowIndex) {
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

        return res.get(rowIndex);
    }
}