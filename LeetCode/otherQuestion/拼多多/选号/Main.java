public class Main {
    public static void main(String[] args) {
    	Scanner cin = new Scanner(System.in);
    	while (cin.hasNext()) {
    		String ns = cin.next(), ks = cin.next();
    		int N = Integer.parseInt(ns);
    		int K = Integer.parseInt(ks);
    		String line = cin.next();
    		int[] number = new int[line.length()];
    		for (int = 0; i < line.length(); ++i) {
    			number[i] = line.charAt(i) - '0';
    		}

    		solver(N, K, number);
    	}
    }

    public static void solver(int N, int K, int[] number) {
    	// 返回至少需要的金额，输出字典序最小的靓号
    	int[] old = Arrays.copyOf(number, number.length);

    	Set<Integer> set = new HashSet<>();
    	for (int n : old) {
    		set.add(n);
    	}
    	Arrays.sort(number);

    }
}