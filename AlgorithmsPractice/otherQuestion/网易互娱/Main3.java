import java.util.*;
import java.io.*;

// 2019/9/7
// 喝咖啡

public class Main3 {
    public static void main(String[] args) {
        Scanner cin = new Scanner(System.in);
        while (cin.hasNext()) {
            try {
                int t = cin.nextInt();  // 样例个数
                int[] ret = new int[t];
                for (int i = 0; i < t; ++i) {
                    int k = cin.nextInt(), m = cin.nextInt();
                    if (m == 0) {
                        int curRet = (int)(30 / (k + 1));
                        ret[i] = curRet;
                    } else if (k == 0) {
                        ret[i] = 30;
                    } else {
                        int[] must = new int[m+2];
                        must[0] = 0;
                        for (int j = 1; j <= m; ++j) {
                            must[j] = cin.nextInt();
                        }
                        must[m+1] = 31;
                        // 直接解决
                        int r = m;
                        for (int x = 1; x < m+2; ++x) {
                            int pre = must[x-1], next = must[x];
                            while (next > pre) {    // 该区间能够喝的次数
                                next -= (k + 1);
                                if (next > pre) {
                                    r += 1;
                                }
                            }
                        }
                        ret[i] = r;
                    }
                }

                for (int r : ret) {
                    System.out.println(r);
                }
            } catch (Exception e) {
                // pass
            }

        }
    }
}

/*
4
0 10
1 2 3 4 5 6 7 8 9 10
1 15
1 3 5 7 9 11 13 15 17 19 21 23 25 27 29
1 7
5 9 13 17 21 25 29
1 0

*/