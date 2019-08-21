import java.util.*;

public class Main2 {
    public static void main(String[] args) {
        Scanner cin = new Scanner(System.in);
        while (cin.hasNext()) {
            String s = cin.nextLine();
            String[] sNums = s.split(" ");
            int[] nums = new int[sNums.length];
            for (int i = 0; i < sNums.length; ++i) {
                nums[i] = Integer.parseInt(sNums[i]);
            }

            int ret = solver(nums[0], nums[1]);
            System.out.println(ret);
        }
    }

    public static int solver(int low, int high) {
    	List<Integer> list = new ArrayList<>();
    	for (; low < high; ++low) {
    		boolean flag = true;
    		for (int j = 2; j < (int)Math.sqrt(low); ++j) {
    			if (low % j == 0) {
    				flag = false;
    				break;
    			}
    		}

    		if (flag) {
    			list.add(low);
    		}
    	}

    	if (list.size() == 0) {
    		return 0;
    	}

    	int ret1 = 0, ret2 = 0;
    	for (int i = 0; i < list.size(); ++i) {
    		int cur = list.get(i);
    		if (cur >= 10) {
    			ret2 += (int)(cur / 10);
    		}
    		ret1 += cur % 10;
    	}

    	return Math.min(ret1, ret2);
    }
}