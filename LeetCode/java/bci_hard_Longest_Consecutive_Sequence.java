/**
Given an unsorted array of integers, find the length of the longest consecutive(连续的) elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
*/

// 2018-7-20
// 128. Longest Consecutive Sequence
class bci_hard_Longest_Consecutive_Sequence {
    public int longestConsecutive(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<>();
        int max = 0;

        for (int i : nums) map.put(i, 0);

        for (int n : nums) {
            int curMax = 0;

            if (map.get(n) == 1) continue;

            int tmp = n;
            while (map.containsKey(tmp)) { // map.containsKey()
                map.put(tmp, 1);
                curMax++;
                tmp++;
            }

            tmp = n - 1;
            while (map.containsKey(tmp)) {
                map.put(tmp, 1);
                curMax++;
                tmp--;
            }

            max = Math.max(max, curMax);
        } // ~~~ end for 

        return max;
    }
}