import java.util.*;
// 输入 {1,2,3,4,5,19}
// 输出：19所在位置，不存在则输出-1

public class Main02 {
	public static void main(String[] args) {
		Scanner cin = new Scanner(System.in);
		while (cin.hasNext()) {
			String line = cin.nextLine();
			List<Integer> list = new ArrayList<>();
			if (!line.contains(",") && line.length() == 2) {
				System.out.println("-1");
				return;
			}
			String[] strList = line.split(",");
			if (strList.length == 1) {
				strList[0] = line.substring(0, line.length()-1);
			}
			Integer[] array = new Integer[strList.length];
			for (int i = 0; i < strList.length; ++i) {
				if (i == 0) {
					array[i] = Integer.parseInt(strList[i].substring(1, strList[i].length()));
				}else if (i == strList.length - 1) {
					array[i] = Integer.parseInt(strList[i].substring(0, strList[i].length() - 1));
				} else {
					array[i] = Integer.parseInt(strList[i]);
				}
			}
			int ret = binarySearch(array, 19, 0, array.length - 1);
			// 忘记这步判断了！！！
			if (ret >= 0) {
				ret += 1;
			}
			System.out.println(ret);
		}
	}

	public static int binarySearch(Integer[] array, Integer target, int left, int right) {
		if (left <= right ) {
			int mid = (right + left) / 2;
			if (array[mid] == target) {
				return mid;
			} else if (array[mid] < target) {
				return binarySearch(array, target, mid + 1, right);
			}else {
				return binarySearch(array, target, left, mid - 1);
			}
		} else {
			return -1;
		}
	}	
}