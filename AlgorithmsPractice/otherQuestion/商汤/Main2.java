import java.util.*;

public class Main2 {
    public static void main(String[] args) {
        Scanner cin = new Scanner(System.in);
        while (cin.hasNext()) {
            String line = cin.nextLine();
            String[] sNums = line.split(" ");
            String s = sNums[0];
            String[] map = sNums[1].split(",");
            String ret = solver(s, map);
            System.out.println(ret);
        }
    }

    public static String solver(String s, String[] map) {
        Deque<Integer> queue = new LinkedList<>();
        Set<Integer> visit = new HashSet<>();

        int lenS = s.length();
        int[] lenDict = new int[map.length];
        for (int i = 0; i < map.length; ++i) {
            lenDict[i] = map[i].length();
        }

        while (!queue.isEmpty()) {
            int curIndex = queue.pollLast();
            for (int j = 0; j < lenDict.length; ++j) {
                int curLens = curIndex + lenDict[j]+1;
                if (visit.contains(curLens)) {
                    continue;
                }

                if (s.substring(curIndex, curLens) == map[j]) {
                    if (curLens == s.length()) {
                        return "true";
                    }

                    queue.offerFirst(curLens);
                    visit.add(curLens);
                }
            }
        }

        return "false";
    }
}