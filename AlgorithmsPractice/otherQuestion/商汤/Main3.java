import java.util.*;

public class Main3 {
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
        int min = nums[0];
        int maxProfit = 0;
        for (int n : nums) {
            maxProfit = Math.max(maxProfit, n - min);
            if (n < min) {
                min = n;
            }
        }

        return String.valueOf(maxProfit);
    }
}