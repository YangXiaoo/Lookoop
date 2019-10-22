import java.util.*;

public class Main1 {
    public static void main(String[] args) {
        Scanner cin = new Scanner(System.in);
        while (cin.hasNext()) {
            String s = cin.nextLine();
            String[] sNums = s.split(" ");
            int[] nums = new int[sNums.length];
            for (int i = 0; i < sNums.length; ++i) {
                nums[i] = Integer.parseInt(sNums[i]);
            }

            String ret = solver(nums);
            System.out.println(ret);
        }
    }

    public static String solver(int[] nums) {
        int x1 = nums[0], y1 = nums[1], w1 = nums[2], h1 = nums[3];
        int x2 = nums[4], y2 = nums[5], w2 = nums[6], h2 = nums[7];

        int w = Math.min(x1 + w1, x2 + w2);
        int h = Math.min(y1 + h1, y2 + h2);
        int x = Math.max(x1, x2);
        int y = Math.max(y1, y2);

        if (x >= w && y >= h) 
            return "null";

        StringBuilder sb = new StringBuilder();
        sb.append(x + " ");
        sb.append(y + " ");
        sb.append(w - x + " ");
        sb.append(h - y);

        return sb.toString();
    }
}